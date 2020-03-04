import smtplib
to=input('enter email send to: ')


email=input('enter email for login:')
password=input('enter password to login:')

msg=input('write your message here:')

s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login(email,password)
print("login successful")
s.sendmail(email,to,msg)
print("mail sent!!")
s.quit()
