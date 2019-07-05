import xlrd
import datetime
import smtplib

file_location = "E:/python project/List.xlsx"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)
today = datetime.datetime.now().date()
birthday = False
connected = True

try:
    mail = smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    mail.login('pnagarkar668@gmail.com', '********')
except:
    print ("Error sending message")
    print ("Mail not sent!")
    connected = False

for i in range(1, sheet.nrows):
    dob = xlrd.xldate.xldate_as_datetime(sheet.cell_value(i, 1),0)
    if dob.day == today.day and dob.month == today.month:
        user = []
        birthday = True
        for j in range(sheet.ncols):
            user.append(sheet.cell_value(i,j))
        print ("Wish Happy Birthday to " + user[0])
        msg = 'Subject: {}\n\n{}'.format("Happy Birthday", "Happy Birthday, " + user[0])
        if connected:
            if user[3] == 'Professional':
                msg = 'Subject: {}\n\n{}'.format("Happy Birthday", "Wish you many many happy returns of the day, " + user[0])
            elif user[3] == 'Friend':
                msg = 'Subject: {}\n\n{}'.format("Happy Birthday", "Happy Birthday dear, " + user[0])
            elif user[3] == 'Relative':
                msg = 'Subject: {}\n\n{}'.format("Happy Birthday", "Wishing you a delightful birthday, " + user[0])
            mail.sendmail('pnagarkar668@gmail.com', user[2], msg)
            print ("Mail sent!")

if not birthday:
    print ("No birthday today!! :)")
if connected:
    mail.close()
