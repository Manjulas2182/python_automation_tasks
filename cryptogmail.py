import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import json
url="https://cryptogmail.com/"
driver=webdriver.Chrome()
driver.get(url)
time.sleep(5)
email_domains=set()
counter=0
while True:
    try:
        input_mail=driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div/div[1]/div')
        generate_mail=input_mail.text
    except NoSuchElementException:
        print("Element not found")
        pass
    domain=generate_mail.split('@')[1]
    if domain not in email_domains:
        email_domains.add(domain)
        # print(email_domains)
    try:
        remove_button=driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div/div[2]/a[4]/span[1]')
        remove_button.click()
        time.sleep(3)
    except NoSuchElementException:
        print("delete button not found")
        pass
    counter+=1
    if counter > 30:
        break

emails=[]
for domain in email_domains:
    email_dict={}
    email_dict["website_domain_name"]="cryptogmail"
    email_dict["mail_domain_name"] = domain
    emails.append(email_dict)
json_data = json.dumps(emails, indent=4)
print(json_data)
print(f"No of times page has been refreshed: {counter}")
driver.quit()