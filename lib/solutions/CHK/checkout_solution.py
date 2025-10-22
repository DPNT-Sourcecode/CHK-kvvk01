from dataclasses import dataclass
from typing import Optional, Tuple, Dict
from collections import Counter

@dataclass
class Item:
    price: int
    offer: Optional[Tuple[int, int]] = None

    def total_for(self, quantity: int) -> int:
        if not self.offer or quantity == 0:
            return self.price * quantity
        bundle_qty, bundle_price = self.offer
        bundles = quantity // bundle_qty
        remainder = quantity % bundle_qty
        return bundles * bundle_price + remainder * self.price

class CheckoutSolution:
    INVENTORY: Dict[str, Item] = {
        "A": Item(price=50, offer=(3, 130)),
        "B": Item(price=30, offer=(2, 45)),
        "C": Item(price=20, offer=None),
        "D": Item(price=15, offer=None),
    }

    def checkout(self, skus: str) -> int:
        if not isinstance(skus, str):
            return -1

        if skus == "":
            return 0

        for ch in skus:
            if ch not in self.INVENTORY:
                return -1

        counts = Counter(skus)
        total = 0
        for sku, qty in counts.items():
            template = self.INVENTORY[sku]
            total += template.total_for(qty)
        return total


