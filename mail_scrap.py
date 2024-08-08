import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://temp-mail.io/en'
driver = webdriver.Chrome()
driver.get(url)

# List to store email domains
email_domains = set()  # Using a set to automatically handle duplicates

# Repeat the following actions until the condition is met
while True:
    try:
        # Wait for the new email to be generated
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'email'))
        )
        domain_value = email_input.get_attribute('value')
        domain = domain_value.split('@')[1] if '@' in domain_value else None

        # Check if the domain is not a duplicate
        if domain and domain not in email_domains:
            # Add the domain to the set
            email_domains.add(domain)

            # Simulate deleting the temporary email
            delete_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'header-btn__text'))
            )
            delete_button.click()

            # Simulate refreshing the page
            refresh_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'header-btn__text'))
            )
            refresh_button.click()

            # Wait for the page to load after refresh
            time.sleep(2)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    # Check your specific condition for breaking the loop
    if len(email_domains) >= 0:  # Change this condition as needed
        break

# Convert the set to a list and then to JSON
json_data = json.dumps(list(email_domains), indent=2)

# Print or save the JSON data as needed
print(json_data)

# Close the browser window
driver.quit()
