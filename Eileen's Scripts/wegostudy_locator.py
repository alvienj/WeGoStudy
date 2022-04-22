from faker import Faker
fake = Faker(locale='en_CA')
wegostudy_url = 'http://34.233.225.85/'
partner_home_url = 'http://34.233.225.85/partner/home'
mywegostudy_application_url = 'http://34.233.225.85/partners/admissions'
mywegostudy_incomplete_application_url = 'http://34.233.225.85/partners/admissions?filter_status=incomplete'
mywegostudy_submitted_application_url = 'http://34.233.225.85/partners/admissions?filter_status=submitted'
mywegostudy_approved_application_url = 'http://34.233.225.85/partners/admissions?filter_status=approved'
mywegostudy_accepted_application_url= 'http://34.233.225.85/partners/admissions?filter_status=accepted'
pay_application_url ='http://34.233.225.85/partners/admissions/ch-velasco-5501a8d5-75ee-4959-89c6-017834c81b08/application_fee'
edit_reza_admission_url = 'http://34.233.225.85/partners/admissions/ch-velasco-5501a8d5-75ee-4959-89c6-017834c81b08/edit'
reza_detail_url = 'http://34.233.225.85/partners/partner_details/student_detail/reza'
algonquin_college_url ='http://34.233.225.85/institutes/algonquin-college'
forestry_technician_url ='http://34.233.225.85/institutes/algonquin-college/institute_programs/forestry-technician'
browse_institution_url = 'http://34.233.225.85/browse-institutions'
subject = fake.sentence(nb_words=100)