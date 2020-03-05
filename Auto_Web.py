from selenium import webdriver
from selenium.webdriver.common.keys import Keys
def convert(url):
    if url.startswith('http://www.'):
        return 'http://' + url[len('http://www.'):]
    if url.startswith('www.'):
        return 'https://' + url[len('www.'):]
    if not url.startswith('https://'):
        return 'https://www.' + url+".com"
    return url 
url=input("Enter a website name/url: ")
print(convert(url))
username = input("Enter your email-id: ")
password = input("Enter your password: ")
driver = webdriver.Chrome()
driver.get(convert(url))
element = driver.find_element_by_id("email")
element.send_keys(username)
element = driver.find_element_by_id("pass")
element.send_keys(password)
element.send_keys(Keys.RETURN)
element.close()

