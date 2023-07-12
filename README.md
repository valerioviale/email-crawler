# email-crawler
A selenium python program to extract email addresses from a list of websites
Here's a step-by-step guide with comments to make the program work on a new machine:

Install Python:

Download and install Python from the official Python website (https://www.python.org/downloads/) based on your operating system.
Follow the installation instructions provided during the setup process.
Set up a virtual environment (optional but recommended):

Open a terminal or command prompt.
Install virtualenv by running the command: pip install virtualenv.
Create a new virtual environment by running the command: virtualenv env.
Activate the virtual environment:
On Windows: .\env\Scripts\activate.
On macOS/Linux: source env/bin/activate.
Install required packages:

In the terminal or command prompt with the virtual environment activated, run the following command:
Copy code
pip install selenium webdriver_manager openpyxl
Download and install Chrome WebDriver:

Visit the Chrome WebDriver download page (https://sites.google.com/a/chromium.org/chromedriver/downloads).
Download the appropriate WebDriver version based on your Chrome browser version and operating system.
Extract the downloaded WebDriver executable and note its location.
Update the code:

Open a text editor or Python IDE of your choice.
Copy the code provided earlier into a new file.
Replace the path_to_chromedriver in the following line with the actual path to the downloaded Chrome WebDriver executable:
less
Copy code
driver = webdriver.Chrome(service=Service('path_to_chromedriver'))
Customize domain list (optional):

If you want to crawl additional domains, modify the domains list to include the desired domains.
Save the file:

Save the file with a meaningful name and the .py extension, for example: email_crawler.py.
Run the program:

Open a terminal or command prompt.
Navigate to the directory where you saved the Python file.
Activate the virtual environment if you set it up.
Run the command: python email_crawler.py.
The program will start executing, crawling the specified domains, extracting email addresses, and saving them to an Excel file.
Check the results:

After the program completes, you will find an email_addresses.xlsx file in the same directory as the Python file.
Open the Excel file to view the extracted email addresses.
By following these steps, you should be able to set up and run the email crawler program on a new machine. 
Make sure to install the necessary dependencies, update the code with the correct WebDriver path, and customize the domain list if needed.
