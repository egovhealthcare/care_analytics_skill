#!/usr/bin/env python
"""Generate static schema catalogs for AI-assisted analytics.

This reads Django model source and Pydantic resource specs without importing the
project. That keeps it usable when the local database or plug setup is absent.
"""

from __future__ import annotations

# ruff: noqa: PLR0911, PLR0912, T201
import ast
import json
import os
import shutil
import subprocess
import sys
from collections import OrderedDict, defaultdict
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

REPO_DIR = Path(__file__).resolve().parents[1]
# Vendored mode: this script lives in care_analytics_skill (shards ship with
# the plugin). Otherwise it's a copy running from care's own scripts/.
VENDORED = (REPO_DIR / "skills" / "care-analytics").is_dir()


def _git(*args: str, cwd: Path | None = None, check: bool = True) -> str:
    result = subprocess.run(
        ["git", *args], cwd=cwd, check=False, capture_output=True, text=True
    )
    if check and result.returncode != 0:
        where = f" (in {cwd})" if cwd else ""
        sys.exit(
            f"error: `git {' '.join(args)}`{where} failed:\n"
            f"{result.stderr.strip() or result.stdout.strip() or '(no output)'}"
        )
    return result.stdout.strip()


def _try_git(*args: str, cwd: Path | None = None) -> bool:
    return (
        subprocess.run(["git", *args], cwd=cwd, capture_output=True).returncode == 0
    )


def _clone_plugs(care_root: Path) -> None:
    """Clone git+ plugs from ADDITIONAL_PLUGS env or plugs.json into app/."""
    raw = os.environ.get("ADDITIONAL_PLUGS", "")
    if not raw and (REPO_DIR / "plugs.json").is_file():
        raw = (REPO_DIR / "plugs.json").read_text()
    if not raw.strip():
        return
    for plug in json.loads(raw):
        name = plug["name"]
        pkg = plug.get("package_name", name)
        ref = plug.get("version", "").lstrip("@")
        if pkg.startswith("git+"):
            dest = care_root / "app" / name
            if (dest / ".git").is_dir():
                _git("fetch", "--quiet", cwd=dest)
            else:
                _git("clone", "--quiet", pkg.removeprefix("git+"), str(dest))
            if ref:
                _git("checkout", "--quiet", ref, cwd=dest)
            print(f"plug: {name} @ {_git('rev-parse', '--short', 'HEAD', cwd=dest)}")
        elif "/" in pkg:
            print(f"plug: {name} (local path {pkg} — assumed present in care tree)")
        else:
            print(
                f"warning: plug {name} is a pip package ({pkg}) — no source to scan, skipped",
                file=sys.stderr,
            )


def _resolve_care_root() -> Path:
    """Locate a care checkout, cloning care and plugs if necessary."""
    env_root = os.environ.get("CARE_SOURCE_ROOT") or os.environ.get("CARE_ROOT")
    if env_root:
        root = Path(env_root).resolve()
    elif not VENDORED:
        root = REPO_DIR  # running from within care itself
    elif (REPO_DIR.parents[1] / "manage.py").is_file() and (
        REPO_DIR.parents[1] / "care"
    ).is_dir():
        root = REPO_DIR.parents[1]  # dev convenience: repo nested inside care
    else:
        root = REPO_DIR / ".care"  # gitignored clone
        repo = os.environ.get("CARE_REPO", "https://github.com/ohcnetwork/care")
        ref = os.environ.get("CARE_REF", "develop")
        if (root / ".git").is_dir():
            print(f"updating care checkout at {root} (ref: {ref}) ...", flush=True)
            usable = _try_git("fetch", "origin", cwd=root) and _try_git(
                "checkout", ref, cwd=root
            )
            if not usable:
                print(
                    f"warning: {root} is stale or partial — deleting and recloning",
                    file=sys.stderr,
                    flush=True,
                )
                shutil.rmtree(root)
        if not (root / ".git").is_dir():
            print(f"cloning {repo} into {root} ...", flush=True)
            _git("clone", repo, str(root))
            _git("checkout", ref, cwd=root)
        _git("pull", "--quiet", "--ff-only", "origin", ref, cwd=root, check=False)
    if not (root / "care").is_dir():
        sys.exit(f"error: no usable care checkout at {root} (set CARE_ROOT)")
    print(f"care: {root} @ {_git('rev-parse', '--short', 'HEAD', cwd=root, check=False) or 'unknown'}")
    _clone_plugs(root)
    return root


# Care source tree to scan. Resolved (and cloned, with plugs) at import so
# module-level catalogs like APP_CONFIGS see the final tree.
PROJECT_ROOT = _resolve_care_root()
OUTPUT_DIR = Path(
    os.environ.get(
        "AI_SCHEMA_OUTPUT_DIR",
        REPO_DIR if VENDORED else PROJECT_ROOT / "docs" / "ai-analytics-schema",
    )
)
# Markdown shards live inside the care-analytics skill so the plugin ships them.
SCHEMA_DIR = OUTPUT_DIR / "skills" / "care-analytics" / "schema"
OUTPUT_FILE = "physical-tables.json"
STALE_OUTPUT_FILES = ("models.json", "pydantic-specs.json", "jsonb-fields.json")

EXCLUDED_PARTS = {"migrations", "__pycache__", ".git", ".ruff_cache", "staticfiles"}

DJANGO_FIELD_CLASSES = {
    "AutoField",
    "BigAutoField",
    "SmallAutoField",
    "UUIDField",
    "CharField",
    "TextField",
    "EmailField",
    "URLField",
    "SlugField",
    "BooleanField",
    "NullBooleanField",
    "IntegerField",
    "BigIntegerField",
    "SmallIntegerField",
    "PositiveIntegerField",
    "PositiveSmallIntegerField",
    "PositiveBigIntegerField",
    "FloatField",
    "DecimalField",
    "DateField",
    "DateTimeField",
    "TimeField",
    "DurationField",
    "JSONField",
    "ArrayField",
    "ForeignKey",
    "OneToOneField",
    "ManyToManyField",
    "GenericForeignKey",
    "FileField",
    "ImageField",
}

RELATION_FIELD_CLASSES = {"ForeignKey", "OneToOneField", "ManyToManyField"}
MODEL_BASE_NAMES = {
    "Model",
    "BaseModel",
    "EMRBaseModel",
    "SlugBaseModel",
    "BaseFlag",
    "AbstractUser",
}
SPEC_BASE_NAMES = {"BaseModel", "RootModel", "EMRResource"}

FIELD_TYPE_MAP = {
    "AutoField": "integer",
    "BigAutoField": "integer",
    "SmallAutoField": "integer",
    "UUIDField": "uuid",
    "CharField": "string",
    "TextField": "string",
    "EmailField": "string",
    "URLField": "string",
    "SlugField": "string",
    "BooleanField": "boolean",
    "NullBooleanField": "boolean",
    "IntegerField": "integer",
    "BigIntegerField": "integer",
    "SmallIntegerField": "integer",
    "PositiveIntegerField": "integer",
    "PositiveSmallIntegerField": "integer",
    "PositiveBigIntegerField": "integer",
    "FloatField": "number",
    "DecimalField": "decimal",
    "DateField": "date",
    "DateTimeField": "datetime",
    "TimeField": "time",
    "DurationField": "duration",
    "JSONField": "jsonb",
    "ArrayField": "array",
    "ForeignKey": "foreign_key",
    "OneToOneField": "one_to_one",
    "ManyToManyField": "many_to_many",
    "GenericForeignKey": "generic_foreign_key",
    "FileField": "string",
    "ImageField": "string",
}


def rel(path: Path) -> str:
    for base in (PROJECT_ROOT, REPO_DIR):
        try:
            return path.relative_to(base).as_posix()
        except ValueError:
            continue
    return path.as_posix()  # outside both trees; keep absolute


def is_excluded(path: Path) -> bool:
    return bool(set(path.relative_to(PROJECT_ROOT).parts) & EXCLUDED_PARTS)


def read_tree(path: Path) -> ast.Module:
    return ast.parse(path.read_text(), filename=str(path))


def unparse(node: ast.AST | None) -> str | None:
    if node is None:
        return None
    return ast.unparse(node)


def literal_value(node: ast.AST) -> Any:
    try:
        return ast.literal_eval(node)
    except (ValueError, SyntaxError):
        return unparse(node)


def call_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        parent = call_name(node.value)
        return f"{parent}.{node.attr}" if parent else node.attr
    if isinstance(node, ast.Subscript):
        return call_name(node.value)
    return unparse(node) or ""


def simple_name(raw: str | None) -> str:
    if not raw:
        return ""
    raw = raw.split("[", 1)[0]
    return raw.rsplit(".", 1)[-1]


def list_literal(node: ast.AST) -> list[Any] | None:
    value = literal_value(node)
    return value if isinstance(value, list) else None


def kwargs_for(call: ast.Call) -> dict[str, ast.AST]:
    return {kw.arg: kw.value for kw in call.keywords if kw.arg}


def jsonable_kwargs(call: ast.Call) -> dict[str, Any]:
    return {key: literal_value(value) for key, value in kwargs_for(call).items()}


def bool_kw(call: ast.Call, name: str, default: bool = False) -> bool:
    if name not in kwargs_for(call):
        return default
    value = literal_value(kwargs_for(call)[name])
    return value if isinstance(value, bool) else default


def default_shape(raw_default: Any) -> dict[str, Any] | None:
    if raw_default in {"dict", "{}", "builtins.dict"}:
        return {"type": "object"}
    if raw_default in {"list", "[]", "builtins.list"}:
        return {"type": "array"}
    if raw_default is None or raw_default == "None":
        return {"type": "unknown", "nullable": True}
    return None


def schema_from_annotation(node: ast.AST | None) -> dict[str, Any]:
    if node is None:
        return {"type": "unknown"}

    raw = unparse(node) or ""

    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.BitOr):
        left = schema_from_annotation(node.left)
        right = schema_from_annotation(node.right)
        if right.get("type") == "null":
            left["nullable"] = True
            left["raw"] = raw
            return left
        if left.get("type") == "null":
            right["nullable"] = True
            right["raw"] = raw
            return right
        return {"type": "union", "raw": raw, "any_of": [left, right]}

    if isinstance(node, ast.Constant) and node.value is None:
        return {"type": "null", "raw": raw}

    if isinstance(node, ast.Name):
        mapping = {
            "str": "string",
            "int": "integer",
            "float": "number",
            "bool": "boolean",
            "dict": "object",
            "list": "array",
            "datetime": "datetime",
            "date": "date",
            "time": "time",
            "UUID": "uuid",
            "UUID4": "uuid",
            "UUID5": "uuid",
            "Decimal": "decimal",
            "Any": "any",
        }
        if node.id in mapping:
            return {"type": mapping[node.id], "raw": raw}
        return {"type": "ref", "ref": node.id, "raw": raw}

    if isinstance(node, ast.Attribute):
        dotted = call_name(node)
        if dotted.endswith(".datetime"):
            return {"type": "datetime", "raw": raw}
        if dotted.endswith(".date"):
            return {"type": "date", "raw": raw}
        if dotted.endswith(".time"):
            return {"type": "time", "raw": raw}
        if dotted.endswith(".Decimal"):
            return {"type": "decimal", "raw": raw}
        if dotted.endswith((".UUID", ".UUID4", ".UUID5")):
            return {"type": "uuid", "raw": raw}
        return {"type": "ref", "ref": dotted, "raw": raw}

    if isinstance(node, ast.Subscript):
        base = call_name(node.value)
        slice_node = node.slice
        if base in {"list", "List"}:
            return {
                "type": "array",
                "items": schema_from_annotation(slice_node),
                "raw": raw,
            }
        if base in {"dict", "Dict"}:
            return {"type": "object", "raw": raw}
        if base in {"Literal", "typing.Literal"}:
            values: list[Any] = []
            if isinstance(slice_node, ast.Tuple):
                values = [literal_value(elt) for elt in slice_node.elts]
            else:
                values = [literal_value(slice_node)]
            return {"type": "literal", "enum": values, "raw": raw}
        if base in {"Union", "typing.Union"}:
            members = (
                list(slice_node.elts) if isinstance(slice_node, ast.Tuple) else [slice_node]
            )
            schemas = [schema_from_annotation(member) for member in members]
            nullable = any(schema.get("type") == "null" for schema in schemas)
            schemas = [schema for schema in schemas if schema.get("type") != "null"]
            if len(schemas) == 1:
                schemas[0]["nullable"] = nullable
                schemas[0]["raw"] = raw
                return schemas[0]
            return {"type": "union", "raw": raw, "nullable": nullable, "any_of": schemas}
        if base.endswith("ValueSetBoundCoding"):
            return {"type": "valueset_coding", "raw": raw}
        return {"type": "ref", "ref": base, "raw": raw}

    return {"type": "unknown", "raw": raw}


def parse_imports(tree: ast.Module) -> dict[str, str]:
    imports: dict[str, str] = {}
    for node in tree.body:
        if isinstance(node, ast.ImportFrom) and node.module:
            for alias in node.names:
                if alias.name == "*":
                    continue
                imports[alias.asname or alias.name] = f"{node.module}.{alias.name}"
        elif isinstance(node, ast.Import):
            for alias in node.names:
                imports[alias.asname or alias.name.split(".")[0]] = alias.name
    return imports


def collect_app_configs() -> list[dict[str, Any]]:
    configs: list[dict[str, Any]] = []
    for path in sorted(PROJECT_ROOT.glob("**/apps.py")):
        if is_excluded(path):
            continue
        tree = read_tree(path)
        constants: dict[str, Any] = {}
        for node in tree.body:
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        constants[target.id] = literal_value(node.value)

        for node in tree.body:
            if not isinstance(node, ast.ClassDef):
                continue
            bases = [simple_name(unparse(base)) for base in node.bases]
            if "AppConfig" not in bases:
                continue

            name = None
            label = None
            verbose_name = None
            for stmt in node.body:
                if isinstance(stmt, ast.Assign):
                    for target in stmt.targets:
                        if isinstance(target, ast.Name):
                            value = literal_value(stmt.value)
                            if isinstance(value, str) and value in constants:
                                value = constants[value]
                            if target.id == "name":
                                name = value
                            elif target.id == "label":
                                label = value
                            elif target.id == "verbose_name":
                                verbose_name = value

            if not isinstance(name, str):
                continue

            configs.append(
                {
                    "class_name": node.name,
                    "package": name,
                    "label": label or name.rsplit(".", 1)[-1],
                    "verbose_name": verbose_name,
                    "source_file": rel(path),
                    "source_dir": rel(path.parent),
                    "_source_path": path.parent,
                }
            )

    configs.sort(key=lambda item: len(item["source_dir"]), reverse=True)
    return configs


APP_CONFIGS = collect_app_configs()


def config_for_path(path: Path) -> dict[str, Any] | None:
    for config in APP_CONFIGS:
        try:
            path.relative_to(config["_source_path"])
        except ValueError:
            continue
        return config
    return None


def module_for_path(path: Path) -> str:
    config = config_for_path(path)
    if config:
        suffix = path.relative_to(config["_source_path"]).with_suffix("").parts
        parts = [config["package"], *[part for part in suffix if part != "__init__"]]
        return ".".join(parts)
    return ".".join(path.relative_to(PROJECT_ROOT).with_suffix("").parts)


def app_label_for_path(path: Path) -> str:
    config = config_for_path(path)
    if config:
        return config["label"]
    parts = path.relative_to(PROJECT_ROOT).parts
    if parts[0] == "care" and len(parts) > 1:
        return parts[1]
    return parts[0]


def iter_model_files() -> list[Path]:
    files: list[Path] = []
    for root_name in ("care", "app"):
        root = PROJECT_ROOT / root_name
        if not root.exists():
            continue
        for path in root.rglob("*.py"):
            if is_excluded(path):
                continue
            parts = path.relative_to(PROJECT_ROOT).parts
            if path.name == "models.py" or "models" in parts:
                files.append(path)
    return sorted(set(files))


def iter_spec_files() -> list[Path]:
    files: set[Path] = set()
    resources_root = PROJECT_ROOT / "care" / "emr" / "resources"
    if resources_root.exists():
        files.update(path for path in resources_root.rglob("*.py") if not is_excluded(path))

    app_root = PROJECT_ROOT / "app"
    if app_root.exists():
        for path in app_root.rglob("*.py"):
            if is_excluded(path):
                continue
            parts = path.relative_to(PROJECT_ROOT).parts
            if (
                path.name == "spec.py"
                or "specs" in parts
                or ("services" in parts and "types" in parts)
            ):
                files.add(path)

    return sorted(files)


def parse_meta(node: ast.ClassDef) -> dict[str, Any]:
    meta: dict[str, Any] = {}
    for stmt in node.body:
        if not isinstance(stmt, ast.ClassDef) or stmt.name != "Meta":
            continue
        meta["bases"] = [unparse(base) for base in stmt.bases]
        for item in stmt.body:
            if isinstance(item, ast.Assign):
                for target in item.targets:
                    if isinstance(target, ast.Name):
                        meta[target.id] = literal_value(item.value)
    return meta


def parse_json_schema_validators(node: ast.AST | None) -> list[dict[str, str]]:
    if node is None or not isinstance(node, (ast.List, ast.Tuple)):
        return []
    validators: list[dict[str, str]] = []
    for element in node.elts:
        if not isinstance(element, ast.Call):
            continue
        name = call_name(element.func)
        if not name.endswith("JSONFieldSchemaValidator") or not element.args:
            continue
        validators.append({"symbol": unparse(element.args[0]) or ""})
    return validators


def parse_field(
    name: str,
    value: ast.AST,
    *,
    source_class: str,
    source_file: str,
    line: int,
) -> dict[str, Any] | None:
    if not isinstance(value, ast.Call):
        return None
    raw_call_name = call_name(value.func)
    field_class = simple_name(raw_call_name)
    if field_class not in DJANGO_FIELD_CLASSES:
        return None

    kwargs = kwargs_for(value)
    info: dict[str, Any] = {
        "name": name,
        "django_field": field_class,
        "analytics_type": FIELD_TYPE_MAP.get(field_class, "unknown"),
        "source_class": source_class,
        "source_file": source_file,
        "line": line,
        "declared": True,
        "inherited": False,
        "db_column": literal_value(kwargs["db_column"]) if "db_column" in kwargs else name,
        "nullable": bool_kw(value, "null"),
        "blank": bool_kw(value, "blank"),
        "primary_key": bool_kw(value, "primary_key"),
        "unique": bool_kw(value, "unique"),
        "db_index": bool_kw(value, "db_index"),
        "raw": unparse(value),
    }

    if "default" in kwargs:
        info["default"] = literal_value(kwargs["default"])
    if "max_length" in kwargs:
        info["max_length"] = literal_value(kwargs["max_length"])
    if "help_text" in kwargs:
        info["help_text"] = literal_value(kwargs["help_text"])
    if "choices" in kwargs:
        info["choices"] = literal_value(kwargs["choices"])

    if field_class in RELATION_FIELD_CLASSES:
        info["relation"] = {
            "target_raw": literal_value(value.args[0]) if value.args else None,
            "on_delete": literal_value(kwargs["on_delete"]) if "on_delete" in kwargs else None,
            "related_name": literal_value(kwargs["related_name"]) if "related_name" in kwargs else None,
            "through": literal_value(kwargs["through"]) if "through" in kwargs else None,
            "to_field": literal_value(kwargs["to_field"]) if "to_field" in kwargs else None,
        }
        if field_class in {"ForeignKey", "OneToOneField"} and "db_column" not in kwargs:
            info["db_column"] = f"{name}_id"
        if field_class == "ManyToManyField":
            info["db_column"] = None

    if field_class == "GenericForeignKey":
        info["db_column"] = None
        info["virtual"] = True
        info["relation"] = {
            "content_type_field": literal_value(value.args[0]) if value.args else None,
            "object_id_field": literal_value(value.args[1]) if len(value.args) > 1 else None,
        }

    if field_class == "ArrayField":
        base_field = value.args[0] if value.args else None
        info["array_item_field"] = unparse(base_field)
        if isinstance(base_field, ast.Call):
            base_class = simple_name(call_name(base_field.func))
            info["array_item_django_field"] = base_class
            info["array_item_type"] = FIELD_TYPE_MAP.get(base_class, "unknown")

    if field_class == "JSONField":
        validators = parse_json_schema_validators(kwargs.get("validators"))
        if validators:
            info["json_schema_validators"] = validators
        info["default_shape"] = default_shape(info.get("default"))

    return info


def parse_model_classes(paths: list[Path]) -> tuple[dict[str, dict[str, Any]], dict[str, Any]]:
    classes: dict[str, dict[str, Any]] = {}
    json_schema_constants: dict[str, Any] = {}

    for path in paths:
        tree = read_tree(path)
        module = module_for_path(path)
        imports = parse_imports(tree)

        for node in tree.body:
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id.isupper():
                        value = literal_value(node.value)
                        if isinstance(value, (dict, list)):
                            json_schema_constants[f"{module}.{target.id}"] = {
                                "name": target.id,
                                "module": module,
                                "source_file": rel(path),
                                "line": node.lineno,
                                "schema": value,
                            }

            if not isinstance(node, ast.ClassDef):
                continue

            fqn = f"{module}.{node.name}"
            own_fields: list[dict[str, Any]] = []
            for stmt in node.body:
                if isinstance(stmt, ast.Assign):
                    for target in stmt.targets:
                        if isinstance(target, ast.Name):
                            field = parse_field(
                                target.id,
                                stmt.value,
                                source_class=fqn,
                                source_file=rel(path),
                                line=stmt.lineno,
                            )
                            if field:
                                own_fields.append(field)

            bases = [unparse(base) or "" for base in node.bases]
            classes[fqn] = {
                "class_name": node.name,
                "model": fqn,
                "module": module,
                "source_file": rel(path),
                "line": node.lineno,
                "app_label": app_label_for_path(path),
                "bases": bases,
                "base_names": [simple_name(base) for base in bases],
                "imports": imports,
                "own_fields": own_fields,
                "meta": parse_meta(node),
            }

    return classes, json_schema_constants


def parse_spec_field(stmt: ast.AnnAssign, source_class: str, source_file: str) -> dict[str, Any] | None:
    if not isinstance(stmt.target, ast.Name):
        return None

    field: dict[str, Any] = {
        "name": stmt.target.id,
        "annotation": unparse(stmt.annotation),
        "schema": schema_from_annotation(stmt.annotation),
        "source_class": source_class,
        "source_file": source_file,
        "line": stmt.lineno,
        "required": stmt.value is None,
    }

    if stmt.value is not None:
        field["default"] = literal_value(stmt.value)
        if isinstance(stmt.value, ast.Call) and simple_name(call_name(stmt.value.func)) == "Field":
            field["field_kwargs"] = jsonable_kwargs(stmt.value)
            if stmt.value.args and isinstance(stmt.value.args[0], ast.Constant):
                field["required"] = stmt.value.args[0].value is Ellipsis
            else:
                field["required"] = False

    return field


def parse_spec_classes(paths: list[Path]) -> dict[str, dict[str, Any]]:
    classes: dict[str, dict[str, Any]] = {}

    for path in paths:
        tree = read_tree(path)
        module = module_for_path(path)
        imports = parse_imports(tree)

        for node in tree.body:
            if not isinstance(node, ast.ClassDef):
                continue

            bases = [unparse(base) or "" for base in node.bases]
            base_names = [simple_name(base) for base in bases]
            fqn = f"{module}.{node.name}"
            fields: list[dict[str, Any]] = []
            model_expr = None
            excludes = None
            store_metadata = None

            for stmt in node.body:
                if isinstance(stmt, ast.AnnAssign):
                    field = parse_spec_field(stmt, fqn, rel(path))
                    if field:
                        fields.append(field)
                elif isinstance(stmt, ast.Assign):
                    for target in stmt.targets:
                        if not isinstance(target, ast.Name):
                            continue
                        if target.id == "__model__":
                            model_expr = unparse(stmt.value)
                        elif target.id == "__exclude__":
                            excludes = list_literal(stmt.value)
                        elif target.id == "__store_metadata__":
                            value = literal_value(stmt.value)
                            store_metadata = value if isinstance(value, bool) else None

            # ponytail: CARE spec classes all end in "Spec"; include subclasses so
            # inherited-only specs (e.g. PatientIdentifierListSpec) resolve.
            include = bool(
                fields
                or model_expr
                or set(base_names) & SPEC_BASE_NAMES
                or any(name.endswith("Spec") for name in base_names)
            )
            if not include:
                continue

            classes[fqn] = {
                "class_name": node.name,
                "spec": fqn,
                "module": module,
                "source_file": rel(path),
                "line": node.lineno,
                "bases": bases,
                "base_names": base_names,
                "imports": imports,
                "own_fields": fields,
                "model_expr": model_expr,
                "exclude": excludes,
                "store_metadata": store_metadata,
            }

    return classes


def build_name_index(classes: dict[str, dict[str, Any]]) -> dict[str, list[str]]:
    index: dict[str, list[str]] = defaultdict(list)
    for fqn, info in classes.items():
        index[info["class_name"]].append(fqn)
    return index


def resolve_class_name(
    class_name: str,
    current_module: str,
    index: dict[str, list[str]],
) -> str | None:
    candidates = index.get(class_name, [])
    if not candidates:
        return None
    same_module = [fqn for fqn in candidates if fqn.rsplit(".", 1)[0] == current_module]
    if len(same_module) == 1:
        return same_module[0]
    same_package = [
        fqn
        for fqn in candidates
        if current_module.startswith(fqn.rsplit(".", 2)[0])
        or fqn.startswith(current_module.rsplit(".", 1)[0])
    ]
    if len(same_package) == 1:
        return same_package[0]
    if len(candidates) == 1:
        return candidates[0]
    return None


def resolve_imported_model(
    expr: str | None,
    imports: dict[str, str],
    model_classes: dict[str, dict[str, Any]],
    model_name_index: dict[str, list[str]],
) -> str | None:
    if not expr:
        return None
    expr_name = expr.rsplit(".", 1)[-1]
    imported = imports.get(expr_name)
    if imported and imported in model_classes:
        return imported
    if imported:
        imported_module = imported.rsplit(".", 1)[0]
        matches = [
            fqn
            for fqn in model_name_index.get(expr_name, [])
            if fqn.rsplit(".", 1)[0] == imported_module
            or fqn.rsplit(".", 1)[0].startswith(f"{imported_module}.")
        ]
        if len(matches) == 1:
            return matches[0]
    matches = model_name_index.get(expr_name, [])
    return matches[0] if len(matches) == 1 else None


def is_model_class(
    fqn: str,
    model_classes: dict[str, dict[str, Any]],
    model_name_index: dict[str, list[str]],
    seen: set[str] | None = None,
) -> bool:
    seen = seen or set()
    if fqn in seen:
        return False
    seen.add(fqn)
    info = model_classes[fqn]
    if info["own_fields"]:
        return True
    if set(info["base_names"]) & MODEL_BASE_NAMES:
        return True
    for base in info["base_names"]:
        parent = resolve_class_name(base, info["module"], model_name_index)
        if parent and is_model_class(parent, model_classes, model_name_index, seen):
            return True
    return False


def collect_model_fields(
    fqn: str,
    model_classes: dict[str, dict[str, Any]],
    model_name_index: dict[str, list[str]],
    seen: set[str] | None = None,
) -> list[dict[str, Any]]:
    seen = seen or set()
    if fqn in seen:
        return []
    seen.add(fqn)
    info = model_classes[fqn]
    fields: OrderedDict[str, dict[str, Any]] = OrderedDict()

    for base in info["base_names"]:
        parent = resolve_class_name(base, info["module"], model_name_index)
        if not parent:
            continue
        for field in collect_model_fields(parent, model_classes, model_name_index, seen):
            inherited = dict(field)
            inherited["inherited"] = True
            inherited["declared"] = False
            inherited.setdefault("inherited_from", field.get("source_class", parent))
            fields[inherited["name"]] = inherited

    for field in info["own_fields"]:
        own = dict(field)
        own["inherited"] = False
        own["declared"] = True
        fields[own["name"]] = own

    return list(fields.values())


def collect_spec_fields(
    fqn: str,
    spec_classes: dict[str, dict[str, Any]],
    spec_name_index: dict[str, list[str]],
    seen: set[str] | None = None,
) -> list[dict[str, Any]]:
    seen = seen or set()
    if fqn in seen:
        return []
    seen.add(fqn)
    info = spec_classes[fqn]
    fields: OrderedDict[str, dict[str, Any]] = OrderedDict()

    for base in info["base_names"]:
        parent = resolve_class_name(base, info["module"], spec_name_index)
        if not parent:
            continue
        for field in collect_spec_fields(parent, spec_classes, spec_name_index, seen):
            inherited = dict(field)
            inherited["inherited"] = True
            inherited.setdefault("inherited_from", field.get("source_class", parent))
            fields[inherited["name"]] = inherited

    for field in info["own_fields"]:
        own = dict(field)
        own["inherited"] = False
        fields[own["name"]] = own

    return list(fields.values())


def resolve_spec_model(
    fqn: str,
    spec_classes: dict[str, dict[str, Any]],
    spec_name_index: dict[str, list[str]],
    model_classes: dict[str, dict[str, Any]],
    model_name_index: dict[str, list[str]],
    seen: set[str] | None = None,
) -> str | None:
    seen = seen or set()
    if fqn in seen:
        return None
    seen.add(fqn)
    info = spec_classes[fqn]
    own = resolve_imported_model(info["model_expr"], info["imports"], model_classes, model_name_index)
    if own:
        return own
    for base in info["base_names"]:
        parent = resolve_class_name(base, info["module"], spec_name_index)
        if parent:
            resolved = resolve_spec_model(
                parent,
                spec_classes,
                spec_name_index,
                model_classes,
                model_name_index,
                seen,
            )
            if resolved:
                return resolved
    return None


def resolve_spec_exclude(
    fqn: str,
    spec_classes: dict[str, dict[str, Any]],
    spec_name_index: dict[str, list[str]],
    seen: set[str] | None = None,
) -> list[str]:
    seen = seen or set()
    if fqn in seen:
        return []
    seen.add(fqn)
    info = spec_classes[fqn]
    if isinstance(info["exclude"], list):
        return info["exclude"]
    for base in info["base_names"]:
        parent = resolve_class_name(base, info["module"], spec_name_index)
        if parent:
            inherited = resolve_spec_exclude(parent, spec_classes, spec_name_index, seen)
            if inherited:
                return inherited
    return []


def resolve_store_metadata(
    fqn: str,
    spec_classes: dict[str, dict[str, Any]],
    spec_name_index: dict[str, list[str]],
    seen: set[str] | None = None,
) -> bool:
    seen = seen or set()
    if fqn in seen:
        return False
    seen.add(fqn)
    info = spec_classes[fqn]
    if isinstance(info["store_metadata"], bool):
        return info["store_metadata"]
    for base in info["base_names"]:
        parent = resolve_class_name(base, info["module"], spec_name_index)
        if parent and resolve_store_metadata(parent, spec_classes, spec_name_index, seen):
            return True
    return False


def resolve_relation_target(
    raw: Any,
    current_model: dict[str, Any],
    field_imports: dict[str, str],
    models: list[dict[str, Any]],
) -> str | None:
    if not raw:
        return None
    if raw == "self":
        return current_model["model"]
    raw_text = str(raw)
    if raw_text in field_imports:
        raw_text = field_imports[raw_text]
    class_name = raw_text.rsplit(".", 1)[-1]
    if "." in raw_text and not raw_text.startswith("care.") and raw_text.count(".") == 1:
        app_label, model_name = raw_text.split(".", 1)
        matches = [
            model["model"]
            for model in models
            if model["app_label"] == app_label and model["class_name"] == model_name
        ]
        return matches[0] if len(matches) == 1 else None
    matches = [
        model["model"]
        for model in models
        if model["class_name"] == class_name
        or model["model"] == raw_text
        or model["model"].endswith(f".{class_name}")
    ]
    return matches[0] if len(matches) == 1 else None


def table_name(model: dict[str, Any]) -> str | None:
    if model["abstract"] or model["proxy"]:
        return None
    meta = model["meta"]
    if isinstance(meta.get("db_table"), str):
        return meta["db_table"]
    return f"{model['app_label']}_{model['class_name'].lower()}"


def schema_constant_for_symbol(
    symbol: str,
    imports: dict[str, str],
    constants: dict[str, Any],
) -> dict[str, Any] | None:
    imported = imports.get(symbol, symbol)
    if imported in constants:
        return constants[imported]
    matches = [value for key, value in constants.items() if key.endswith(f".{symbol}")]
    return matches[0] if len(matches) == 1 else None


def enrich_json_validators(
    field: dict[str, Any],
    model_info: dict[str, Any],
    json_schema_constants: dict[str, Any],
) -> None:
    validators = field.get("json_schema_validators")
    if not validators:
        return
    imports = model_info["imports"]
    for validator in validators:
        symbol = validator["symbol"].split(".", 1)[0]
        constant = schema_constant_for_symbol(symbol, imports, json_schema_constants)
        if constant:
            validator["schema_source"] = constant["source_file"]
            validator["schema"] = constant["schema"]


def build_models_catalog(
    model_classes: dict[str, dict[str, Any]],
    model_name_index: dict[str, list[str]],
    json_schema_constants: dict[str, Any],
) -> list[dict[str, Any]]:
    models: list[dict[str, Any]] = []
    for fqn in sorted(model_classes):
        info = model_classes[fqn]
        if not is_model_class(fqn, model_classes, model_name_index):
            continue

        fields = collect_model_fields(fqn, model_classes, model_name_index)
        abstract = info["meta"].get("abstract") is True
        proxy = info["meta"].get("proxy") is True
        physical_table = not abstract and not proxy

        if physical_table and not any(field["primary_key"] for field in fields):
            fields = [
                {
                    "name": "id",
                    "django_field": "AutoField",
                    "analytics_type": "integer",
                    "source_class": "django.db.models.Model",
                    "source_file": None,
                    "line": None,
                    "declared": False,
                    "inherited": True,
                    "implicit": True,
                    "db_column": "id",
                    "nullable": False,
                    "blank": False,
                    "primary_key": True,
                    "unique": True,
                    "db_index": True,
                },
                *fields,
            ]

        model = {
            "class_name": info["class_name"],
            "model": fqn,
            "module": info["module"],
            "source_file": info["source_file"],
            "line": info["line"],
            "app_label": info["app_label"],
            "bases": info["bases"],
            "abstract": abstract,
            "proxy": proxy,
            "physical_table": physical_table,
            "db_table": None,
            "meta": {key: value for key, value in info["meta"].items() if key != "bases"},
            "fields": fields,
        }
        model["db_table"] = table_name(model)
        models.append(model)

    for model in models:
        class_info = model_classes[model["model"]]
        for field in model["fields"]:
            if field.get("django_field") == "JSONField":
                enrich_json_validators(field, class_info, json_schema_constants)
            relation = field.get("relation")
            if relation and relation.get("target_raw"):
                target = resolve_relation_target(
                    relation["target_raw"], model, class_info["imports"], models
                )
                if target:
                    relation["target_model"] = target

    return sorted(models, key=lambda item: (item["app_label"], item["class_name"]))


def build_specs_catalog(
    spec_classes: dict[str, dict[str, Any]],
    spec_name_index: dict[str, list[str]],
    model_classes: dict[str, dict[str, Any]],
    model_name_index: dict[str, list[str]],
) -> list[dict[str, Any]]:
    specs: list[dict[str, Any]] = []
    for fqn in sorted(spec_classes):
        info = spec_classes[fqn]
        fields = collect_spec_fields(fqn, spec_classes, spec_name_index)
        model_fqn = resolve_spec_model(
            fqn, spec_classes, spec_name_index, model_classes, model_name_index
        )
        specs.append(
            {
                "class_name": info["class_name"],
                "spec": fqn,
                "module": info["module"],
                "source_file": info["source_file"],
                "line": info["line"],
                "bases": info["bases"],
                "imports": info["imports"],
                "model": model_fqn,
                "exclude": resolve_spec_exclude(fqn, spec_classes, spec_name_index),
                "store_metadata": resolve_store_metadata(fqn, spec_classes, spec_name_index),
                "fields": fields,
            }
        )
    return sorted(specs, key=lambda item: item["spec"])


def build_jsonb_catalog(models: list[dict[str, Any]], specs: list[dict[str, Any]]) -> list[dict[str, Any]]:
    specs_by_model: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for spec in specs:
        if spec["model"]:
            specs_by_model[spec["model"]].append(spec)

    json_fields: list[dict[str, Any]] = []
    for model in models:
        if not model["physical_table"]:
            continue
        db_fields = {field["name"] for field in model["fields"] if field.get("db_column")}
        model_specs = specs_by_model.get(model["model"], [])
        metadata_fields_by_name: OrderedDict[str, dict[str, Any]] = OrderedDict()
        for spec in model_specs:
            if not spec["store_metadata"]:
                continue
            excluded = set(spec["exclude"])
            for spec_field in spec["fields"]:
                if spec_field["name"] not in db_fields and spec_field["name"] not in excluded:
                    metadata_field = metadata_fields_by_name.setdefault(
                        spec_field["name"],
                        {
                            "spec": spec["spec"],
                            "source_specs": [],
                            "name": spec_field["name"],
                            "annotation": spec_field.get("annotation"),
                            "schema": spec_field.get("schema"),
                        },
                    )
                    if spec["spec"] not in metadata_field["source_specs"]:
                        metadata_field["source_specs"].append(spec["spec"])

        metadata_fields = list(metadata_fields_by_name.values())

        for field in model["fields"]:
            if field.get("django_field") != "JSONField":
                continue
            matched_specs: list[dict[str, Any]] = []
            for spec in model_specs:
                excluded = set(spec["exclude"])
                for spec_field in spec["fields"]:
                    if spec_field["name"] != field["name"]:
                        continue
                    matched_specs.append(
                        {
                            "spec": spec["spec"],
                            "source_file": spec["source_file"],
                            "annotation": spec_field.get("annotation"),
                            "schema": spec_field.get("schema"),
                            "required": spec_field.get("required"),
                            "excluded_by_spec": spec_field["name"] in excluded,
                        }
                    )

            schema_status = "unknown"
            if matched_specs:
                schema_status = "from_pydantic_spec"
            elif field.get("json_schema_validators"):
                schema_status = "from_json_schema_validator"
            elif field.get("default_shape"):
                schema_status = "default_shape_only"

            json_fields.append(
                {
                    "model": model["model"],
                    "class_name": model["class_name"],
                    "app_label": model["app_label"],
                    "db_table": model["db_table"],
                    "field": field["name"],
                    "db_column": field["db_column"],
                    "source_file": field["source_file"],
                    "line": field["line"],
                    "nullable": field["nullable"],
                    "blank": field["blank"],
                    "default": field.get("default"),
                    "default_shape": field.get("default_shape"),
                    "schema_status": schema_status,
                    "pydantic_spec_matches": matched_specs,
                    "json_schema_validators": field.get("json_schema_validators", []),
                    "meta_stored_fields": metadata_fields if field["name"] == "meta" else [],
                }
            )

    return sorted(
        json_fields,
        key=lambda item: (item["app_label"], item["class_name"], item["field"]),
    )


def walk_schema_refs(schema: Any) -> set[str]:
    refs: set[str] = set()
    if isinstance(schema, dict):
        if schema.get("type") == "ref" and schema.get("ref"):
            refs.add(str(schema["ref"]))
        if schema.get("type") == "valueset_coding":
            refs.add("Coding")  # ValueSetBoundCoding stores a plain Coding
        for value in schema.values():
            refs.update(walk_schema_refs(value))
    elif isinstance(schema, list):
        for item in schema:
            refs.update(walk_schema_refs(item))
    return refs


def resolve_schema_ref(
    ref: str,
    source_spec: dict[str, Any],
    spec_name_index: dict[str, list[str]],
) -> str | None:
    ref_name = simple_name(ref)
    # ponytail: import map disambiguates; no-import ambiguity stays unresolved, not guessed
    imported = source_spec.get("imports", {}).get(ref_name)
    if imported:
        return imported
    return resolve_class_name(ref_name, source_spec["module"], spec_name_index)


def collect_embedded_definitions(
    root_schemas: list[tuple[dict[str, Any], str]],
    specs_by_fqn: dict[str, dict[str, Any]],
    spec_name_index: dict[str, list[str]],
    enum_index: dict[str, list[dict[str, Any]]],
) -> tuple[list[dict[str, Any]], list[str]]:
    definitions: OrderedDict[str, dict[str, Any]] = OrderedDict()
    unresolved_refs: set[str] = set()
    queue = list(root_schemas)

    while queue:
        schema, source_spec_fqn = queue.pop(0)
        source_spec = specs_by_fqn.get(source_spec_fqn)
        if not source_spec:
            continue
        for ref in sorted(walk_schema_refs(schema)):
            target_fqn = resolve_schema_ref(ref, source_spec, spec_name_index)
            # Membership guard: resolve_schema_ref may hand back an import/ambiguity
            # FQN that was filtered out of specs_by_fqn — fall through to enums.
            target_spec = specs_by_fqn.get(target_fqn) if target_fqn else None
            if target_spec is not None:
                if target_fqn in definitions:
                    continue
                definition = {
                    "name": target_spec["class_name"],
                    "spec": target_spec["spec"],
                    "source_file": target_spec["source_file"],
                    "fields": [
                        {
                            "name": field["name"],
                            "annotation": field.get("annotation"),
                            "schema": field.get("schema"),
                            "required": field.get("required"),
                        }
                        for field in target_spec["fields"]
                    ],
                }
                definitions[target_fqn] = definition
                for field in target_spec["fields"]:
                    queue.append((field.get("schema", {}), target_fqn))
                continue
            # Spec miss → try the enum catalog. Names are NOT unique across files;
            # prefer the enum in the same file, then same dir, then a stable pick.
            candidates = enum_index.get(simple_name(ref), [])
            if candidates:
                spec_file = source_spec["source_file"]
                spec_dir = spec_file.rsplit("/", 1)[0]
                enum = (
                    next((e for e in candidates if e["source_file"] == spec_file), None)
                    or next((e for e in candidates if e["source_file"].startswith(spec_dir)), None)
                    or sorted(candidates, key=lambda e: (e["source_file"], e["line"]))[0]
                )
                # Synthetic key: never collides with a spec FQN, keeps distinct
                # same-named enums (StatusChoices etc.) from collapsing.
                key = f"enum::{enum['source_file']}::{enum['class_name']}"
                definitions.setdefault(
                    key,
                    {
                        "name": enum["class_name"],
                        "key": key,
                        "kind": "enum",
                        "values": enum["values"],
                    },
                )
                continue
            unresolved_refs.add(ref)

    return list(definitions.values()), sorted(unresolved_refs)


def build_column_jsonb_schema(
    jsonb_field: dict[str, Any],
    specs_by_fqn: dict[str, dict[str, Any]],
    spec_name_index: dict[str, list[str]],
    enum_index: dict[str, list[dict[str, Any]]],
) -> dict[str, Any]:
    root_schemas: list[tuple[dict[str, Any], str]] = []
    candidate_schemas = []

    for match in jsonb_field["pydantic_spec_matches"]:
        schema = match.get("schema", {})
        candidate_schemas.append(
            {
                "source": "pydantic_spec",
                "spec": match["spec"],
                "source_file": match["source_file"],
                "annotation": match.get("annotation"),
                "required": match.get("required"),
                "excluded_by_spec": match.get("excluded_by_spec"),
                "schema": schema,
            }
        )
        root_schemas.append((schema, match["spec"]))

    for meta_field in jsonb_field["meta_stored_fields"]:
        schema = meta_field.get("schema", {})
        for source_spec in meta_field.get("source_specs", []):
            root_schemas.append((schema, source_spec))

    definitions, unresolved_refs = collect_embedded_definitions(
        root_schemas, specs_by_fqn, spec_name_index, enum_index
    )

    schema = {
        "status": jsonb_field["schema_status"],
        "default_shape": jsonb_field.get("default_shape"),
        "candidate_schemas": candidate_schemas,
        "json_schema_validators": jsonb_field.get("json_schema_validators", []),
        "meta_stored_fields": jsonb_field.get("meta_stored_fields", []),
    }
    if definitions:
        schema["definitions"] = definitions
    if unresolved_refs:
        schema["unresolved_refs"] = unresolved_refs
    if jsonb_field["schema_status"] == "default_shape_only":
        schema["inferred_schema"] = jsonb_field.get("default_shape")
    return schema


def build_physical_table_catalog(
    models: list[dict[str, Any]],
    specs: list[dict[str, Any]],
    spec_name_index: dict[str, list[str]],
    jsonb_fields: list[dict[str, Any]],
    enum_index: dict[str, list[dict[str, Any]]],
) -> list[dict[str, Any]]:
    specs_by_fqn = {spec["spec"]: spec for spec in specs}
    jsonb_by_model_field = {
        (field["model"], field["field"]): field for field in jsonb_fields
    }
    tables: list[dict[str, Any]] = []

    for model in models:
        if not model["physical_table"]:
            continue
        columns = []
        for field in model["fields"]:
            column = dict(field)
            if column.get("choices") is not None:
                choice_values = resolve_choice_values(column, enum_index)
                if choice_values is not None:
                    column["choice_values"] = choice_values
            if field.get("django_field") == "JSONField":
                jsonb_field = jsonb_by_model_field.get((model["model"], field["name"]))
                if jsonb_field:
                    column["jsonb_schema"] = build_column_jsonb_schema(
                        jsonb_field, specs_by_fqn, spec_name_index, enum_index
                    )
            columns.append(column)

        table = {
            "class_name": model["class_name"],
            "model": model["model"],
            "module": model["module"],
            "source_file": model["source_file"],
            "line": model["line"],
            "app_label": model["app_label"],
            "db_table": model["db_table"],
            "bases": model["bases"],
            "meta": model["meta"],
            "column_count": len(columns),
            "jsonb_column_count": sum(
                1 for column in columns if column.get("django_field") == "JSONField"
            ),
            "columns": columns,
        }
        tables.append(table)

    return sorted(tables, key=lambda item: (item["app_label"], item["db_table"]))


# ---------------------------------------------------------------------------
# Enum / choices extraction. Resolves `choices=Status.choices` symbols to the
# literal stored values, and catalogs every enum-ish class for _enums.md
# (EMR columns often carry no choices= at all — their enum lives only in the
# Pydantic spec layer, e.g. care/emr/resources/encounter/constants.py).
# ---------------------------------------------------------------------------

ENUM_BASE_NAMES = {"TextChoices", "IntegerChoices", "Choices", "Enum", "IntEnum", "StrEnum"}


def parse_enum_classes(paths: list[Path]) -> list[dict[str, Any]]:
    enums: list[dict[str, Any]] = []
    seen: set[tuple[str, int]] = set()
    for path in sorted(set(paths)):
        try:
            tree = read_tree(path)
        except SyntaxError:
            continue
        source_file = rel(path)
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                base_names = {simple_name(unparse(base)) for base in node.bases}
                if not base_names & ENUM_BASE_NAMES:
                    continue
                values: list[Any] = []
                for stmt in node.body:
                    if not (
                        isinstance(stmt, ast.Assign)
                        and len(stmt.targets) == 1
                        and isinstance(stmt.targets[0], ast.Name)
                        and not stmt.targets[0].id.startswith("_")
                    ):
                        continue
                    value_node = stmt.value
                    if isinstance(value_node, ast.Constant):
                        values.append(value_node.value)
                    elif (
                        isinstance(value_node, (ast.Tuple, ast.List))
                        and value_node.elts
                        and isinstance(value_node.elts[0], ast.Constant)
                    ):
                        values.append(value_node.elts[0].value)
                if values and (source_file, node.lineno) not in seen:
                    seen.add((source_file, node.lineno))
                    enums.append(
                        {
                            "class_name": node.name,
                            "source_file": source_file,
                            "line": node.lineno,
                            "values": values,
                        }
                    )
            elif isinstance(node, ast.Assign):
                # Module-level UPPER_CASE choice constants: ((value, label), ...)
                for target in node.targets:
                    if not (isinstance(target, ast.Name) and target.id.isupper()):
                        continue
                    value = literal_value(node.value)
                    if not (
                        isinstance(value, (list, tuple))
                        and value
                        and all(
                            isinstance(item, (list, tuple)) and len(item) == 2
                            for item in value
                        )
                    ):
                        continue
                    if (source_file, node.lineno) in seen:
                        continue
                    seen.add((source_file, node.lineno))
                    enums.append(
                        {
                            "class_name": target.id,
                            "source_file": source_file,
                            "line": node.lineno,
                            "values": [item[0] for item in value],
                        }
                    )
    return sorted(enums, key=lambda item: (item["source_file"], item["line"]))


def resolve_choice_values(
    column: dict[str, Any], enum_index: dict[str, list[dict[str, Any]]]
) -> list[Any] | None:
    raw = column.get("choices")
    if isinstance(raw, (list, tuple)) and raw:
        return [
            item[0] if isinstance(item, (list, tuple)) and item else item
            for item in raw
        ]
    if not isinstance(raw, str):
        return None
    symbol = raw.removesuffix(".choices")
    symbol = simple_name(symbol)
    candidates = enum_index.get(symbol, [])
    if not candidates:
        return None
    same_file = [e for e in candidates if e["source_file"] == column.get("source_file")]
    if same_file:
        return same_file[0]["values"]
    if len(candidates) == 1:
        return candidates[0]["values"]
    return None  # ambiguous across files — agent falls back to _enums.md


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


def write_readme(tables: list[dict[str, Any]], specs: list[dict[str, Any]], jsonb_fields: list[dict[str, Any]]) -> None:
    with_spec = sum(1 for field in jsonb_fields if field["schema_status"] == "from_pydantic_spec")
    with_validator = sum(1 for field in jsonb_fields if field["schema_status"] == "from_json_schema_validator")
    default_only = sum(1 for field in jsonb_fields if field["schema_status"] == "default_shape_only")

    content = f"""# AI Analytics Schema

Generated from the Care source tree. These files are static catalogs for AI-assisted analytics, SQL generation, and warehouse planning.

## Files

- `{OUTPUT_FILE}` (at the output root, not in this directory): full machine-readable catalog (large — AI agents should NOT read this directly).
- `_index.md`: one line per table with FK edges. **Agents start here.**
- `_conventions.md`: SQL rules (soft delete, id vs external_id, JSONB access).
- `_base_models.md`: inherited base-class columns, defined once.
- `_enums.md`: every enum/choices class with stored values, grouped by source file.
- `tables/<db_table>.md`: declared columns and relations for one table.
- `jsonb/<db_table>.md`: JSONB column shapes for one table.

## Current Coverage

- Physical tables: {len(tables)}
- Pydantic/spec classes read for JSONB inference: {len(specs)}
- JSONB columns: {len(jsonb_fields)}
- JSONB columns with Pydantic spec matches: {with_spec}
- JSONB columns with JSON schema validators: {with_validator}
- JSONB columns with only default-shape hints: {default_only}

## Analytics Notes

- Django `JSONField` is treated as PostgreSQL JSONB for analytics purposes.
- `BaseModel` descendants use `deleted` for soft deletion; analytics queries should normally filter `deleted = false`.
- `external_id` is the public UUID. The implicit `id` column is the internal integer primary key unless the model declares otherwise.
- `EMRBaseModel` descendants inherit `history`, `meta`, `created_by_id`, and `updated_by_id`.
- Only physical tables are emitted. Abstract bases and standalone spec classes are used internally and are not separate schema outputs.
- JSONB columns include `jsonb_schema`; Pydantic spec matches, JSON schema validators, default-shape hints, and referenced definitions are embedded there.
- Pydantic specs are API/resource schemas. A same-name spec field is strong evidence for JSONB shape, but custom serializers/deserializers can still change behavior.
- Fields listed under `jsonb_schema.meta_stored_fields` are stored in `meta` only for resources that set `__store_metadata__ = True`.
- Plugin models under `app/` are included as source inventory; this does not prove a plug is enabled in a runtime deployment.

## Regenerate

From the care repo root: `pipenv run python scripts/generate_ai_analytics_schema.py`
(set `AI_SCHEMA_OUTPUT_DIR` to redirect output). From the care_analytics_skill
repo: `scripts/build.sh` (supports `ADDITIONAL_PLUGS`).
"""
    SCHEMA_DIR.mkdir(parents=True, exist_ok=True)
    (SCHEMA_DIR / "README.md").write_text(content)


# ---------------------------------------------------------------------------
# Sharded markdown output for AI agents (progressive disclosure).
# Agents load _index.md + _conventions.md (~15KB) and drill into per-table
# shards instead of the 2.5MB physical-tables.json.
# ---------------------------------------------------------------------------

CONVENTIONS_MD = """# CARE Analytics SQL Conventions

Target: PostgreSQL 16. Django `JSONField` columns are JSONB.

## Core rules

- Soft delete: `BaseModel` descendants have `deleted`; always filter `deleted = false` unless auditing deletions.
- IDs: `id` is the internal integer PK used by FK joins. `external_id` is the public UUID — expose this in results, never `id`.
- FKs are stored as `<name>_id` integer columns. Join `child.<name>_id = parent.id` unless the shard shows a `to_field`.
- Timestamps: `created_date` / `modified_date` (auto-managed, nullable, indexed).
- `EMRBaseModel` descendants add `history`, `meta` (JSONB), `created_by_id`, `updated_by_id` -> `users_user`.

## JSONB

- Shapes are documented in `jsonb/<db_table>.md`, distilled from Pydantic API specs — strong hints, not guarantees; custom serializers can change the stored shape. Named object types are expanded once per file under `## definitions`.
- Access patterns: `col->>'field'` (text), `col->'nested'` (jsonb), `jsonb_array_elements(col)` for arrays.
- Fields on a `stores (when __store_metadata__)` line live in the `meta` column only for resources that enable it.

## Enum values

- Resolved choices appear inline in table shards as `choices=[a|b|c]` — these are the stored values, use them directly.
- Unresolved symbols (`choices=Status.choices (see _enums.md)`) and columns with no `choices=` at all (common on EMR status/category columns, validated at the API layer): look up `_enums.md` by class name, preferring the definition whose file matches the column's model or resource module. Never guess enum values.

## Caveats

- Plugin tables (sources under `app/`) exist in the catalog but may not be enabled in a given deployment.
- The catalog is source-derived, not introspected from a live database; verify unusual constructs against migrations if in doubt.
"""


def is_declared_column(col: dict[str, Any]) -> bool:
    return not col.get("inherited") and not col.get("implicit")


def format_column_type(col: dict[str, Any]) -> str:
    ctype = col.get("analytics_type") or col.get("django_field") or "?"
    if col.get("max_length"):
        ctype += f"({col['max_length']})"
    if ctype.startswith("array") and col.get("array_item_type"):
        ctype += f"<{col['array_item_type']}>"
    return ctype


def format_column_line(col: dict[str, Any], model_to_table: dict[str, str]) -> str:
    parts = [f"`{col['name']}`", format_column_type(col)]
    relation = col.get("relation") or {}
    if relation:
        target_model = relation.get("target_model") or ""
        target = model_to_table.get(
            target_model, target_model or relation.get("target_raw") or "?"
        )
        ref = f"-> {target}"
        if relation.get("to_field"):
            ref += f".{relation['to_field']}"
        if relation.get("through"):
            ref += f" (through {relation['through']})"
        parts.append(ref)
    db_column = col.get("db_column")
    if db_column and db_column != col["name"]:
        parts.append(f"[col: {db_column}]")
    if col.get("primary_key"):
        parts.append("PK")
    if col.get("nullable"):
        parts.append("NULL")
    if col.get("unique") and not col.get("primary_key"):
        parts.append("UNIQUE")
    elif col.get("db_index") and not col.get("primary_key"):
        parts.append("idx")
    if col.get("choice_values"):
        values = col["choice_values"]
        shown = "|".join(str(v) for v in values[:20])
        if len(values) > 20:
            shown += f"|+{len(values) - 20} more"
        parts.append(f"choices=[{shown}]")
    elif col.get("choices"):
        parts.append(f"choices={str(col['choices'])[:120]} (see _enums.md)")
    default = col.get("default")
    if default not in (None, ""):
        parts.append(f"default={str(default)[:60]}")
    return "- " + " ".join(str(part) for part in parts)


def write_index_shard(tables: list[dict[str, Any]], model_to_table: dict[str, str]) -> None:
    lines = [
        "# CARE Physical Table Index",
        "",
        "One line per table. Details: `tables/<db_table>.md`. "
        "JSONB shapes: `jsonb/<db_table>.md`. "
        "Inherited columns: `_base_models.md`. Enum values: `_enums.md`. "
        "SQL rules: `_conventions.md`.",
        "",
    ]
    by_app: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for table in tables:
        by_app[table["app_label"]].append(table)
    for app in sorted(by_app):
        lines.append(f"## {app}")
        lines.append("")
        for table in by_app[app]:
            declared = [c for c in table["columns"] if is_declared_column(c)]
            fks = sorted(
                {
                    model_to_table.get(
                        (c["relation"].get("target_model") or ""),
                        c["relation"].get("target_raw") or "?",
                    )
                    for c in declared
                    if c.get("relation")
                }
            )
            entry = (
                f"- `{table['db_table']}` ({table['class_name']}) "
                f"{len(declared)} declared cols"
            )
            if table["jsonb_column_count"]:
                entry += f", {table['jsonb_column_count']} jsonb"
            if fks:
                entry += " | FK: " + ", ".join(fks)
            lines.append(entry)
        lines.append("")
    (SCHEMA_DIR / "_index.md").write_text("\n".join(lines))


def write_base_models_shard(
    tables: list[dict[str, Any]], model_to_table: dict[str, str]
) -> None:
    groups: OrderedDict[str, OrderedDict[str, dict[str, Any]]] = OrderedDict()
    for table in tables:
        for col in table["columns"]:
            if is_declared_column(col):
                continue
            source = col.get("inherited_from") or col.get("source_class") or "unknown"
            groups.setdefault(source, OrderedDict()).setdefault(col["name"], col)
    lines = [
        "# Inherited Base Columns",
        "",
        "Every table's `bases:` line names its ancestry; those columns are defined "
        "once here instead of repeated per table. JSONB shapes for inherited columns "
        "(`meta`, `history`) are table-specific — see `jsonb/<db_table>.md`.",
        "",
    ]
    for source, cols in groups.items():
        lines.append(f"## {source}")
        lines.append("")
        lines.extend(format_column_line(col, model_to_table) for col in cols.values())
        lines.append("")
    (SCHEMA_DIR / "_base_models.md").write_text("\n".join(lines))


def write_table_shards(
    tables: list[dict[str, Any]], model_to_table: dict[str, str]
) -> None:
    for table in tables:
        declared = [c for c in table["columns"] if is_declared_column(c)]
        lines = [
            f"# {table['db_table']} ({table['class_name']})",
            "",
            f"app: {table['app_label']} | source: {table['source_file']}",
        ]
        if table["bases"]:
            lines.append(
                f"bases: {', '.join(table['bases'])} "
                "(inherited columns: `_base_models.md`)"
            )
        lines.extend(["", "## Columns", ""])
        lines.extend(format_column_line(col, model_to_table) for col in declared)
        jsonb_cols = [c for c in table["columns"] if "jsonb_schema" in c]
        if jsonb_cols:
            names = ", ".join(f"`{c['name']}`" for c in jsonb_cols)
            lines.extend(["", f"JSONB shapes ({names}): `jsonb/{table['db_table']}.md`"])
        if table.get("meta"):
            lines.extend(
                ["", "## Model meta", "", "```json",
                 json.dumps(table["meta"], indent=1, sort_keys=True), "```"]
            )
        (SCHEMA_DIR / "tables" / f"{table['db_table']}.md").write_text(
            "\n".join(lines) + "\n"
        )


SIMPLE_TYPE_NAMES = {
    "string": "str",
    "integer": "int",
    "number": "float",
    "boolean": "bool",
    "object": "dict",
    "datetime": "datetime",
    "date": "date",
    "time": "time",
    "decimal": "decimal",
    "uuid": "uuid",
    "any": "any",
    "null": "null",
    "unknown": "?",
}


def type_str(schema: dict[str, Any] | None) -> str:
    """Render a parsed annotation schema as a compact type expression."""
    if not schema:
        return "?"
    kind = schema.get("type")
    if kind == "array":
        out = f"list[{type_str(schema.get('items'))}]"
    elif kind == "literal":
        out = " | ".join(repr(v) for v in schema.get("enum", []))
    elif kind == "union":
        out = " | ".join(type_str(m) for m in schema.get("any_of", []))
    elif kind == "ref":
        out = simple_name(str(schema.get("ref") or "?"))
    elif kind == "valueset_coding":
        out = "Coding"
    else:
        out = SIMPLE_TYPE_NAMES.get(kind, schema.get("raw") or "?")
    if schema.get("nullable"):
        out += "?"
    return out


def fields_str(defn: dict[str, Any]) -> str:
    inner = ", ".join(
        f"{field['name']}: {type_str(field.get('schema'))}"
        for field in defn.get("fields", [])
    )
    return "{" + inner + "}"


def spec_names_str(spec_fqns: list[str], limit: int = 4) -> str:
    names = [simple_name(fqn) for fqn in spec_fqns]
    if len(names) > limit:
        return ", ".join(names[:limit]) + f" +{len(names) - limit}"
    return ", ".join(names)


def render_jsonb_column(name: str, js: dict[str, Any]) -> list[str]:
    """One compact block per column: distinct shapes, validators, meta fields."""
    lines = [f"## {name}", ""]
    # Dedupe candidate schemas: one line per distinct (shape, requiredness).
    variants: OrderedDict[tuple[str, bool], list[str]] = OrderedDict()
    for cand in js.get("candidate_schemas", []):
        schema = cand.get("schema") or {}
        shape = type_str(schema)
        if schema.get("type") == "valueset_coding":
            shape += " (valueset-bound)"
        key = (shape, bool(cand.get("required")))
        variants.setdefault(key, []).append(cand.get("spec", "?"))
    for (shape, required), specs in variants.items():
        req = "required" if required else "optional"
        lines.append(f"- {shape}, {req} — {spec_names_str(specs)}")
    for validator in js.get("json_schema_validators", []):
        symbol = validator.get("symbol", str(validator)) if isinstance(validator, dict) else str(validator)
        lines.append(f"- validator: `{symbol}`")
    if not variants and not js.get("json_schema_validators"):
        lines.append(
            "- shape unknown — no spec declares this field "
            "(check serializers; default is "
            f"{type_str(js.get('default_shape')) if js.get('default_shape') else '?'})"
        )
    stored = js.get("meta_stored_fields", [])
    if stored:
        inner = ", ".join(
            f"{field['name']}: {type_str(field.get('schema'))}" for field in stored
        )
        lines.append(f"- stores (when `__store_metadata__`): {{{inner}}}")
    lines.append("")
    return lines


def write_jsonb_shards(tables: list[dict[str, Any]]) -> None:
    for table in tables:
        jsonb_cols = [c for c in table["columns"] if "jsonb_schema" in c]
        if not jsonb_cols:
            continue
        lines = [
            f"# {table['db_table']} JSONB shapes",
            "",
            "Distilled from Pydantic API specs — strong hints, not guarantees; "
            "custom serializers can change the stored shape.",
            "",
        ]
        definitions: OrderedDict[str, dict[str, Any]] = OrderedDict()
        unresolved: set[str] = set()
        for col in jsonb_cols:
            lines.extend(render_jsonb_column(col["name"], col["jsonb_schema"]))
            for defn in col["jsonb_schema"].get("definitions", []):
                definitions.setdefault(defn.get("key", defn["name"]), defn)
            unresolved.update(col["jsonb_schema"].get("unresolved_refs", []))
        if definitions or unresolved:
            lines.extend(["## definitions", ""])
            for _key, defn in sorted(definitions.items()):
                if defn.get("kind") == "enum":
                    vals = " | ".join(repr(v) for v in defn["values"])
                    lines.append(f"- `{defn['name']}`: {vals}")
                else:
                    lines.append(f"- `{defn['name']}`: {fields_str(defn)}")
            if unresolved:
                lines.append(f"- unresolved refs: {', '.join(sorted(unresolved))}")
            lines.append("")
        (SCHEMA_DIR / "jsonb" / f"{table['db_table']}.md").write_text("\n".join(lines))


def write_enums_shard(enums: list[dict[str, Any]]) -> None:
    lines = [
        "# Enum / Choices Catalog",
        "",
        "Every enum-ish class and choices constant found in the scanned source, "
        "grouped by file. Values listed are the **stored database values**. "
        "Columns whose shard shows a bare `choices=Symbol` (unresolved), and "
        "spec-layer enums for columns with no `choices=` at all (common on EMR "
        "status/category columns), can be looked up here by name — prefer the "
        "definition whose file matches the column's `source:` or resource module.",
        "",
    ]
    by_file: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for enum in enums:
        by_file[enum["source_file"]].append(enum)
    for source_file in sorted(by_file):
        lines.append(f"## {source_file}")
        lines.append("")
        for enum in by_file[source_file]:
            values = ", ".join(str(v) for v in enum["values"])
            lines.append(f"- `{enum['class_name']}`: {values}")
        lines.append("")
    (SCHEMA_DIR / "_enums.md").write_text("\n".join(lines))


def write_shards(tables: list[dict[str, Any]], enums: list[dict[str, Any]]) -> None:
    for name in ("tables", "jsonb"):
        shard_dir = SCHEMA_DIR / name
        shard_dir.mkdir(parents=True, exist_ok=True)
        for stale in shard_dir.glob("*.md"):
            stale.unlink()
    model_to_table = {table["model"]: table["db_table"] for table in tables}
    (SCHEMA_DIR / "_conventions.md").write_text(CONVENTIONS_MD)
    write_index_shard(tables, model_to_table)
    write_base_models_shard(tables, model_to_table)
    write_table_shards(tables, model_to_table)
    write_jsonb_shards(tables)
    write_enums_shard(enums)


def _selfcheck_enum_resolution() -> None:
    """An enum-typed ref must resolve to an inline-value definition, not unresolved."""
    # ponytail: self-check runs in main(); no standalone importer to keep isolated
    source_fqn = "x.SourceSpec"
    specs_by_fqn = {
        source_fqn: {"module": "x", "source_file": "x.py", "imports": {}, "fields": []}
    }
    enum_index = {
        "AdmitSourcesChoices": [
            {
                "class_name": "AdmitSourcesChoices",
                "source_file": "x.py",
                "line": 1,
                "values": ["hosp-trans", "emd"],
            }
        ]
    }
    root = ({"type": "ref", "ref": "AdmitSourcesChoices"}, source_fqn)
    definitions, unresolved = collect_embedded_definitions(
        [root], specs_by_fqn, {}, enum_index
    )
    assert unresolved == [], f"selfcheck: unexpected unresolved refs {unresolved}"
    enum_defs = [d for d in definitions if d.get("kind") == "enum"]
    assert enum_defs, "selfcheck: enum ref did not resolve to a definition"
    assert enum_defs[0]["values"] == ["hosp-trans", "emd"], (
        f"selfcheck: wrong enum values {enum_defs[0]['values']}"
    )


def main() -> None:
    _selfcheck_enum_resolution()
    generated_at = datetime.now(UTC).isoformat()
    model_files = iter_model_files()
    spec_files = iter_spec_files()
    print(
        f"scanning {len(model_files)} model files, {len(spec_files)} spec files ...",
        flush=True,
    )

    model_classes, json_schema_constants = parse_model_classes(model_files)
    model_name_index = build_name_index(model_classes)
    models = build_models_catalog(model_classes, model_name_index, json_schema_constants)

    spec_classes = parse_spec_classes(spec_files)
    spec_name_index = build_name_index(spec_classes)
    specs = build_specs_catalog(spec_classes, spec_name_index, model_classes, model_name_index)
    jsonb_fields = build_jsonb_catalog(models, specs)
    enums = parse_enum_classes(model_files + spec_files)
    enum_index: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for enum in enums:
        enum_index[enum["class_name"]].append(enum)
    tables = build_physical_table_catalog(
        models, specs, spec_name_index, jsonb_fields, enum_index
    )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for stale_file in STALE_OUTPUT_FILES:
        (OUTPUT_DIR / stale_file).unlink(missing_ok=True)

    app_configs = [
        {key: value for key, value in config.items() if not key.startswith("_")}
        for config in APP_CONFIGS
    ]
    common_meta = {
        "generated_at": generated_at,
        "generator": rel(Path(__file__)),
        "source_scope": {
            "model_files": [rel(path) for path in model_files],
            "spec_files": [rel(path) for path in spec_files],
        },
    }

    write_json(
        OUTPUT_DIR / OUTPUT_FILE,
        {
            **common_meta,
            "app_configs": app_configs,
            "counts": {
                "physical_tables": len(tables),
                "columns": sum(len(table["columns"]) for table in tables),
                "jsonb_fields": len(jsonb_fields),
                "spec_classes_read_for_jsonb_inference": len(specs),
                "from_pydantic_spec": sum(
                    1 for field in jsonb_fields if field["schema_status"] == "from_pydantic_spec"
                ),
                "from_json_schema_validator": sum(
                    1 for field in jsonb_fields if field["schema_status"] == "from_json_schema_validator"
                ),
                "default_shape_only": sum(
                    1 for field in jsonb_fields if field["schema_status"] == "default_shape_only"
                ),
                "unknown": sum(1 for field in jsonb_fields if field["schema_status"] == "unknown"),
            },
            "tables": tables,
        },
    )
    write_readme(tables, specs, jsonb_fields)
    write_shards(tables, enums)

    care_sha = _git("rev-parse", "HEAD", cwd=PROJECT_ROOT, check=False) or "unknown"
    plugs_raw = os.environ.get("ADDITIONAL_PLUGS", "")
    if not plugs_raw and (REPO_DIR / "plugs.json").is_file():
        plugs_raw = (REPO_DIR / "plugs.json").read_text().strip()
    (SCHEMA_DIR / "PROVENANCE").write_text(
        f"care_sha: {care_sha}\n"
        f"plugs: {plugs_raw or 'none (app/ sources as present in local checkout)'}\n"
        f"generated_at: {datetime.now(UTC).strftime('%Y-%m-%dT%H:%M:%SZ')}\n"
    )

    print(
        "Generated "
        f"{len(tables)} physical tables, {len(jsonb_fields)} JSONB fields "
        f"under {rel(OUTPUT_DIR)}"
    )


if __name__ == "__main__":
    main()
