"""Inventory service: tracks stock levels for the warehouse."""

from sample2 import Warehouse, record_event


class InventoryService:
    """Coordinates stock checks against a Warehouse."""

    def __init__(self, warehouse: Warehouse) -> None:
        self.warehouse = warehouse

    def check_stock(self, sku: str, qty: int) -> bool:
        # NOTE: check_stock is the public entry point used by OrderProcessor.
        available = self.warehouse.available(sku)
        if available < qty:
            record_event("stock_short", sku)
            return False
        return True

    def reserve(self, sku: str, qty: int) -> None:
        # WHY: reservation happens only after check_stock succeeds.
        self.warehouse.decrement(sku, qty)
        record_event("stock_reserved", sku)
