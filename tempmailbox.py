import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import json

url = 'https://temp-mailbox.com/'
driver = webdriver.Chrome()
driver.get(url)

# storing
email_domains = set()
counter = 0
while True:
    # generate mail
    email_input = driver.find_element(By.ID, 'trsh_mail')  # Update with the correct ID
    email_value = email_input.get_attribute('value')

    # get domain name only
    domain = email_value.split('@')[1]

    # remove duplicates
    if domain not in email_domains:
        email_domains.add(domain)
        # print(email_domains)

    # delete
    delete_button = driver.find_element(By.XPATH, '/html/body/section[1]/div/div/div/div/div[2]/div/div[3]/a')
    delete_button.click()
    time.sleep(5)

    # # refresh
    # refresh_button = driver.find_element(By.XPATH, '/html/body/section[1]/div/div/div/div/div[2]/div/div[1]/a')
    # refresh_button.click()
    # time.sleep(5)
    counter += 1

    # Check for a condition to break the loop, for example, after 5 iterations
    # if len(email_domains) >3:
    #     break

    if counter > 50:
        break


# Convert the set to a list and then to JSON
#convert set to dict
emails = []
for domain in email_domains:
    email_dict = {}
    email_dict["website_name"] = "Temp-mailbox"
    email_dict["mail_domain_name"] = domain
    emails.append(email_dict)


json_data = json.dumps(emails, indent=4)
print(json_data)
print(f"No of times page has been refreshed: {counter}")
# close browser
driver.quit()
