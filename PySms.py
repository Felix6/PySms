import smtplib

# Use sms gateway provided by mobile carrier:
# at&t:     number@mms.att.net
# t-mobile: number@tmomail.net
# verizon:  number@vtext.com
# sprint:   number@page.nextel.com
# claro:    number@vtexto.com
# boost:    number@sms.myboostmobile.com


message = str(raw_input("Please enter message: "))
# Establish a secure session with gmail's outgoing SMTP server using your gmail account
server = smtplib.SMTP( "smtp.gmail.com", 587)

server.starttls()

# Replace <email> and <password> with valid credentials (without <>)
server.login( '<email>', '<password>' )



# Send text message through SMS gateway of destination number

# follow comments above for choosing  target number
server.sendmail( 'foo@bar.com', '<target number>', message)
