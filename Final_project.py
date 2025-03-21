##################### Extra Hard Starting Project ######################

#USE PYHTONANYWHERE WEBSITE TO RUN ANY CODE DAILY
import pandas as pd,datetime as dt,os,random,smtplib
# 1. Update the birthdays.csv
data = pd.read_csv("birthdays.csv")
row_index = 0
# Extract the first row of data into a list
column_names = data.columns.tolist()
# data_count = int(input("enter the number of inputs you want to gi[NAME]ve into the csv"))
# for j in range(data_count):
#     for i in column_names:
#         details = input(f"enter the {i}")
#         data.at[row_index, i] = details
#         data.to_csv("birthdays.csv")
#     row_index += 1
# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
this_month = now.month
today = now.day
name = ""
day_list = data['day'].to_list()
month_list = data['month'].to_list()
for i in range(len(day_list)):
    if day_list[i] == today and month_list[i] == this_month:
        name = data.at[i,'name']
        email = data.at[i,'email']

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

file_names = os.listdir("/home/pardhu/PycharmProjects/Email_generator/birthday-wisher-extrahard-start/letter_templates")
letter = random.choice(file_names)
open_letter = f"letter_templates/{letter}"
with open(open_letter,"r") as email_letter:
    file_data = email_letter.read()

if name:
    new_data = file_data.replace("[NAME]",name)
else:
    print("today there is no one's birthday")
    exit(0)

# 4. Send the letter generated in step 3 to that person's email address.


my_email = "apashyamkirikiri849@gmail.com"
password = "bqsiwpqrnninvoww"
try:
    connection = smtplib.SMTP("smtp.gmail.com",587)# port is must
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=email, msg=f"Subject:Happy Birthday\n\n {new_data}")
    connection.close()
    print("Email sent successfully!")

except Exception as e:
    print(f"An error occurred: {str(e)}")



