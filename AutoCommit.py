import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Initialize ChromeDriver using webdriver_manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Set the maximum waiting time for the page to load
driver.implicitly_wait(10)  # Adjust the waiting time as needed (in seconds)

# Open the page
driver.get('https://github.com/valerioviale/email-crawler/edit/main/empty.txt')

# Find the login and password input fields
login_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'login_field')))
password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password')))

# Enter the login and password values
login_input.clear()
login_input.send_keys('viale.valerio@gmail.com')  # Replace 'YourLogin' with the actual username
password_input.clear()
password_input.send_keys('1$Margarita')  # Replace 'YourPassword' with the actual password

# Find the login button and click it
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'commit')))
login_button.click()

time.sleep(4)

# Find the input field and paste the actual date
date_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'cm-content')))
date_input.clear()  # Clear any existing text

# Get the current date and time
current_datetime = datetime.datetime.now()
formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')

time.sleep(4)

# Paste the current date and time into the input field
date_input.send_keys(formatted_datetime)

# Find the first 'Commit changes...' button and click it
first_commit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(.//span, "Commit changes...")]')))
first_commit_button.click()

time.sleep(4)


# Find the second 'Commit changes' button in the new pop-up window and click it
popup_commit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(.//span, "Commit changes")]')))
popup_commit_button.click()

time.sleep(4)


# Close the browser
driver.quit()