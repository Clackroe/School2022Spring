from hashStudentID import key_from_student_ids


class StudentIDManager:
    """
    A class that holds a dictionary of student IDs and has special methods to manage and export the data.

    attributes:
        - student_ids: a dictionary of student IDs (key: student ID, value: list of first and last name strings)
    """

    def __init__(self):
        self.student_ids = {"0321958322": ["Bjarne", "Stroustrup"],
                            "9780262033848": ["Thomas", "Cormen"],
                            "9780131103627": ["Brian", "Kernighan"],
                            "0136042597": ["Stuart", "Russell"]}

    def add_student_id_record(self, student_id: int, first_name: str, last_name: str) -> None:
        """
        Adds a student ID record to the global student_ids dictionary.

        modifies:
            - self.student_ids: adds a new key-value pair to the dictionary
        """
        # TODO 3: Use the proper dictionary method to add a new key-value pair to the dictionary
        # - you must convert the student ID to a string
        # - your value should be a list of the first and last name strings
        pass  # Replace this line with your code
        
        tempID = str(student_id)
    
        self.student_ids.update({tempID: [first_name, last_name]})

    def calculate_all_keys(self) -> None:
        """
        Calculates all possible keys from the student IDs in the global student_ids dictionary.

        - returns: a list of all possible keys and their corresponding student names
        """
        keys = []

        for student_id_A in self.student_ids:
            for student_id_B in self.student_ids:
                if student_id_A == student_id_B:
                    continue
                full_name_A, full_name_B = "", ""
                key, key_info = "", []
                # TODO 4: Grab the names for each student ID and store them in their correct variables
                # - `full_name_A` should be the first and last name of student A
                # - `full_name_B` should be the first and last name of student B
                # - put a space between the first and last name in your full_name variables
                # - remember that the values in the dictionary are lists and must be indexed to get the names
                pass  # Replace this line with your code
                full_name_A = self.student_ids.get(student_id_A)[0] + " " + self.student_ids.get(student_id_A)[1]
                full_name_B = self.student_ids.get(student_id_B)[0] + " " + self.student_ids.get(student_id_B)[1]

                # TODO 5: Calculate the key and store it in a variable called `key`
                # - use the key_from_student_ids() function
                pass  # Replace this line with your code
                
                key = key_from_student_ids(student_id_A, student_id_B)

                # TODO 6: Create a list called `key_info` to store all information for this key
                # - the first element should be the key
                # - the second element should be the full name of student A
                # - the third element should be the full name of student B
                pass  # Replace this line with your code
                
                key_info = [key, full_name_A, full_name_B]

                # TODO 7: Append the `key_info` list to the `keys` list
                pass  # Replace this line with your code
                                
                keys.append(key_info)

        return keys

    def write_all_ids_to_file(self, filename: str) -> None:
        """
        Writes all student ID keys and values to a file.

        modifies:
            - filename: a file containing all student ID keys and values
        """
        all_keys = self.calculate_all_keys()

        with open(filename, "w") as file:
            for key in all_keys:
                file.write(f"{key[0]}: {key[1]} and {key[2]}\n")

        print(f"Successfully wrote {len(all_keys)} keys to {filename}!")


def main():
    manager = StudentIDManager()
    # TODO 8: Add your own and your partner's student IDs to the StudentIDManager
    # - use the add_student_id_record() method
    # - parameters must be strings, passed in the order: student ID, first name, last name
    # - you do not have to enter your real student ID
    pass  # Replace this line with your code
    manager.add_student_id_record("801240326", "Xander", "Cole")
    manager.add_student_id_record("801237098", "Jack", "Douglass")

    # TODO 9: Write all keys to the file "keys.txt"
    # - use the write_all_ids_to_file() method
    pass  # Replace this line with your code
    manager.write_all_ids_to_file("keys.txt")


if __name__ == "__main__":
    main()
