from selenium import webdriver
from selenium.webdriver.common.keys import Keys
user_name = "anizham"
password = "Lelitha@67"
chrome_path = 'D:\\Anusha\\flipped\\task3\\chromedriver.exe'

driver = webdriver.Chrome(executable_path=chrome_path)
driver.get("https://www.github.com/login")
element = driver.find_element_by_id("login_field")
element.send_keys(user_name)
element = driver.find_element_by_id("password")
element.send_keys(password)
element.send_keys(Keys.RETURN)
element.close()