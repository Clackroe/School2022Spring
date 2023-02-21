from utils import *
from selenium import webdriver
from selenium.webdriver.common.by import By


def scrape_book_titles(driver: webdriver.Chrome, url: str) -> list:
    """
    Scrapes the book titles from the books to scrape website.

    args:
        - driver: a selenium webdriver object
        - url: the url of the current page within the website

    returns:
        - a list of book titles (strings)    
    """

    # TODO 5: Use the driver to get the url
    driver.get(url)

    # book titles come from the class "product_pod" and the tag "h3" and the tag "a" and title is the attribute "title"
    # But we need to get every book title on the page, so we need to loop through all the books
    # and get the title of each one
    # We can do this by using the find_elements method and passing in the class name "product_pod"
    # This will return a list of all the books on the page

    book_titles = []

    # TODO 6: Get the list of books from the current page using the driver
    # - Save the list of books to the variable `books`
    # - See the README for documentation on locating elements in Selenium
    books = driver.find_elements(By.CLASS_NAME, value="product_pod")

    # TODO 7: Loop through the list of books and get the title of each book
    # - Append the title of each book to the list `book_titles`
    
    for b in books:
        book_titles.append(b.get_attribute("title"))

    return book_titles


def main():
    driver = create_driver(get_chromedriver_path())
    erase_file("titles.txt")
    route_counts = {}
    for route in ROUTES:
        url = build_books_to_scrape_url(route)
        book_titles = scrape_book_titles(driver, url)
        route_counts[route] = len(book_titles)
        write_titles_to_file("titles.txt", book_titles)
    driver.quit()
    write_smallest_and_largest_books(
        "titles.txt", sort_dict_by_value(route_counts))


if __name__ == '__main__':
    main()
