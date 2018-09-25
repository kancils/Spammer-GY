#!/usr/bin/python
#E-bomber
#This code for education purpose only.
#Use it at your own risk !!!



import os
import smtplib
import getpass
import sys


print '##############################################\n'
print '##################\n'
print '  SPAMMER GMAIL AND YAHOO VIA TERMUX V1'
print '       Author by: Mr./K5NC1L5'
print '       Contac Me: denishendriawansyah@gmail.com'
print '       YouTube  : D3N15H ID'
print '       TEAM     : Explosion Squad Cyber'
print '###################\n'
print '##############################################\n'

server = raw_input ('MailServer Gmail/Yahoo: ')
user = raw_input('Email: ')
passwd = getpass.getpass('Password: ')


to = raw_input('\nTo: ')
#subject = raw_input('Subject: ') 
body = raw_input('Message: ')
total = input('Number of send: ')

if server == 'gmail':
    smtp_server = 'smtp.gmail.com'
    port = 587
elif server == 'yahoo.com':
    smtp_server = 'smtp.mail.yahoo.com'
    port = 25
    sys.exit()
else:
    print 'Cek Ulang Itu Ada Yang Salah.'
    sys.exit()


try:
    server = smtplib.SMTP(smtp_server,port) 
    server.ehlo()
    if smtp_server == "smtp.gmail.com":
            server.starttls()
    server.login(user,passwd)
    for i in range(1, total+1):
        subject = os.urandom(9)
        msg = 'From: ' + user + '\nSubject: ' + subject + '\n' + body
        server.sendmail(user,to,msg)
        print "\rE-mails sent: %i" % i
        sys.stdout.flush()
    server.quit()
    print '\n Done !!!'
except KeyboardInterrupt:
    print '[-] Canceled'
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print '\n[!] Username Atau Password Lu Ada Yang Salah Bro...'
    sys.exit()
    