# a new version of the script, faster, try to fine tune the keywords for better result, explore some of the website you target manually.

import re
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from openpyxl import Workbook

# Define the list of relevant HR keywords in English and Spanish
hr_keywords = [
    # keywords
    'career', 'carreras', 'careers', 'hr', 'human resources', 'recruitment',  'talent', 'employee',
    'talent', 'job', 'jobs', 'opportunities', 'hiring', 'recruiting', 'open positions',
    'about', 'talent', 'hr consultant', 'jobs','contact','contacts'

]
# a list of remote friendly companies, it would result in 40% of websites giving back an email address
domains = [
    
'11onze.cat',
'abaenglish.com',
'affirm.com',
'akamai.com',
'andjaro.com',
'apiumhub.com',
'aplazame.com',
'aratech.es',
'arexmarkets.com',
'atomicjar.com',
'audiense.com',
'backmarket.com',
'bebanjo.com',
'belvo.com',
'bestsecret.com',
'blacklane.com',
'bmat.com',
'boatsgroup.com',
'brainly.com',
'bravostudio.app',
'bryter.io',
'cabify.com',
'camaloon.com',
'capchase.com',
'canonical.com',
'carto.com',
'cdmon.com',
'chartboost.com',
'chess.com',
'citnow.com',
'clarity.ai',
'clarivate.com',
'cloudbees.com',
'clovrlabs.com',
'codurance.com',
'thecolvinco.com',
'confluent.io',
'coopdevs.org',
'copado.com',
'crisistextline.org',
'damavis.com',
'datadoghq.com',
'dealdash.com',
'docker.com',
'docplanner.com',
'ebury.com',
'edgeimpulse.com',
'edpuzzle.com',
'elastic.co',
'element.io',
'empathy.co',
'ensembleip.com',
'eyeseetea.com',
'eventbrite.com'

]

email_set = set()

# Set up Selenium WebDriver (ensure you have the appropriate driver executable for your browser installed)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # starts the webdriver

for domain in domains:
    try:
        url = 'http://www.' + domain
        driver.get(url)

        # Find all links containing the relevant HR keywords in the href attribute
        hr_links = WebDriverWait(driver, 4).until(
            EC.presence_of_all_elements_located((By.XPATH, '//a[' + ' or '.join(f'contains(@href, "{kw.lower()}")' for kw in hr_keywords) + ']'))
        )

        # Iterate over the HR links and open them
        for hr_link in hr_links:
            hr_url = hr_link.get_attribute('href')
            driver.get(hr_url)

            # Wait for the page to load and find all elements containing email addresses
            email_elements = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, '//a[contains(@href, "mailto:")]'))
            )

            # Extract email addresses from elements
            for element in email_elements:
                email = re.search(r'mailto:(.+)', element.get_attribute('href')).group(1)
                if not re.search(r'@(?:pec|cert)\b', email, flags=re.IGNORECASE):
                    email_set.add(email)

    except Exception as e:
        print(f"Error processing domain '{domain}': {str(e)}")

    time.sleep(0)  # Delay for 3 seconds between each domain

# Create an Excel workbook and sheet
workbook = Workbook()
sheet = workbook.active

# Write the extracted email addresses to the sheet
for index, email in enumerate(email_set, start=1):
    sheet.cell(row=index, column=1, value=email)

# Save the workbook to a file
workbook.save('hr_emails.xlsx')

# Close the Selenium WebDriver
driver.quit()
