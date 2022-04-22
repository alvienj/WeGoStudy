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

def sign_in():
    driver.find_element(By.XPATH, "//b[normalize-space()='LOGIN']").click()
    sleep(0.5)

    driver.find_element(By.XPATH, "//input[@id='user_email']").send_keys('chris.velasco78@gmail.com')
    sleep(0.5)

    driver.find_element(By.XPATH,"//input[@id='user_password']").send_keys('123cctb')
    sleep(0.5)

    driver.find_element(By.XPATH, "//input[@name='commit']").click()
    sleep(1)

    # driver.find_element(By.XPATH, "//div[@id='authentication']").click()
    # sleep(0.5)

    if driver. current_url == locators.partner_home_url:
        driver.find_element(By.XPATH, "//span[contains(.,'Ch Velasco')]").is_displayed()
        sleep(0.5)
        print(f'Test scenario: login with new credential : username - chris.velasco78@gmail.com, password - 123cctb')

    else:
        print("Check your code!")


def my_wegostudy_applications():
    if driver.current_url == locators.partner_home_url:
        driver.find_element(By.XPATH, "//span[contains(.,'My WeGoStudy')]").click()
        sleep(0.5)
        driver.find_element(By.XPATH, "//a[contains(.,'Applications')]").click()
        sleep(0.5)

        # All Application
        if driver.current_url == locators.mywegostudy_application_url:
            driver.find_element(By.XPATH, "//h4[contains(.,'Admission Applications')]").is_displayed()
            sleep(0.5)
            print(f'we are at Application home page -- {driver.current_url}')

        else:
            print(' we are not landing at application page, check your code')

        driver.find_element(By.XPATH, "//a[contains(.,'All Applications')]").click()
        sleep(0.5)

        driver.find_element(By.XPATH, "//a[contains(.,'AS000071-35')]").is_displayed()
        sleep(0.5)

        # navigate to Edit admission application by application number.
        driver.find_element(By.XPATH, "//a[contains(.,'AS000071-35')]").click()
        sleep(2)

        # switch to new tab
        driver.switch_to.window(driver.window_handles[1])
        sleep(0.5)

        if driver. current_url == locators.edit_reza_admission_url:
            assert driver.find_element(By.XPATH, "//h4[contains(.,'Edit admission application for Reza')]").is_displayed()
            print(f' we are at Edit admission application for Reza page.')

        else:
            print('check your code!')
        driver.close()

        # switch to original tab
        driver.switch_to.window(driver.window_handles[0])

        # Id Number
        driver.find_element(By.XPATH, "//a[contains(.,'S000071')]").is_displayed()
        sleep(0.5)

        driver.find_element(By.XPATH, "//a[contains(.,'S000071')]").click()
        sleep(0.5)

        # switch to new tab
        driver.switch_to.window(driver.window_handles[1])
        sleep(0.5)

        if driver.current_url == locators.reza_detail_url:
            driver.find_element(By.XPATH, "//a[contains(.,'Personal Details:')]").is_displayed()
            driver.find_element(By.XPATH, "//a[contains(.,'Reza')]").is_displayed()
            print(f' we are at student details page.')

        else:
            print('check your code')
        driver.close()

        # switch to original tab
        driver.switch_to.window(driver.window_handles[0])

        #First name, Lastname
        driver.find_element(By.XPATH, "//a[contains(.,'Reza')]").is_displayed()
        sleep(0.5)

        driver.find_element(By.XPATH, "//a[contains(.,'sada')]").is_displayed()
        sleep(0.5)

        # school
        driver.find_element(By.XPATH, "//a[contains(.,'Algonquin College')]").is_displayed()
        sleep(0.5)

        driver.find_element(By.XPATH, "//a[contains(.,'Algonquin College')]").click()
        sleep(0.5)

        # switch to new tab
        driver.switch_to.window(driver.window_handles[1])
        sleep(0.5)
        if driver.current_url == locators.algonquin_college_url:
            print('we are at ALGONQUIN COLLEGE home page ')
        driver.close()

         # switch to original tab
        driver.switch_to.window(driver.window_handles[0])
        sleep(0.5)

        #Programs
        driver.find_element(By.XPATH, "//a[contains(.,'Forestry Technician')]").is_displayed()
        sleep(0.5)
        driver.find_element(By.XPATH, "//a[contains(.,'Forestry Technician')]").click()
        sleep(0.5)

        # switch to new tab
        driver.switch_to.window(driver.window_handles[1])
        sleep(0.5)

        if driver.current_url == locators.forestry_technician_url:
            driver.find_element(By.XPATH, "//h4[contains(.,'Forestry Technician')]").is_displayed()
            print('we are at Forestry Technician page.')
        driver.close()

        # switch to original tab
        driver.switch_to.window(driver.window_handles[0])
        sleep(0.5)

        # status
        driver.find_element(By.XPATH, "//span[@class='badge badge-incomplete status-badge']").is_displayed()
        sleep(0.5)

        # status date
        driver.find_element(By.XPATH, "//td[contains(.,'April 21, 2022')]").is_displayed()
        sleep(0.5)

        # check select
        driver.find_element(By.XPATH, "//label[@for='application_ids_84']").click()
        sleep(0.5)

        # Chat
        driver.find_element(By.XPATH, "//i[@class='fa fa-comments-o']").click()
        sleep(0.5)

        driver.find_element(By.XPATH, "//input[@id='admin_message_content']").click()
        sleep(0.5)

        driver.find_element(By.XPATH, "//input[@id='admin_message_content']").send_keys(locators.subject)
        sleep(0.5)

        driver.find_element(By.XPATH, "//i[@class='fa fa-paper-plane']]").click()
        sleep(0.5)

        driver.find_element(By.XPATH, "//i[@class='fa fa-comments-o']").click()
        sleep(0.5)
        print('successfully sent message!')

        driver.find_element(By.XPATH, "///button[@class='btn btn-default btn-sm']").click()
        sleep(0.5)










        # driver.find_element(By.XPATH, "//button[@id='pay_for_application']").click()
        # sleep(0.5)
        # if driver.current_url == locators.pay_application_url:
        #     driver.find_element(By.XPATH,"//h4[contains(.,'Pay Application fee $ 95')]").is_displayed()
        #
        #
        # # Incompleted Applications
        # driver.find_element(By.XPATH, "//a[contains(.,'Incomplete Applications')]").click()
        # if driver.current_url == locators.mywegostudy_incomplete_application_url:
        #
        # # Summited Applications
        # driver.find_element(By.XPATH,"//a[contains(.,'Submitted Applications')]"). click()
        # if driver.current_url == locators.mywegostudy_submitted_application_url:
        #
        # # Approved Application
        # driver.find_element(By.XPATH,"//a[contains(.,'Approved Applications')]").click()
        # if driver.current_url == locators.mywegostudy_approved_application_url:
        #
        #
        # # Accepted Applications
        # driver.find_element(By.XPATH, "//a[contains(.,'Accepted Applications')]").click()
        # if driver.current_url == locators.mywegostudy_accepted_application_url:





setUp()
# browse_institution()
sign_in()
my_wegostudy_applications()
# tearDown()
