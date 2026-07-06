# emr_deviceservicehistory JSONB shapes

Distilled from Pydantic API specs — strong hints, not guarantees; custom serializers can change the stored shape.

## history

- shape unknown — no spec declares this field (check serializers; default is dict)

## meta

- dict, optional — DeviceServiceHistoryListSpec, DeviceServiceHistoryRetrieveSpec, DeviceServiceHistorySpecBase, DeviceServiceHistoryWriteSpec

## edit_history

- list[dict], optional — DeviceServiceHistoryRetrieveSpec
