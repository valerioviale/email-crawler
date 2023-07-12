import re
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from openpyxl import Workbook

domains = [
    'unica.it'
    # Add more domains here...
]

email_set = set()

# Set up Selenium WebDriver (ensure you have the appropriate driver executable for your browser installed)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # starts the webdriver

for domain in domains:
    try:
        url = 'http://www.' + domain
        driver.get(url)

        # Find all elements containing email addresses
        email_elements = driver.find_elements(By.XPATH, '//a[contains(@href, "mailto:")]')

        # Extract email addresses from elements
        emails = [re.search(r'mailto:(.+)', element.get_attribute('href')).group(1) for element in email_elements]

        # Exclude email addresses with "pec" after the "@" symbol
        emails = [email for email in emails if not re.search(r'@pec\b', email)]

        # Add found email addresses to the set
        email_set.update(emails)

        # Extract the second-level domain
        domain_parts = domain.split('.')
        if len(domain_parts) > 2:
            second_level_domain = '.'.join(domain_parts[1:])
            second_level_url = 'http://www.' + second_level_domain
            driver.get(second_level_url)

            # Find all elements containing email addresses in the second-level domain
            email_elements_second_level = driver.find_elements(By.XPATH, '//a[contains(@href, "mailto:")]')

            # Extract email addresses from elements in the second-level domain
            emails_second_level = [re.search(r'mailto:(.+)', element.get_attribute('href')).group(1) for element in email_elements_second_level]

            # Exclude email addresses with "pec" after the "@" symbol in the second-level domain
            emails_second_level = [email for email in emails_second_level if not re.search(r'@pec\b', email)]

            # Add found email addresses from the second-level domain to the set
            email_set.update(emails_second_level)

            # Open additional pages within the second-level domain
            for i in range(2, 4):  # Example: open pages 2 and 3
                additional_page_url = f'http://www.{second_level_domain}/page{i}.html'  # Modify the URL pattern as per your requirements
                driver.get(additional_page_url)

                # Find all elements containing email addresses on the additional page
                email_elements_additional_page = driver.find_elements(By.XPATH, '//a[contains(@href, "mailto:")]')

                # Extract email addresses from elements on the additional page
                emails_additional_page = [re.search(r'mailto:(.+)', element.get_attribute('href')).group(1) for element in email_elements_additional_page]

                # Exclude email addresses with "pec" after the "@" symbol on the additional page
                emails_additional_page = [email for email in emails_additional_page if not re.search(r'@pec\b', email)]

                # Add found email addresses from the additional page to the set
                email_set.update(emails_additional_page)
    except Exception as e:
        print(f"Error processing domain '{domain}': {str(e)}")

    time.sleep(6)  # Delay for 5 seconds between each domain

# Create an Excel workbook and sheet
workbook = Workbook()
sheet = workbook.active

# Write the extracted email addresses to the sheet
for index, email in enumerate(email_set, start=1):
    sheet.cell(row=index, column=1, value=email)

# Save the workbook to a file
workbook.save('email_addresses.xlsx')

# Close the Selenium WebDriver
driver.quit()
