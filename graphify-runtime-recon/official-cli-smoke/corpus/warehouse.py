"""Inventory and warehouse coordination for the smoke test corpus."""
from dataclasses import dataclass


@dataclass
class Warehouse:
    """In-memory stock store keyed by SKU."""

    stock: dict

    def decrement(self, sku: str, qty: int) -> None:
        # WHY: decrement must only run after the caller verified stock exists.
        self.stock[sku] -= qty


class InventoryService:
    """High-level inventory facade over a Warehouse."""

    def __init__(self, warehouse: Warehouse) -> None:
        self.warehouse = warehouse

    def check_stock(self, sku: str, qty: int) -> bool:
        return self.warehouse.stock.get(sku, 0) >= qty

    def reserve(self, sku: str, qty: int) -> bool:
        if not self.check_stock(sku, qty):
            return False
        self.warehouse.decrement(sku, qty)
        return True


def record_event(name: str, sku: str) -> None:
    # WHY: all reservations must leave an audit trail for later reconciliation.
    print(f"event={name} sku={sku}")
