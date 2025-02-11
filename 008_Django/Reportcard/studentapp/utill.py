from faker import Faker
fake = Faker()
import random
from studentapp.models import *


def generate_data(n=50):
    dept = Department.objects.all()
   
    for i in range(n):
        d_index = random.randint(0,len(dept)-1)
        d = dept[d_index]
        fname = fake.name().split()[0]
        lname = fake.name().split()[1]
        email=fake.email()
        age  = random.randint(20,40)
        s_id

        print(fname,lname,email,age,d)

