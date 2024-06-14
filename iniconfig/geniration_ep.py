import random
import string
def generate_email_password():

    email_length = random.randint(5, 10)  
    email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=email_length))
    email += "@example.com"

    
    password_length = random.randint(8, 12)
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=password_length))

    return email, password

email, password = generate_email_password()
