from dataclasses import dataclass


# parse the string into an appropiate data structure
# process each item i
# apply business rules to item

# what does an example string look likE??

@dataclass
class Item:
    price: int
    quantity: int
    offer: tuple | None

class CheckoutSolution:

    INVENTORY = {"A": Item(50, 0, (3, 130)),
                 "B": Item(30, 0, (2, 45)),
                 "C": Item(20, 0, None),
                 "D": Item(15, 0, None)}



    def _validateStockInput(self, skus) -> bool:
        if not isinstance(skus, str):
            return False

        for ch in skus:
            if ch not in self.INVENTORY.keys():
                return False
        return True

    # skus = unicode string
    def checkout(self, skus) -> int :

        if not self._validateStockInput(skus):
            return -1

         if skus == "":
             return 0


        for index, stk in skus:
            self.INVENTORY[stk].quantity +=1



        total = 0
        return total


