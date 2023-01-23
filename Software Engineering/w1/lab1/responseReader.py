import os


def read_file(file_name):
    # TODO: Implement this function
    # - open the file
    # - read the contents and store them in a string
    # - return the string
    pass  # Replace this line with your code
    f = open(file_name)
    str = f.read()
    return str

def test_response_length(a_string: str):
    a_string = a_string.strip()  # strip the string of whitespace
    a_string = a_string.replace(",", "").replace(".", "").replace(
        "!", "").replace("?", "")  # removes common punctuation
    words_list = a_string.split()  # splits the string into a list of words
    if len(words_list) < 125:
        print(
            f"Your response is too short. It should be at least 125 words.\nYour response is {len(words_list)} words long.")
    elif len(words_list) > 500:
        print(
            f"TEST CASE 1: Failed\nYour response is too long. It should be at most 500 words.\nYour response is {len(words_list)} words long.")
    else:
        print(
            f"TEST CASE 1: PASSED\nYour response is an acceptable length ({len(words_list)} words).")


def main():
    while True:
        file_name = input("Enter the name of the file: ")
        if os.path.exists(file_name):
            file_string = read_file(file_name)
            test_response_length(file_string)
            break
        else:
            print("File does not exist")


if __name__ == '__main__':
    main()
