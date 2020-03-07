from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass
print("Facebook login from terminal")
username = input("Enter your facebook username: ")
password = getpass("Enter your facebook password: ")
driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
element = driver.find_element_by_id("email")
element.send_keys(username)
element = driver.find_element_by_id("pass")
element.send_keys(password)
element.send_keys(Keys.RETURN)
element.close()
