import lib.mail as mail
from lib.colors import *
from sys import platform
from time import sleep
import json
import os
#variables
red = colors.red
green = colors.green
yellow = colors.yellow
blue = colors.blue
purple = colors.purple
cyan = colors.cyan
white = colors.white
reset = colors.reset
input_msg = f"""{blue}┌─[OPTION]─[~]
└──❯❯❯ {white}"""
input_mail = f"""{yellow}┌─[E-MAIL]
└──❯❯❯ {white}"""
input_receiver = f"""{yellow}┌─[RECEIVER E-MAIL]
└──❯❯❯ {white}"""
input_password = f"""{red}┌─[PASSWORD]
└──❯❯❯ {white}"""
msgtext =  f"""{blue}┌─[MESSAGE]
└──❯❯❯ \033[0;0m"""
#functions
def title():
  os.system("clear")
  os.system("java res/title.java")
def loading():
  c = "■"
  for i in range(23):
    print(f"\r{cyan}loading:{i*c}", end="")
    sleep(0.01)
#main
if platform == "linux" or platform == "linux2":
  title()
  loading()
  print(f"\n{red}[1]{yellow} START\n{red}[2] {yellow}PARAMETERS\n{red}[3] {purple}ABOUT\n{cyan}[4] EXIT")
  option = input(input_msg)
  if option == "1":
    if os.path.exists("res/data.json") == True:
      with open("res/data.json", "r") as file:
        db = file.read()
        data = json.loads(db)
      file.close()
      try:
        e_mail = data["email"]
        password = data["password"]
        mail.login(e_mail, password)
      except:
        print(f"{red}error: missing login file")
        sleep(2)
        while True:
          title()
          loading()
          print(f"{white}{purple}\nLOGIN TO CONTINUE{reset}")
          e_mail = input(input_mail)
          password = input(input_password)
          try:
            mail.login(e_mail, password)
            with open("res/data.json", "r") as file:
              db = file.read()
              data = json.loads(db)
              data["email"] = e_mail
              data["password"] = password
              file.close()
              with open("res/data.json", "w") as file:
                db = json.dumps(data, indent = 2)
                file.write(db)
                file.close()
                print(f"{green}alert: login successfully")
                sleep(1)
                os.system("python main.py")
          except:
            print(f"{red}error: incorrect login information{reset}")
    else:
      print(f"{red}error: can't find data.json file{reset}")
    title()
    loading()
    print(f"\n{red}[1] {yellow}SEND EMAIL\n{red}[2] {yellow}SPAM")
    option = input(input_msg)
    if option == "1":
      receiver = input(input_receiver)
      while True:
        msg = input(msgtext)
        mail.send(e_mail, password, msg, receiver)
    elif option == "2":
      receiver = input(input_receiver)
      msg = input(msgtext)
      while True:
        mail.send(e_mail, password, msg, receiver)
    else:
      print(f"{red}error: invalide option{reset}")
  elif option == "2":
    ask = input(f"{cyan}do you want to logout? [y/n]: ")
    if ask == "y":
      try:
        with open("res/data.json", "r") as file:
          db = file.read()
          data = json.loads(db)
          data["email"] = ""
          data["password"] = ""
          file.close()
          with open("res/data.json", "w") as file:
            db = json.dumps(data, indent = 2)
            file.write(db)
            file.close()
            print(f"{green}alert: logout succesfully")
            sleep(1)
            os.system("python main.py")
      except:
        print(f"{red}error: can't find data.json file{reset}")
        sleep(2)
        os.system("python main.py")
  elif option == "3":
    print("This tool was invented by the developer A.X.E.L to be used to send emails or carry out spam attacks")
    x = input(f"{green}press enter")
    os.system("python main.py")
  elif option == "4":
    exit()
  else:
    print(f"{red}error: invalide option{reset}")
    os.system("python main.py")
else:
  print("error: unsupported platform")