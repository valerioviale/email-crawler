import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from openpyxl import Workbook

domains = [
    "	https://mercatoelettrico.org	"	,
"	https://www.eni.com	"	,
"	https://www.stellantis.com	"	,
"	https://globaltrading.enel.com	"	,
"	https://www.eni.com	"	,
"	https://www.gse.it	"	,
"	https://www.enel.it	"	,
"	https://www.engie.it	"	
    # Add more domains here...
]

email_set = set()

# Set up Selenium WebDriver
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())  # starts the webdriver

for domain in domains:
    try:
        url = domain
        driver.get(url)

        # Find all links containing the words "contatti" or "info" or "contact" or "contacts" the href attribute
        contact_links = WebDriverWait(driver, 2).until(
            EC.presence_of_all_elements_located((By.XPATH, '//a[contains(@href, "contactos") or contains(@href, "info") or contains(@href, "contact") or contains(@href, "contacts")]'))
        )

        # Iterate over the contact links and open them
        for contact_link in contact_links:
            contact_url = contact_link.get_attribute('href')
            driver.get(contact_url)

            # Wait for the page to load and find all elements containing email addresses
            email_elements = WebDriverWait(driver, 2).until(
                EC.presence_of_all_elements_located((By.XPATH, '//a[contains(@href, "mailto:")]'))
            )

            # Extract email addresses from elements
            for element in email_elements:
                email = re.search(r'mailto:(.+)', element.get_attribute('href')).group(1)
                if not re.search(r'@(?:pec|cert)\b', email, flags=re.IGNORECASE):
                    email_set.add(email)

    except Exception as e:
        print(f"Error processing domain '{domain}': {str(e)}")

    time.sleep(1)  # Delay for 3 seconds between each domain

# Create an Excel workbook and sheet
workbook = Workbook()
sheet = workbook.active

# Write the extracted email addresses to the sheet
for index, email in enumerate(email_set, start=1):
    sheet.cell(row=index, column=1, value=email)

# Save the workbook to a file
workbook.save('email_addresses.xlsx')

# Close the WebDriver
driver.quit()
