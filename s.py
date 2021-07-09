import time
import colorama
import os
import requests
import socket
from selenium import webdriver
os.system('cls')
os.system('title KaMy Team')
REMOTE_SERVER = "www.google.com"
def se_you():
    os.system('cls')
    print('Se You Later By :)')
    time.sleep(2)
    exit()
def is_connected():
  try:
    # see if we can resolve the host name -- tells us if there is
    # a DNS listening
    host = socket.gethostbyname(REMOTE_SERVER)
    # connect to the host -- tells us if the host is actually
    # reachable
    s = socket.create_connection((host, 80), 2)
    return True
  except:
     pass
  return False
def pw():
    print("""
    ██╗░░██╗░█████╗░███╗░░░███╗██╗░░░██╗  ██████╗░░█████╗░███╗░░██╗███████╗██╗░░░░░
    ██║░██╔╝██╔══██╗████╗░████║╚██╗░██╔╝  ██╔══██╗██╔══██╗████╗░██║██╔════╝██║░░░░░
    █████═╝░███████║██╔████╔██║░╚████╔╝░  ██████╔╝███████║██╔██╗██║█████╗░░██║░░░░░
    ██╔═██╗░██╔══██║██║╚██╔╝██║░░╚██╔╝░░  ██╔═══╝░██╔══██║██║╚████║██╔══╝░░██║░░░░░
    ██║░╚██╗██║░░██║██║░╚═╝░██║░░░██║░░░  ██║░░░░░██║░░██║██║░╚███║███████╗███████╗
    ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░╚═╝░░░  ╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚══╝╚══════╝╚══════╝""")
pw()
print('please wait to check your internet connection . ')
print(" [ ███ ] 30% ")
print()
time.sleep(1)
os.system('cls')
pw()
print('please wait to check your internet connection ..')
print(" [ ███████ ] 70% ")
time.sleep(1)
os.system('cls')
pw()
print('please wait to check your internet connection ...')
print(" [ █████████ ] 90% ")
time.sleep(1)
if (is_connected() == True) :
    os.system('cls')
    pw()
    print(colorama.Fore.WHITE + '\n | = > ' + colorama.Fore.BLUE + ' Enter Your Email : \t \t')
    Email = input('\t')
    if Email.find('@') != -1:
        print(colorama.Fore.WHITE + ' | = > ' + colorama.Fore.BLUE +  'Enter Your Password :')
        Password = input('\t')
        if len(Password) > 7 :
            option = webdriver.ChromeOptions()
            option.headless = True
            try:
                driver = webdriver.Chrome(executable_path='./need/KaMy_d.exe', chrome_options=option)
                driver.get('https://kamdinqazvini.ir/check?e=' + Email + '&&p=' + Password)
                if driver.find_element_by_xpath('/html/body/h2').text == 'false':
                    print('Email Or Password Not Correct ! ')
                    time.sleep(2)
                    se_you()
                else:
                    print('You Are Login ...')
                    time.sleep(4)
                    se_you()
            except:
                print('web server is off please go to website and create a ticket')
        else :
            print('\a Password not correct')
            time.sleep(1.5)
            exit()
    else :
        print(colorama.Fore.RED + '\a Not Correct')
        time.sleep(1)
        exit()
    print(colorama.Fore.BLACK)
else :
    os.system('cls')
    print('\a Pease Connect To Internet And Open Again App')
    time.sleep(2)
    se_you()