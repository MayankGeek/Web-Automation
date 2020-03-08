from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass
def main(): 
    def insta_navigator():
        username=input("Enter username: ")
        password=getpass("Enter password: ")
        driver = webdriver.Chrome()
        driver.get("https://www.instagram.com/accounts/login/")
        element = driver.find_element_by_xpath("//input[@name='username']")
        element.send_keys(username)
        element = driver.find_element_by_xpath("//input[@name='password']")
        element.send_keys(password)
        element.send_keys(Keys.RETURN)
        element.close()
    def facebook_navigator():
        username=input("Enter username: ")
        password=getpass("Enter password: ")
        driver = webdriver.Chrome()
        driver.get("https://www.facebook.com/")
        element = driver.find_element_by_id("email")
        element.send_keys(username)
        element = driver.find_element_by_id("pass")
        element.send_keys(password)      
        element.send_keys(Keys.RETURN)
        element.close()  
    def menu():
        print("")
    choice=input("""
                     ###This is a simple CLI based automation tool that helps you login to Instagram and Facebook.### 
                     
                1.Instagram
                2.Facebook
                3.Quit
                Enter your choice: """)
    if choice=="1":
        print("Enter Instagram username and password")
        insta_navigator()
    elif choice=="2":
        print("Enter Facebook username and password")
        facebook_navigator()
    elif choice=="3":
        print("Thank's for using")
    else:
        print("Please enter a valid choice.")
main()
