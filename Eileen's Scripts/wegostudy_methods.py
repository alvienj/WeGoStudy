import datetime
from time import sleep
from selenium import webdriver
import wegostudy_locator as locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
s = Service(executable_path='./chromedriver.exe')
driver = webdriver.Chrome(service=s)

def setUp():
    #  print test start day and time
    print(f'Test started at: {datetime.datetime.now()}')

    # Make a full screen
    driver.maximize_window()

    # Let's wait for the browser respond in general
    driver.implicitly_wait(30)

    # navigating to Moodle app website
    driver.get(locators.wegostudy_url)

    # Checking that we're on the correct URL address and we're seeing correct title
    if driver.current_url == locators.wegostudy_url and driver.title == "WeGoStudy":
        print(f'we are at we go study homepage --{driver.current_url}')
        print(f'we\'re seeing title message --{driver.title} ')
        sleep(1)

    else:
        print(f'we\'re not at the we go study homepage, Check your code!')
        driver.close()
        driver.quit()


def tearDown():
    if driver is not None:
        print(f'------------------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()

def browse_institution():
    driver.find_element(By.LINK_TEXT, 'BROWSE INSTITUTIONS').click()
    sleep(0.5)
    if driver.current_url == locators.browse_institution_url:
        driver.find_element(By.XPATH, "//h2[contains(text(),'Search The Largest Database of Institutions In Can')]").is_displayed()
        sleep(0.5)
        print(f'we are on browse institution page------{driver.current_url}')

        driver.find_element(By.XPATH, "//input[@id='search_field']").click()
        sleep(0.5)

        driver.find_element(By.XPATH, "//input[@id='search_field']").send_keys('Niagara College')
        sleep(0.5)

        driver.find_element(By.XPATH, "//button[@id='search_institute_form']").click()
        sleep(0.5)




setUp()
browse_institution()
tearDown()
