# Design Notes

## Inventory Flow

1. `InventoryService.reserve` calls `check_stock` before mutating the warehouse.
2. A failed `check_stock` short-circuits and returns `False`.
3. A successful reservation calls `Warehouse.decrement`.

## Audit Trail

Every reservation must call `record_event` so the audit log stays complete.
