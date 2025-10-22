from dataclasses import dataclass, replace


# parse the string into an appropiate data structure
# process each item i
# apply business rules to item

# what does an example string look likE??

@dataclass
class Item:
    price: int
    quantity: int
    offer: tuple | None
    total: int

    #apply business rule as a method
    def get_discount(self) -> int:
        reduction = (self.quantity * self.price)  - self.offer[1]
        return reduction

    def apply_discount(self) :
        new_total = self.total - self.get_discount()
        return replace(self, total=new_total)

    def offer_met(self, index: int) -> bool:

class CheckoutSolution:

    INVENTORY = {"A": Item(50, 0, (3, 130), 0),
                 "B": Item(30, 0, (2, 45), 0),
                 "C": Item(20, 0, None, 0),
                 "D": Item(15, 0, None, 0)}



    def _validate_stock_input(self, skus) -> bool:
        if not isinstance(skus, str):
            return False

        for ch in skus:
            if ch not in self.INVENTORY.keys():
                return False
        return True

    # skus = unicode string
    def checkout(self, skus) -> int :

        if not self._validate_stock_input(skus):
            return -1

         if skus == "":
             return 0

        for index, stk in skus:
            self.INVENTORY[stk].quantity +=1
            #if offer is avaialble for item then check for offer before calcualton
            # otherewise apply buisiness rules



        total = 0
        return total
