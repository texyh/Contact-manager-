from twilio.rest import TwilioRestClient

 

client = TwilioRestClient("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

def send_message(to,msg):
	message = client.messages.create(to=to,from_='+16602024102',body=msg,)
	print ('message sent')

