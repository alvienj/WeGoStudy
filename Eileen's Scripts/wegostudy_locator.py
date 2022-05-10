from faker import Faker
fake = Faker(locale='en_CA')
wegostudy_url = 'http://34.233.225.85/'
partner_home_url = 'http://34.233.225.85/partner/home'
mywegostudy_application_url = 'http://34.233.225.85/partners/admissions'
mywegostudy_incomplete_application_url = 'http://34.233.225.85/partners/admissions?filter_status=incomplete'
mywegostudy_submitted_application_url = 'http://34.233.225.85/partners/admissions?filter_status=submitted'
mywegostudy_approved_application_url = 'http://34.233.225.85/partners/admissions?filter_status=approved'
mywegostudy_accepted_application_url= 'http://34.233.225.85/partners/admissions?filter_status=accepted'
mywegostudy_students_url = 'http://34.233.225.85/partners/student_details'
mywegostudy_new_students_url ='http://34.233.225.85/partners/student_details/new'
pay_application_url ='http://34.233.225.85/partners/admissions/ch-velasco-5501a8d5-75ee-4959-89c6-017834c81b08/application_fee'
first_name = fake.first_name()
last_name = fake.last_name()
email = fake.email()
city = fake.city()
full_name = f"{first_name} {last_name}"
phone = fake.phone_number()
passport = fake.swift8()
address = fake.street_address()
postalcode = fake.postcode()
message = fake.sentence(nb_words=100)
application_number = 'AS000116-59'
id_number = 'S000116'
edit_application_admission_url = 'http://34.233.225.85/partners/admissions/ch-velasco-f167644a-7489-48ef-9fe5-79a23a329286/edit'
application_detail_url = 'http://34.233.225.85/partners/partner_details/student_detail/allan-yu'
school_url = 'http://34.233.225.85/institutes/cambrian-college'
school_name = 'Cambrian College'
school_website_url ='https://cambriancollege.ca/'
school_website_tuition_url = 'https://cambriancollege.ca/apply/how-to-apply/tuition-and-fees/'
programs_url = 'http://34.233.225.85/institutes/cambrian-college/institute_programs/project-management-579'
program_name = 'Project Management'
program_title = 'Project Management'
status_date = 'May 04, 2022'
browse_institution_url = 'http://34.233.225.85/browse-institutions'
subject = fake.sentence(nb_words=50)
card_holder_name = fake.name()
card_number = fake.credit_card_number()
card_expired_month = fake.month()
card_expired_year = '2023'
cvc = fake.credit_card_security_code()