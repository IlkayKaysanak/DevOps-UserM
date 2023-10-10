from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Web tarayıcısını başlat (örneğin Chrome)
driver = webdriver.Chrome()

# Web sitesinin URL'sini açın
driver.get("http://express-app-service.default.svc.cluster.local:4000")  # Web sitesinin URL'sini buraya ekleyin

# Kullanıcı adı, soyadı, e-posta ve parola bilgilerini doldurun
name_input = driver.find_element(By.ID, "name")
surname_input = driver.find_element(By.ID, "surname")
email_input = driver.find_element(By.ID, "email")
password_input = driver.find_element(By.ID, "password")

name_input.send_keys("Test")
surname_input.send_keys("User")
email_input.send_keys("test@example.com")
password_input.send_keys("password")

# "Add User" düğmesine tıklayın
add_user_button = driver.find_element(By.ID, "submit")
add_user_button.click()

# Kullanıcı listesini alın ve kontrol edin
user_list = driver.find_element(By.ID, "userList")
if "Test User - test@example.com" in user_list.text:
    print("Kullanıcı başarıyla eklenmiş.")
else:
    print("Kullanıcı eklenirken bir hata oluştu.")

# Tarayıcıyı kapat
driver.quit()
