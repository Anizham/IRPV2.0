from selenium import webdriver
from selenium.webdriver.common.keys import Keys
name ="anu"
email=""
number=""
regno="1234"
chrome_path = 'D:\\Anusha\\flipped\\task3\\chromedriver.exe'

driver = webdriver.Chrome(executable_path=chrome_path)
driver.get("http://localhost:8000/attendance/")
print(driver.title)
search_bar = driver.find_element_by_class_name("btn")
search_bar.send_keys(Keys.RETURN)
driver.implicitly_wait(10)

def submit(var):
    if len(var)==0:
        element.send_keys("Invalid ")
        global flag
        flag=flag+1
    else:
        element.send_keys(var)
flag=0
element = driver.find_element_by_name("name")
submit(name)
element = driver.find_element_by_name("email")
submit(email)
element = driver.find_element_by_name("number")
submit(number)
element = driver.find_element_by_name("regno")
submit(regno)
driver.implicitly_wait(10)
if flag==0:
    element.send_keys(Keys.RETURN)
print(driver.current_url)
# element.close()