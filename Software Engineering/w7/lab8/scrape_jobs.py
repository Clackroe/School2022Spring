from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from utils import create_driver, get_chromedriver_path, LOCATIONS, ROLES
import os


def create_scraping_url(role, location):
    """
    Creates a URL for scraping jobs from www.talent.com
    - uses f strings to format the url
    """
    url = f"https://www.talent.com/jobs?k={role}&l={location}"
    return url


def scrape_jobs(chromedriver_path, url):
    """
    Scrapes the jobs from the given url
    - uses selenium to scrape the jobs
    - parses the jobs into a list of dictionaries
    - returns the list of dictionaries
    """

    # TODO 2: Create the driver from the chromedriver path and get the url
    driver = create_driver(chromedriver_path)
    driver.get(url)# Replace None with the correct code

    jobs = []

    # TODO 3: Grab all elements with the class "link-job-wrap"
    job_elements = driver.find_elements(By.CLASS_NAME, "link-job-wrap") # Replace None with the correct code

    for job_element in job_elements:
        job = {}  # dictionary to hold the job data

        job_title = job_element.get_attribute("title")
        job_company = job_element.find_element(By.CLASS_NAME, "card__job-empname-label").text
        try:
            job_image = job_element.find_element(By.CLASS_NAME, "card__job-logo")
        except:
            job_image = None
            
        job["title"] = job_title
        job["company"] = job_company
        job["image_url"] = job_image
        
        # TODO 4: Grab the following data from the job element and store each in the job dictionary:
        # - title: stored in the "title" attribute
        # - company: stored in the class "card__job-empname-label", use .text to get the text value
        # - image_url: stored in the class "card__job-logo" src attribute
        #   - NOTE: if the image does not exist, set the image_url to None
        #   - NOTE: use try/except to handle the case where the image does not exist (see README for documentation)
        # - use the variable names "title", "company", and "image_url" as the keys in the job dictionary

        # TODO 5: Append the current job dictionary to the jobs list
        jobs.append(job)

    return jobs


def test_scraping():
    """
    Tests the scraping functions.
    """
    chromedriver_path = get_chromedriver_path()
    for location in LOCATIONS:
        for role in ROLES:
            url = create_scraping_url(role, location)
            jobs = scrape_jobs(chromedriver_path, url)
            print(f"Scraped {len(jobs)} jobs for {role} in {location}.")
        with open("jobs.txt", "w") as f:
            for job in jobs:
                f.write(f"Title: {job['title']}\n")
                f.write(f"Company: {job['company']}\n")
                f.write(f"Image: {job['image_url']}\n")


if __name__ == "__main__":
    test_scraping()
