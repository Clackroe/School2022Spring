import math


def key_from_student_ids(student_id_A: str, student_id_B: str) -> int:
    """
    Creates a cryptographically unique key from two student IDs.
    - student_id_A: the first student ID
    - student_id_B: the second student ID
    - returns: a unique key from the two student IDs
    """
    hashed_tuple = None

    # TODO 1: Convert the student IDs to integers
    # - keep the variable names as student_id_A and
    pass  # Replace this line with your code
    
    student_id_A = int(student_id_A)
    student_id_B = int(student_id_B)

    # TODO 2: Hash the two student IDs together in a tuple
    # - create a tuple of the two student IDs
    # - remember that tuples are created with parentheses, not brackets
    # - use the built-in hash() function to hash the tuple
    # - store the hashed tuple in a variable called `hashed_tuple`
    pass  # Replace this line with your code
    tuple = (student_id_A, student_id_B)
    hashed_tuple = hash(tuple)
    

    return hashed_tuple


def test_key_from_student_ids():
    """
    Tests the key_from_student_ids function.
    - returns: True if all tests pass, False otherwise
    """
    TEST_CASES = [
        (1, "801325583", "801333333", 8364144825106048592),
        (2, "801333333", "801325583", 7723031223333693408),
        (3, "000000000", "000000000", -8458139203682520985),
        (4, "10", "100", 7651590994047093297)]

    for i, student_id_A, student_id_B, expected_key in TEST_CASES:
        actual_key = key_from_student_ids(student_id_A, student_id_B)
        if actual_key != expected_key:
            print(f"Test {i} failed!")
            print("  - Expected:", expected_key)
            print("  - Actual:", actual_key)
            return False

    return True


def run_menu():
    """
    Runs an interactive cli menu for the key generator.
    """
    print("Welcome to the key generator!")
    while True:
        choice = input(
            "What would you like to do?\na) Generate key from student IDs\nb) Test key generator\nEnter your choice: ")

        if choice == "a":
            student_id_A = input("Enter the first student ID: ")
            student_id_B = input("Enter the second student ID: ")
            print("The key is", key_from_student_ids(
                student_id_A, student_id_B))
            continue_prompt = input("Would you like to continue? (y/n) ")
            if continue_prompt == "n":
                break

        elif choice == "b":
            if test_key_from_student_ids():
                print("All tests passed!")
            continue_prompt = input("Would you like to continue? (y/n) ")
            if continue_prompt == "n":
                break

        else:
            print("Invalid choice.")

    print("Goodbye!")


def main():
    run_menu()


if __name__ == "__main__":
    main()
