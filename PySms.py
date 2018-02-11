import smtplib
from collections import OrderedDict

print '''
/$$$$$$$             /$$$$$$
| $$__  $$           /$$__  $$
| $$  \ $$ /$$   /$$| $$  \__/ /$$$$$$/$$$$   /$$$$$$$
| $$$$$$$/| $$  | $$|  $$$$$$ | $$_  $$_  $$ /$$_____/
| $$____/ | $$  | $$ \____  $$| $$ \ $$ \ $$|  $$$$$$
| $$      | $$  | $$ /$$  \ $$| $$ | $$ | $$ \____  $$
| $$      |  $$$$$$$|  $$$$$$/| $$ | $$ | $$ /$$$$$$$/
|__/       \____  $$ \______/ |__/ |__/ |__/|_______/
           /$$  | $$
          |  $$$$$$/
           \______/
        '''

print "Choose carrier\n"


gatewayServers = OrderedDict([('AT&T','@mms.att.net'),
							  ('T-Mobile','@tmomail.net'),
							  ('Verizon','@vtext.com'),
							  ('Sprint','@page.nextel.com'),
							  ('Claro','@vtexto.com'),
							  ('Boost','@sms.myboostmobile.com')])

for i,x in enumerate(gatewayServers, start=1):
    print str([i]),x

gateway = raw_input("\nChoose gateway: ")
message = raw_input("Please enter message: ")
number = raw_input("Enter target phone number: ")

if gateway == str(1):
    targetNum = number + gatewayServers['AT&T']

elif gateway == str(2):
    targetNum = number + gatewayServers['T-Mobile']

elif gateway == str(3):
    targetNum = number + gatewayServers['Verizon']

elif gateway == str(4):
    targetNum = number + gatewayServers['Sprint']

elif gateway == str(5):
    targetNum = number + gatewayServers['Claro']

elif gateway == str(6):
    targetNum = number + gatewayServers['Boost']

# Establish a secure session with gmail's outgoing SMTP server using your gmail account
server = smtplib.SMTP( "smtp.gmail.com", 587)

server.starttls()

# Replace <email> and <password> with valid credentials (without <>)
server.login( '<email>', '<password>' )
server.sendmail( 'foo@bar.com', targetNum, message)
print "\nMessage Sent"
