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
from selenium import webdriver
driver=webdriver.Chrome()  
driver.get(convert(url))
