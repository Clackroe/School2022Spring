from datetime import datetime as dt


class Item:
    def __init__(self, name: str, quantity: int, unit_price: float, discount_percent: float = 0.0):
        """
        A class representing an item in an invoice, with a name, quantity, price, and discount percent.

        args & attributes:
            - name: the name of the item as a string.
            - quantity: the quantity of the item as an integer.
            - unit_price: the price of the item as a float.
            - discount_percent: the discount percent of the item as a float between 0 and 1. Defaults to 0 (no discount)
        """

        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price
        self.discount_percent = discount_percent

    def calculate_item_total_price(self) -> float:
        """
        Calculates the total_price of the item by multiplying the quantity by the unit price and subtracting the discount.

        returns:
            - the total price of the item as a float.
        """
        # TODO 3: Implement this method
        # - Should return the total price of the item as a float, using the formula described in the comment above.
        # - Remember that the discount is a float between 0 and 1, so you'll need to convert it.
        # - You can use the `round` function to round the result to 2 decimal places.
        pass  # Replace this line with your code


class Invoice:

    def __init__(self, client_name: str, date: dt = dt.now().strftime("%Y-%m-%d"), discounted=False):
        """
        A class representing an invoice, with a client name, date, and a list of items.

        args & attributes:
            - client_name: the name of the client as a string.
            - date: the date of the invoice as a string. Defaults to the current date.
            - discounted: a boolean indicating whether the invoice is discounted. Defaults to False.
            - items: a list to hold the items in the invoice. Defaults to an empty list.
        """

        self.client_name = client_name
        self.date = date
        self.discounted = discounted
        self.items: list[Item] = []

    def add_item(self, name: str, quantity: int, unit_price: float, discount_percent: float = 0.0):
        """
        Creates an `Item` object and appends it to the `self.items` list.

        args:
            - name: the name of the item as a string.
            - quantity: the quantity of the item as an integer.
            - unit_price: the price of a single unit of the item as a float.
            - discount_percent: the discount percent of the item as a float between 0 and 1. Defaults to 0 (no discount)
        """
        # TODO 6: Implement this method
        # - Should create an Item object and append it to the self.items list.

    def request_input(self):
        """
        Continuously requests input from the user to create an invoice.
        """

        while True:
            # Gets all possible item information from the user
            name = input("Enter item name: ")
            quantity = int(input("Enter item quantity: "))
            unit_price = float(input("Enter item unit price: "))
            discount_percent = float(input("Enter discount percent: "))

            # Adds the item to the invoice
            self.add_item(name, quantity, unit_price, discount_percent)

            # Checks if the user wants to add another item
            run_again = input("Do you want to add another item? (y/n): ")
            if run_again == "n":
                break

    def total_price(self):
        total = 0
        for item in self.items:
            total += item.calculate_item_total_price()
        return total
