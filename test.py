from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


options = webdriver.ChromeOptions()

options.add_argument('–ignore-ssl-errors=yes')

options.add_argument('–ignore-certificate-errors')


driver = webdriver.Remote(

command_executor='172.17.0.2:4444',

options=options

)


driver.get("http://34.30.4.137")  


name_input = driver.find_element(By.ID, "name")
surname_input = driver.find_element(By.ID, "surname")
email_input = driver.find_element(By.ID, "email")
password_input = driver.find_element(By.ID, "password")

name_input.send_keys("Test")
surname_input.send_keys("User")
email_input.send_keys("test@example.com")
password_input.send_keys("password")


add_user_button = driver.find_element(By.ID, "submit")
add_user_button.click()



user_list = driver.find_element(By.ID, "userList")
if "Test User - test@example.com" in user_list.text:
    print("Kullanıcı başarıyla eklenmiş.")
else:
    print("Kullanıcı eklenirken bir hata oluştu.")

driver.quit()
