import smtplib
def login(e_mail, password):
  s = smtplib.SMTP('smtp.gmail.com', 587)
  s.starttls()
  s.login(e_mail, password)
  s.quit()
def send(e_mail, password, msg, receiver):
  s = smtplib.SMTP('smtp.gmail.com', 587)
  s.starttls()
  s.login(e_mail, password)
  s.sendmail(e_mail, receiver, msg)
  s.quit()