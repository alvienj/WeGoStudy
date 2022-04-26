from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
import locators as locators
from time import sleep
import datetime

s = Service("C:/Users/User/PycharmProjects/si/WeGoStudy/Vien's Scripts/chromedriver.exe")
driver = webdriver.Chrome(service=s)


driver.maximize_window()
driver.implicitly_wait(30)
driver.get(locators.wegostudy_url)


def Setup():
    if driver.current_url == locators.wegostudy_url and driver.title == 'WeGoStudy':
        print('Were at the WeGoStudy homepage')
    else:
        print('Wrong website. Please try again')
        driver.close()
        driver.quit()
    sleep(.5)

def login():
    driver.find_element(By.XPATH, "//b[text()='LOGIN']").click()
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='user_email']").send_keys(locators.login)
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='user_password']").send_keys(locators.password)
    sleep(1)
    driver.find_element(By.XPATH, "//*[@name='commit']").click()
    sleep(1)
    if driver.current_url == 'http://34.233.225.85/partner/home':
        print('You are signed in as a Partner')
    else:
        print('Oh something is wrong.. please fix go back')

def application():
    driver.find_element(By.XPATH, "//*[contains(@class, 'navbar-nav')]/li/a/span").click()
    sleep(1)
    driver.find_element(By.XPATH, "//a[text()='Applications']").click()
    sleep(2)
    driver.find_element(By.XPATH, "//*[contains(@class, 'odd')]/td[9]").click()
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='send_message']").click()
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='message']").send_keys(locators.message)
    sleep(1)
    driver.find_element(By.XPATH, "//*[@name='commit']").click()
    sleep(1)


def Teardown1():
    if driver is not None:
        print(f'Test Started at: {datetime.datetime.now()}')
        print(f'--------------------------------------')

def Teardown2():
    if driver is not None:
        print(f'--------------------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')










Teardown1()
Setup()
login()
application()
Teardown2()
