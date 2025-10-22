from dataclasses import dataclass


# parse the string into an appropiate data structure
# process each item i
# apply business rules to item

# what does an example string look likE??




class CheckoutSolution:
    @dataclass
    class Item:
        price: int
        quantity: int
        offer: tuple | None

    inventory = {"A":  Item(50, 0, (3, 130)), "B": Item(30, 0, (2, 45), "C": Item(20, 0, None), "D", Item(15, 0, None)}

    # skus = unicode string
    def checkout(self, skus) -> int :


         if not isinstance(skus, str):
             return -1

         if skus == "":
             return 0

         for ch in skus


        total = 0
        return total

