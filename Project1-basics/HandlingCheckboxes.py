import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
browser.maximize_window()
browser.execute_script("window.scrollTO(0, document.body.scrollHeight);")

# find all the elements
checkboxes = browser.find_element(By.XPATH,"//input[@type='checkbox']")

for checkbox in checkboxes:
    checkbox.send_keys(Keys.SPACE)

# checking the count of checkboxes in th epage
checked_count = 0
for checkbox in checkboxes:
    if checkbox.is_selected():
        checked_count +=1

expected_checked_count = 9
if checked_count == expected_checked_count:
    print('Checkbox count verified')
else:
    print('Checkbox count mismatch')

time.sleep(5)
browser.close()


""""

# click on the sunday checkbox 
browser.find_element(By.XPATH,"//label[normalize-space()='Sunday']").click()
time.sleep(5)

# click on the sunday checkbox again , now it is unclicked then  
browser.find_element(By.XPATH,"//label[normalize-space()='Sunday']").click()
time.sleep(5)

"""




