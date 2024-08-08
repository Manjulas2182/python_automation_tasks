import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import json
url="https://tempmailers.com/"
driver=webdriver.Chrome()
driver.get(url)
email_domains=set()
counter=0
while True:
    time.sleep(2)
    try:
        input_mail=driver.find_element(By.ID,'email_id')
        new_mail=input_mail.text
        domain=new_mail.split('@')[1]
        if domain not in email_domains:
            email_domains.add(domain)
            # print(email_domains)
    except NoSuchElementException:
        print("Element not found")
        pass
    try:
        delete_button=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div[3]/div')
        delete_button.click()
        time.sleep(3)
    except NoSuchElementException:
        print("delete button not found")
        pass
    counter+=1
    if counter > 40:
        break

emails=[]
for domain in email_domains:
    email_dict={}
    email_dict["website_domain_name"]="temp_mailers"
    email_dict["mail_domain_name"] = domain
    emails.append(email_dict)
json_data = json.dumps(emails, indent=4)
print(json_data)
print(f"No of times page has been refreshed: {counter}")
driver.quit()