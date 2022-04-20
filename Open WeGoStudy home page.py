from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
import locators as locators
from time import sleep
import datetime

s = Service('C:/Users/User/PycharmProjects/si/WeGoStudy/chromedriver.exe')
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
Teardown2()





