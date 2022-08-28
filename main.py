##################### Extra Hard Starting Project ######################
import csv
import datetime as dt
import pandas as pd
import random
import smtplib
# 1. Update the birthdays.csv
PATH_OF_BIRTHDAYS_CSV = "birthdays.csv"
MY_EMAIL = "ENTER YOUR EMAIL"
PASSWORD = "ENTER YOUR PASSWORD"

# 3. Send the letter generated in step 3 to that person's email address.
import datetime as td
def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="ENTER SENDER EMAIL",
            msg=f"Subject: Happy birthday {name} \n\n {new_text}"
        )


on = True
while on:
    name = input("What is the name or nickname of a person you want to add to the database?")
    if name == "Out":
        break
    email = input("What is his/her email?")
    birthday_year = int(input("What year she/he was born?"))
    birthday_month = int(input("What month?"))
    birthday_day = int(input("What day"))
    birthday_date = dt.datetime(year=birthday_year, month=birthday_month, day=birthday_day)
    new_birthday_dict = {"name":[name], "email":[email], "year":[birthday_year], "month":[birthday_month], "day":[birthday_day]}
    data = pd.DataFrame(new_birthday_dict)
    print(data)
    data.to_csv(PATH_OF_BIRTHDAYS_CSV, mode='a', index=False, header=False)

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
today_date = dt.datetime(year=now.year,month=now.month,day=now.day)
check_date = dt.datetime(year=1988, month=12, day=6)

letter = []
with open ("letter_templates/letter_1.txt", mode="r") as txt:
    txt1 = txt.read()
    print(txt1)
    letter.append(txt1)
with open ("letter_templates/letter_2.txt", mode="r") as txt:
    txt2 = txt.read()
    letter.append(txt2)
with open ("letter_templates/letter_3.txt", mode="r") as txt:
    txt3 = txt.read()
    letter.append(txt3)

read_file = pd.read_csv(PATH_OF_BIRTHDAYS_CSV, index_col=0)
for (index, row) in read_file.iterrows():
    if dt.datetime(row.year, row.month, row.day) == check_date:
        text = random.choice(letter)
        new_text = text.replace("[NAME]", row.name)
        name = row.name
        print(new_text)
        send_email()




