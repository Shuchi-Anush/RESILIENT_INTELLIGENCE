# Mini warehouse corpus

This fixture is a tiny inventory and order-processing system.

- `sample.py` defines `InventoryService`.
- `sample2.py` defines `Warehouse`, `record_event`, and `OrderProcessor`.
- `OrderProcessor` depends on `InventoryService`, which depends on `Warehouse`.

See [architecture.md](architecture.md) for the intended layering.
