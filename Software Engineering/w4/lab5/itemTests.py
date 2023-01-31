from invoice import Item


def test_item_initializes_name() -> tuple[bool, str]:
    """
    Tests that a new Item object is initialized with the correct name.

    returns:
        - a tuple containing a boolean indicating whether the test passed and a string
          containing the error message if the test failed.
    """
    item = Item("Item 1", 1, 1.0)

    fail_case = item.name != "Item 1"

    if fail_case:
        return (False, f"Error in test_item_initializes_name: Incorrect name\n  - Expected: Item 1\n  - Actual: {item.name}")
    else:
        return (True, "Item object name correctly initialized")


def test_item_initializes_quantity() -> tuple[bool, str]:
    """
    Tests that a new Item object is initialized with the correct quantity.

    returns:
        - a tuple containing a boolean indicating whether the test passed and a string
          containing the error message if the test failed.
    """
    item = Item("Item 1", 1, 1.0)

    fail_case = item.quantity != 1

    if fail_case:
        return (False, f"Error in test_item_initializes_quantity: Incorrect quantity\n  - Expected: 1\n  - Actual: {item.quantity}")
    else:
        return (True, "Item object quantity correctly initialized")


def test_item_initializes_unit_price() -> tuple[bool, str]:
    """
    Tests that a new Item object is initialized with the correct unit price.

    returns:
        - a tuple containing a boolean indicating whether the test passed and a string
          containing the error message if the test failed.
    """
    item = Item("Item 1", 1, 1.0)

    fail_case = item.unit_price != 1.0

    if fail_case:
        return (False, f"Error in test_item_initializes_price: Incorrect price\n  - Expected: 1.0\n  - Actual: {item.unit_price}")
    else:
        return (True, "Item object unit price correctly initialized")


def test_item_initializes_discount_percent_false() -> tuple[bool, str]:
    """
    Tests that a new Item object is initialized with a discount_percent value of 0.0 when no value is provided.

    returns:
        - a tuple containing a boolean indicating whether the test passed and a string
    """
    item = Item("Item 1", 1, 1.0)

    fail_case = item.discount_percent != 0.0

    if fail_case:
        return (False, f"Error in test_item_initializes_discounted_percent_false: Incorrect discounted_percent value\n  - Expected: 0.0\n  - Actual: {item.discount_percent}")
    else:
        return (True, "Item object discounted_percent correctly initialized")


def test_item_initializes_discount_percent_true(expected_discount_percent: float = 0.1) -> tuple[bool, str]:
    """
    Tests that a new Item object is initialized with a correct discount_percent value when one is provided.

    args:
        - expected_discount_percent: The expected discount_percent value. (default: 0.1)

    returns:
        - a tuple containing a boolean indicating whether the test passed and a string
    """
    item = Item("Item 1", 1, 1.0, expected_discount_percent)

    fail_case = item.discount_percent != expected_discount_percent

    if fail_case:
        return (False, f"Error in test_item_initializes_discounted_percent_true: Incorrect discounted_percent value\n  - Expected: {expected_discount_percent}\n  - Actual: {item.discount_percent}")
    else:
        return (True, "Item object discounted_percent correctly initialized")


def test_calculate_item_total_price_converts_discount(expected_discount: float = 0.2) -> tuple[bool, str]:
    """
    Tests that the Item.calculate_item_total_price method returns the correct price.

    args:
        - expected_discount: The expected discount value. (default: 0.2)

    returns:
        - a tuple containing a boolean indicating whether the test passed and a string
    """

    # TODO 1: Implement this test.
    # - Create a new Item object with the given expected_discount
    # - Save the total item price by using the the Item.calculate_item_total_price method
    # - Divide the total item price by unit_price * quantity and then subtract the result from 1.0
    # - Compare the result to the expected_discount value
    # - Run the test before implementing the calculate_item_total_price method and check that it fails
    # - TIP: Use the round function to round the result to 2 decimal places
    item = None  # Replace None with the correct code
    fail_case = None  # Replace None with the correct code
    actual_discount = None  # Replace None with the correct code

    if fail_case:
        return (False, f"Error in test_calculate_item_price_converts_discount: Incorrect discount\n  - Expected: {expected_discount}\n  - Actual: {actual_discount}")
    else:
        return (True, "Item.calculate_item_price correctly converts discount_percent to discount")


def test_calculate_item_total_price_correct() -> tuple[bool, str]:
    """
    Tests that the Item.calculate_item_total_price method returns the correct price.

    returns:
        - a tuple containing a boolean indicating whether the test passed and a string
    """

    # TODO 2: Implement this test.
    # - Create a new Item object with the given discount_percent
    # - Calculate the expected item price using the formula:
    #   - item_price = quantity * unit_price * (1 - discount_percent)
    # - Call the Item.calculate_item_price method
    # - Compare the result to the expected value
    # - Run the test before implementing the calculate_item_total_price method and check that it fails
    # - TIP: Use the round function to round the result to 2 decimal places
    item = None  # Replace None with the correct code
    expected_item_price = None  # Replace None with the correct code
    actual_item_price = None  # Replace None with the correct code
    fail_case = None  # Replace None with the correct code

    if fail_case:
        return (False, f"Error in test_calculate_item_price_correct: Incorrect item price\n  - Expected: {expected_item_price}\n  - Actual: {actual_item_price}")
    else:
        return (True, "Item.calculate_item_price method correctly calculates item price")
