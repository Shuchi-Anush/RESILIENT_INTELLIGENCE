# Notes

WHY: OrderProcessor never talks to Warehouse directly. That isolation keeps
stock policy in InventoryService.

HACK: record_event currently prints to stdout instead of a real event bus.

The architecture document claims reservation is gated by check_stock.
