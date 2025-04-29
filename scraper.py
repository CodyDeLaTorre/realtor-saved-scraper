from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import re
from urllib.parse import urlparse


load_dotenv()
USERNAME = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

# Set Chrome options
options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Launch browser
driver = webdriver.Chrome(service=Service(), options=options)

# Visit the target page
driver.get("https://www.realtor.com/myaccount/saved/homes")
time.sleep(3)

# Wait for the modal to be visible (based on data-testid "modal-content")
WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-testid="modal-content"]'))
)

# Wait for the email input field to be visible (using data-testid)
email_input = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-testid="email-input"]'))
)

# Enter your email address
email_input.send_keys(USERNAME)

# Wait for the "Continue" button to be clickable
continue_button = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="continue-button"]'))
)

# Click the "Continue" button
continue_button.click()
time.sleep(2)

# Wait for the modal to be visible
modal = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-testid="modal-content"]'))
)

# Wait for the Password input field to be visible and enter the password
password_input = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-testid="password-input"]'))
)
password_input.send_keys(PASSWORD)


# Wait for the "Login" button to be clickable and click it
login_button = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="login-button"]'))
)
login_button.click()

# Wait for login to process
time.sleep(5)

# Switch back to main content
driver.switch_to.default_content()

# Visit saved homes page
driver.get("https://www.realtor.com/myaccount/saved/homes")
time.sleep(5)

# Wait for and select the dropdown
try:
    dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'select[data-testid="select-element"]'))
    )
    select = Select(dropdown)
    select.select_by_value('for_sale')  # This selects "For Sale"
    print("Selected 'For Sale' from dropdown.")
    time.sleep(2)  # Give the page a moment to reload listings
except Exception as e:
    print(f"Dropdown selection failed: {e}")

def extract_city_from_url(url):
    # Try to extract 'CityName' from the address in the URL
    # Example URL: https://www.realtor.com/realestateandhomes-detail/123-Main-St_CityName_ST_12345_M12345-67890
    match = re.search(r'\/([^_\/]+)_([^_\/]+)_([A-Z]{2})_', url)
    if match:
        return match.group(2)  # Extracts 'CityName'
    return 'unknown'

# Scroll to load content
for _ in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

try:
    cards = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'li.Col__StyledCol-rui__sc-1aq27yt-0 a.card-anchor'))
    )

    seen = set()
    city_links = {}

    for card in cards:
        link = card.get_attribute('href')
        if link and link not in seen:
            seen.add(link)
            city = extract_city_from_url(link)
            city_links.setdefault(city, []).append(link)

    with open('links.txt', 'w') as file:
        for city in sorted(city_links.keys()):
            file.write(f"{city}\n")  # City name as header
            for link in city_links[city]:
                file.write(f"{link}\n")
            file.write("\n")  # Blank line between cities
            print(f"[{city}] {len(city_links[city])} links saved.")

    print("Links sorted by city saved to 'links.txt'.")

except Exception as e:
    print(f"An error occurred: {e}")

driver.quit()
