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

    # skus = unicode string
    def checkout(self, skus) -> int :

        inventory = {"A": Item(50, 0, (3, 130)),
                     "B": Item(30, 0, (2, 45)),
                     "C": Item(20, 0, None),
                     "D": Item(15, 0, None)}
         if not isinstance(skus, str):
             return -1

         for ch in skus:
             if ch not in inventory.keys()


         if skus == "":
             return 0



        total = 0
        return total



