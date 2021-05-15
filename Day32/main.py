import datetime
import pandas
import random
import smtplib
today=datetime.datetime.now()
today_tup=(today.month,today.day)

user_mail="Please type the Sender's Email Address here." ##
user_password="Please type the Sender's Email Password here." ##
data=pandas.read_csv("birthdays.csv")
birthdays_dict={
    (data_row["month"],data_row["day"]): data_row for(index,data_row) in data.iterrows()
}
if today_tup in birthdays_dict:
    birthday_person=birthdays_dict[today_tup]
    file_path="letter_templates/letter_"+str(random.randint(1,3))+".txt"
    with open(file_path) as letter_file:
        contents =letter_file.read()
        contents=contents.replace("[NAME]",birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user_mail,user_password)
        connection.sendmail(from_addr=user_mail,to_addrs=birthday_person["email"],msg="Subject:Happy Birthday\n\n"+str(contents))
