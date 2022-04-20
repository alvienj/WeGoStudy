from faker import Faker
fake = Faker()

wegostudy_url = 'http://34.233.225.85/'
getintouch_url = 'http://34.233.225.85/contacts/new'
firstname = fake.first_name()
lastname = fake.last_name()
email = fake.email()
city = fake.city()
message = fake.sentence(nb_words=100)
browseinstitutions_url = 'http://34.233.225.85/browse-institutions'


