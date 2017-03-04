import smtplib


from_name = 'Neil'
from_addr = 'yourusername@gmail.com' 
to_name ='Nash'
to_addr = 'receiverusername@gmail.com'
subject = 'SMTP email test'
message = """From: {} <{}>
To: Jonny Depp  
Subject: Testing 

Be enlightened

"""

message_to_send = message.format(from_name, from_addr, to_name, to_addr, subject, message)
# Credentials (if needed)
username ='yourusername@gmail.com' 
password = '{youremailapppassword}'
# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(from_addr, to_addr, message_to_send)
server.quit()