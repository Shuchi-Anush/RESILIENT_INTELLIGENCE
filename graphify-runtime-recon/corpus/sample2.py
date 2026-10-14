"""Warehouse storage and order processing."""


class Warehouse:
    """In-memory stock map keyed by SKU."""

    def __init__(self) -> None:
        self._stock: dict[str, int] = {}

    def available(self, sku: str) -> int:
        return self._stock.get(sku, 0)

    def decrement(self, sku: str, qty: int) -> None:
        self._stock[sku] = self.available(sku) - qty


def record_event(kind: str, sku: str) -> None:
    print(f"{kind}:{sku}")


class OrderProcessor:
    """Accepts orders and asks InventoryService to reserve stock."""

    def __init__(self, inventory) -> None:
        self.inventory = inventory

    def place_order(self, sku: str, qty: int) -> bool:
        if not self.inventory.check_stock(sku, qty):
            return False
        self.inventory.reserve(sku, qty)
        return True
