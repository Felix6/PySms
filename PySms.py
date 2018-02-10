import smtplib

from collections import OrderDict

# Use sms gateway provided by mobile carrier:
# at&t:     number@mms.att.net
# t-mobile: number@tmomail.net
# verizon:  number@vtext.com
# sprint:   number@page.nextel.com
# claro:    number@vtexto.com
# boost:    number@sms.myboostmobile.com

print "---PySms---"

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

# Establish a secure session with gmail's outgoing SMTP server using your gmail account
server = smtplib.SMTP( "smtp.gmail.com", 587)

server.starttls()

# Replace <email> and <password> with valid credentials (without <>)
server.login( '<email>', '<password>' )



# Send text message through SMS gateway of destination number

# follow comments above for choosing  target number
server.sendmail( 'foo@bar.com', '<target number>', message)
