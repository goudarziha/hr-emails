from dotenv import load_dotenv
from faker import Faker
from random import randint
from time import sleep
import os, yagmail

load_dotenv()
fake = Faker()
Faker.seed(0)

def create_email(email:str):
    yag = yagmail.SMTP(f'{email}', os.getenv('EMAIL_PASSWORD'))

    to = "hr@opm.gov"
    to_name = 'HR'
    subject = "Re: What did you do last week?"
    sender_name = fake.name()

    action_items = []

    for _ in range(5):
        action_items.append(fake.sentence(nb_words=10, variable_nb_words=False))

    action_items_str = ',\n\n'.join(str(x) for x in action_items)

    contents = f'Dear {to_name},\n\nHere is what I did last week.\n\n{action_items_str}\n\nBest regards,\n{sender_name}'

    yag.send(to, subject, contents)

def create_sleep_time(min: int, max: int): 
    return randint(min, max)

def create_dynamic_email(email_number: int):
    email = os.getenv('EMAIL').split('@')
    new_email = f'{email[0]}+{email_number}@{email[1]}'
    return new_email


if __name__ == '__main__':
    emails_to_send = 5
    sleep_time_min = 5
    sleep_time_max = 10

    for _ in range(1,emails_to_send + 1):
        print(f'sending email... {_}')
        email_address = create_dynamic_email(_)
        create_email(email_address)
        sleep_time = create_sleep_time(sleep_time_min, sleep_time_max)
        print(f'sleeping for {sleep_time} seconds...')
        sleep(sleep_time)
        print("DONE")

    print('all emails sent!')
    