# Architecture

## Layers

1. **Order layer** — `OrderProcessor` accepts customer orders.
2. **Inventory layer** — `InventoryService` decides whether stock can be reserved.
3. **Storage layer** — `Warehouse` holds SKU quantities.

## Data flow

An order flows OrderProcessor -> InventoryService -> Warehouse.

Events are recorded by `record_event` whenever stock is short or reserved.

## Design constraint

Reservation must not occur unless `check_stock` returned true.
