import datetime
from time import sleep
from selenium import webdriver
import wegostudy_locator as locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
# s = Service(executable_path='./chromedriver.exe')
# driver = webdriver.Chrome(service=s)
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

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

    driver.find_element(By.XPATH, "//input[@id='user_password']").send_keys('123cctb')
    sleep(0.5)

    driver.find_element(By.XPATH, "//input[@name='commit']").click()
    sleep(1)

    if driver. current_url == locators.partner_home_url:
        driver.find_element(By.XPATH, "//span[contains(.,'Chris Velasco')]").is_displayed()
        sleep(0.5)
        print(f'Test scenario: login with new credential \n'
              f'username - chris.velasco78@gmail.com, password - 123cctb ------is passed.')

    else:
        print("Check your code!")

def students():
    if driver.current_url == locators.partner_home_url:
        driver.find_element(By.XPATH, "//span[contains(.,'My WeGoStudy')]").click()
        sleep(0.5)
        driver.find_element(By.XPATH, "//a[contains(.,'Students')]").click()
        sleep(0.5)

        #students
        if driver.current_url == locators.mywegostudy_students_url:
            driver.find_element(By.XPATH, "//h4[normalize-space()='My Students']").is_displayed()
            sleep(0.5)
            print(f'we are at students home page -- {driver.current_url}')

        else:
            print('we are not landing at students page, check your code')

        driver.find_element(By.XPATH, "//a[text()='Create New Student']").click()
        sleep(0.5)

        # Create a new student
        # personal
        if driver.current_url == locators.mywegostudy_new_students_url:
            driver.find_element(By.XPATH, "//*[@id='user_student_detail_attributes_first_name']").send_keys(locators.first_name)
            sleep(1)

            driver.find_element(By.XPATH, "//*[@id='user_student_detail_attributes_last_name']").send_keys(locators.last_name)
            sleep(1)

            driver.find_element(By.XPATH, "//*[@id='user_student_detail_attributes_birth_date']").click()
            sleep(1)

            driver.find_element(By.XPATH, "//*[@id='user_student_detail_attributes_birth_date']").send_keys('1')
            sleep(1)

            driver.find_element(By.XPATH, "//*[@id='user_student_detail_attributes_passport_number']").send_keys(locators.passport)
            sleep(1)

            driver.find_element(By.XPATH, '//*[contains(@class, "select2-selection")]').click()
            sleep(1)

            driver.find_element(By.XPATH, "//*[contains(@class, 'select2-search__field')]").send_keys('Canada')
            sleep(1)

            driver.find_element(By.XPATH, "//html/body/span/span/span[2]/ul/li").click()
            sleep(1)

            driver.find_element(By.XPATH, "//*[@id='phone_number']").send_keys(locators.phone)
            sleep(1)

            # contact
            driver.find_element(By.XPATH,
                                "//*[@id='user_student_detail_attributes_address_attributes_mailing_address']").send_keys(locators.address)
            sleep(1)

            driver.find_element(By.XPATH, "//span[text()='Country']").click()
            sleep(1)

            driver.find_element(By.XPATH,
                                '//*[@id="user_student_detail_attributes_address_attributes_country_chosen"]\n'
                                '/div/div/input').send_keys('Canada')
            sleep(1)

            driver.find_element(By.XPATH,
                                '//*[@id="user_student_detail_attributes_address_attributes_country_chosen"]\n'
                                '/div/ul/li/em').click()
            sleep(1)

            driver.find_element(By.XPATH, "//span[text()='Province/State']").click()
            sleep(1)

            driver.find_element(By.XPATH,
                                '//*[@id="user_student_detail_attributes_address_attributes_state_chosen"]\n'
                                '/div/div/input').send_keys('British Columbia')
            sleep(1)

            driver.find_element(By.XPATH,
                                '//*[@id="user_student_detail_attributes_address_attributes_state_chosen"]\n'
                                '/div/ul/li/em').click()
            sleep(1)

            driver.find_element(By.XPATH, "//span[text()='City']").click()
            sleep(1)

            driver.find_element(By.XPATH,
                                '//*[@id="user_student_detail_attributes_address_attributes_city_chosen"]\n'
                                '/div/div/input') .send_keys('Kamloops')
            sleep(1)

            driver.find_element(By.XPATH,
                                '//*[@id="user_student_detail_attributes_address_attributes_city_chosen"]/div/ul/li/em').click()
            sleep(1)

            driver.find_element(By.XPATH,
                                "//*[@id='user_student_detail_attributes_address_attributes_zip_code']").send_keys(locators.postalcode)
            sleep(1)

            driver.find_element(By.XPATH, "//*[@id='user_email']").send_keys(locators.email)
            sleep(1)

            #Education
            driver.find_element(By.XPATH, "//span[text()='Credentials']").click()
            sleep(1)

            driver.find_element(By.XPATH,
                                '//*[@id="user_student_detail_attributes_user_educations_attributes_0_credentials_chosen"]\n'
                                '/div/div/input').send_keys('Certificate')
            sleep(1)

            driver.find_element(By.XPATH,
                                '//*[@id="user_student_detail_attributes_user_educations_attributes_0_credentials_chosen"]\n'
                                '/div/ul/li').click()
            sleep(1)

            driver.find_element(By.XPATH,
                                "//*[@id='user_student_detail_attributes_user_educations_attributes_0_school_name']").send_keys('Random High School')
            sleep(1)

            driver.find_element(By.XPATH,
                                "//*[@id='user_student_detail_attributes_user_educations_attributes_0_program']").send_keys(
                'Computer Science')
            sleep(1)

            driver.find_element(By.XPATH, "//span[text()='GPA Scale']").click()
            sleep(1)

            driver.find_element(By.XPATH,
                                '//*[@id="user_student_detail_attributes_user_educations_attributes_0_gpa_scale_chosen"]\n'
                                '/div/div/input').send_keys('4')
            sleep(1)

            driver.find_element(By.XPATH,
                                '//*[@id="user_student_detail_attributes_user_educations_attributes_0_gpa_scale_chosen"]\n'
                                '/div/ul/li').click()
            sleep(1)

            driver.find_element(By.XPATH,
                                "//*[@id='user_student_detail_attributes_user_educations_attributes_0_gpa']").send_keys('4')
            sleep(1)

            #document
            driver.execute_script("window.scrollTo(0,700);")
            sleep(0.5)

            driver.find_element(By.XPATH, "//input[@id='user_student_detail_attributes_documents_attributes_0_file']").send_keys("C:\\practice pic\\browse institution.png")

            # workexperience
            driver.find_element(By.XPATH,
                                "//*[@id='user_student_detail_attributes_work_experiences_attributes_0_type_of_industry']").send_keys('Associate')
            sleep(1)

            driver.find_element(By.XPATH,
                                "//*[@id='user_student_detail_attributes_work_experiences_attributes_0_position_rank']").send_keys('Top floor boss')
            sleep(1)

            driver.find_element(By.XPATH,
                                "//*[@id='user_student_detail_attributes_work_experiences_attributes_0_employer']").send_keys('Self-Employed')
            sleep(1)

            driver.find_element(By.XPATH,
                                "//*[@id='user_student_detail_attributes_work_experiences_attributes_0_title']").send_keys('Associate')
            sleep(1)

            driver.find_element(By.XPATH,
                                "//*[@id='user_student_detail_attributes_work_experiences_attributes_0_job_description']").send_keys(locators.message)
            sleep(1)

            driver.execute_script("window.scrollTo(800,1000);")
            sleep(0.5)

            driver.find_element(By.XPATH, "//*[@name='commit']").click()
            sleep(1)

            print(f'Test scenario: Create New Student ----- successfully created new student\n'
                  f'student name -- {locators.full_name} -------is passed')

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
            print('we are not landing at application page, check your code')

        driver.find_element(By.XPATH, "//a[contains(.,'All Applications')]").click()
        sleep(0.5)

        # application_number
        driver.find_element(By.XPATH, f"//a[contains(.,'{locators.application_number}')]").is_displayed()
        sleep(0.5)

        # navigate to Edit admission application by application number.
        driver.find_element(By.XPATH, f"//a[contains(.,'{locators.application_number}')]").click()
        sleep(2)

        # switch to new tab
        driver.switch_to.window(driver.window_handles[1])
        sleep(1)

        if driver. current_url == locators.edit_application_admission_url:
            assert driver.find_element(By.XPATH, f"//h4[contains(.,'Edit admission application for {locators.full_name}')]").is_displayed()
            print(f'we are landing Edit admission application page - {locators.full_name} \n'
                  f'Test Scenario : Clicking application number to get to Edit admission application page ---- is passed.')

        else:
            print('Fail to landing Edit application page.check your code!')
        sleep(1)
        driver.close()

        # switch to original tab
        driver.switch_to.window(driver.window_handles[0])

        # Id Number
        driver.find_element(By.XPATH, f"//a[normalize-space()='{locators.id_number}']").is_displayed()
        sleep(0.5)

        driver.find_element(By.XPATH, f"//a[normalize-space()='{locators.id_number}']").click()
        sleep(0.5)

        # Navigate to personal detail page
        driver.switch_to.window(driver.window_handles[1])
        sleep(1)

        if driver.current_url == locators.application_detail_url:
            driver.find_element(By.XPATH, f"//td[contains(.,'{locators.first_name}')]").is_displayed()
            sleep(0.5)
            driver.find_element(By.XPATH, f"//td[contains(.,'{locators.last_name}')]").is_displayed()
            sleep(0.5)
            driver.find_element(By.XPATH, f"//h6[contains(.,'{locators.full_name}')]").is_displayed()
            sleep(0.5)
            print(f'we are at {locators.full_name} student details page.\n'
                  f'Test Scenario : Clicking ID number to get to Student detail page ---- is passed.')

        else:
            print('something goes wrong at detail page. check your code')

        sleep(2)
        driver.close()

        # switch to original tab
        driver.switch_to.window(driver.window_handles[0])

        # First name, Lastname
        driver.find_element(By.XPATH, f"//td[contains(.,'{locators.first_name}')]").is_displayed()
        sleep(0.5)

        driver.find_element(By.XPATH, f"//td[contains(.,'{locators.last_name}')]").is_displayed()
        sleep(0.5)
        print(f'Check first name-{locators.first_name}, Last name-{locators.last_name}')

        # navigate to school page
        driver.find_element(By.XPATH, f"//a[contains(.,'{locators.school_name}')]").is_displayed()
        sleep(0.5)

        driver.find_element(By.XPATH, f"//a[contains(.,'{locators.school_name}')]").click()
        sleep(0.5)

        # switch to new tab
        driver.switch_to.window(driver.window_handles[1])
        sleep(0.5)

        if driver.current_url == locators.school_url:
            print(f'we are at {locators.school_name} page ')

        # navigate to college website
            driver.find_element(By.XPATH, "//a[contains(.,'Visit College Website')]").click()
            sleep(0.5)

            driver.switch_to.window(driver.window_handles[2])
            sleep(0.5)

            if driver.current_url == locators.school_website_url:
                print(f'We are at {locators.school_name} website.----{locators.school_website_url}')
                driver.close()

            driver.switch_to.window(driver.window_handles[1])

            driver.find_element(By.XPATH, "//a[contains(.,'Tuition')]").click()
            sleep(0.5)
            driver.switch_to.window(driver.window_handles[2])
            sleep(0.5)
            if driver.current_url == locators.school_website_tuition_url:
                print(f'we are at tuition page of {locators.school_name}\n'
                      f'----{locators.school_website_tuition_url} \
                      Test Scenario : Clicking school and able to navigate to college home page to see tuition.')

                driver.close()

        driver.switch_to.window(driver.window_handles[1])
        sleep(0.5)
        driver.close()

         # switch to original tab
        driver.switch_to.window(driver.window_handles[0])
        sleep(0.5)

        # navigate to Programs page
        driver.find_element(By.XPATH, f"//a[contains(.,'{locators.program_name}')]").is_displayed()
        sleep(0.5)

        driver.find_element(By.XPATH, f"//a[contains(.,'{locators.program_name}')]").click()
        sleep(0.5)

        # switch to new tab
        driver.switch_to.window(driver.window_handles[1])
        sleep(0.5)

        if driver.current_url == locators.programs_url:
            driver.find_element(By.XPATH, f"//h4[contains(.,'{locators.program_title}')]").is_displayed()
            print(f'we are at {locators.program_title}  page.')

        # navigate to college website
            driver.find_element(By.XPATH, "//a[contains(.,'Visit College Website')]").click()
            sleep(0.5)

            driver.switch_to.window(driver.window_handles[2])
            sleep(0.5)

            if driver.current_url == locators.school_website_url:
                print(f'We are at {locators.school_name} website.----{locators.school_website_url}')
                driver.close()

            driver.switch_to.window(driver.window_handles[1])

            driver.find_element(By.XPATH, "//a[contains(.,'Tuition')]").click()
            sleep(0.5)

            driver.switch_to.window(driver.window_handles[2])
            sleep(0.5)

            if driver.current_url == locators.school_website_tuition_url:
                print(f'we are at tuition page of {locators.school_name}\n'
                      f'----{locators.school_website_tuition_url}')

                driver.close()
                driver.switch_to.window(driver.window_handles[1])
                sleep(0.5)
                driver.close()

        driver.switch_to.window(driver.window_handles[0])
        sleep(0.5)

        # status
        driver.find_element(By.XPATH, "//span[contains(.,'Incomplete')]").is_displayed()
        sleep(0.5)

        # status date
        driver.find_element(By.XPATH, f"//td[contains(.,'{locators.status_date}')]").is_displayed()
        sleep(0.5)

        # Chat
        driver.find_element(By.XPATH, "//i[@class='fa fa-comments-o']").click()
        sleep(0.5)

        driver.find_element(By.XPATH, "//input[@id='admin_message_content']").click()
        sleep(0.5)

        driver.find_element(By.XPATH, "//input[@id='admin_message_content']").send_keys(locators.subject)
        sleep(1)

        driver.find_element(By.XPATH, "//input[@id='message_files']").send_keys("C:\\practice pic\\browse institution.png")

        driver.find_element(By.XPATH, "//i[@class='fa fa-paper-plane']").click()
        sleep(0.5)

        driver.find_element(By.XPATH, "//button[contains(.,'Close')]").click()
        sleep(0.5)
        print('successfully sent message!')

        # check select
        driver.find_element(By.XPATH, "//*[contains(@class, 'odd')]/td[9]").click()
        sleep(0.5)

        # pay for application
        driver.find_element(By.XPATH, "//button[@id='pay_for_application']").click()
        sleep(0.5)

        driver.find_element(By.XPATH, "//input[@id='card_name']").send_keys(locators.card_holder_name)
        sleep(0.5)

        driver.find_element(By.XPATH, "//input[@id='card_number']").send_keys(locators.card_number)

        driver.find_element(By.XPATH, "//input[@id='card_month']").send_keys(locators.card_expired_month)
        sleep(0.5)

        driver.find_element(By.XPATH, "//input[@id='card_year']").send_keys(locators.card_expired_year)
        sleep(0.5)

        driver.find_element(By.XPATH, "//input[@id='card_cvc']").send_keys(locators.cvc)
        sleep(0.5)

        driver.find_element(By.XPATH, "//input[@name='commit']").click()
        sleep(0.5)

    # delete_application
    # check select
    driver.find_element(By.XPATH, "//*[contains(@class, 'odd')]/td[9]").click()
    sleep(0.5)

    driver.find_element(By.XPATH, "//button[@id='delete_applications']").click()
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
students()
# my_wegostudy_applications()
# tearDown()
