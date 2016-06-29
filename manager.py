
"""
manager.py: Contains the application functionality


Usage:
	manager.py add  <name> <phonenumber>
	manager.py search (<name>)
	manager.py text (<name> <message>)
	manager.py show_all


Options:
	-h --help	 Show this screen



"""

from textbot import send_message
from docopt import docopt
from pprint import pprint
from models import *

#db session
Session = sessionmaker(bind=engine)
session = Session()

class Contact():
	def __init__(self):
		self.contacts = {}

	def add_contacts(self,name,phone):
		self.name = name
		self.phone = phone
		user = User(name=name,phonenumber=phone)
		try:
			session.add(user)
			session.commit()
			print ('contact saved')
		except:
			session.rollback()

	def search(self,name):
		self.name = name
		results = session.query(User).all()
		found_persons = {}
		for person in results:
			if name in person.name or name == person.name:
				found_persons[person.name] = person.phonenumber 
			continue
		print (found_persons)
		if len(found_persons) == 1:
			print (found_persons[name])
		else:
			print ("Which {}".format(name))
			for i, name in enumerate(found_persons):
				print ([i], name, end=' ',)
			choice = input('')
			print (found_persons[choice])

	def show_all_contact(self):
		contacts = session.query(User).all()
		for person in contacts:
			print (person.name,':',person.phonenumber)

	def send_text(self,name,text):
		self.name =  name
		self.text = text
		
		results = session.query(User).all()
		found_persons = {}
		for person in results:
			if name in person.name or name == person.name:
				found_persons[person.name] = person.phonenumber 
			continue
		
		if len(found_persons) == 1:
			send_message(found_persons[name],text)
		else:
			print ("Which {}".format(name))
			for i, name in enumerate(found_persons):
				print ([i], name, end=' ',)
			choice = input('')
			send_message(found_persons[choice],text)
if __name__ == "__main__":
	arguements = docopt(__doc__)
	contact = Contact()
	if arguements['add']:
		contact.add_contacts(arguements['<name>'],arguements['<phonenumber>'])
	elif arguements['search']:
		contact.search(arguements['<name>'])
	elif arguements['show_all']:
		contact.show_all_contact()

	else:
		contact.send_text(arguements['<name>'],arguements['<message>'])
	
		