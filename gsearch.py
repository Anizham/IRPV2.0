from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.parse as urlparse
chrome_path = 'D:\\Anusha\\flipped\\task3\\chromedriver.exe'

driver = webdriver.Chrome(executable_path=chrome_path)
driver.get("https://www.google.com/search?q=test")

results = driver.find_elements_by_css_selector('div.yuRUbf')
link = results[0].find_element_by_tag_name("a")
href = link.get_attribute("href")
print(urlparse.parse_qs(urlparse.urlparse(href).query)["q"])
# search_bar.send_keys(Keys.RETURN)
print(driver.current_url)
# driver.close()