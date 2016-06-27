
"""
manager.py: Contains the application functionality


Usage:
	manager.py add (<name> <phonenumeber>)
	manager.py search (<name>)
	manager.py text (<name> <message>)
	manager.py show_all


Options:
	-h --help					Show this screen


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
		except:
			session.rollback()

	def search(self,name):
		self.name = name
		results = session.query(User).filter_by(name).all()
		for i in results:
			if name in i or name == i:
				res.append(i.split(' '))
			continue
		if len(res) == 1:
			if len(res[0]) > 1:
				only_contact = " ".join(res[0])
				print (self.contacts[only_contact])
			else:
				only_contact = res[0][0]
				print (self.contacts[only_contact])
		elif len(res)>1:
			print ('which {}?'.format(name))

			for j in range (len(res)):
				print ('{}{},'.format([j+1],res[j][1]),)

			choice = int(raw_input('\n'))
			rc = ' '.join(res[choice-1])
			print (self.contacts[rc])
		else:
			print (name, 'Not found')

	def show_all_contact(self):
		contacts = session.query(User).all()
		for person in contacts:
			print (person.name,':',person.phonenumber)

	def send_text(self,name,text):
		self.name =  name
		self.text = text
		res =[]

		for i in self.contacts:
			if name in i or name == i:
				res.append(i.split(' '))
			continue
		if len(res) == 1:
			if len(res[0]) > 1:
				only_contact = " ".join(res[0])
				print ('sending message to {}'.format(self.contacts[only_contact]))
				send_message(self.contacts[only_contact],text)
			else:
				only_contact = res[0][0]
				print ('sending message to {}'.format(self.contacts[only_contact]))
				send_message(self.contacts[only_contact],text)
		else:
			print ('which {}?'.format(name))

			for j in range (len(res)):
				print ('{}{},'.format([j+1],res[j][1]),)

			choice = int(raw_input('\n'))
			rc = ' '.join(res[choice-1])
			print ('sending message to {}'.format(self.contacts[rc]))
			send_message(self.contacts[rc],text)
if __name__ == "__main__":
	arguements = docopt(__doc__)
	contact = Contact()
	if arguements['add']:
		contact.add_contacts(arguements['<name>'],arguements['<phonenumeber>'])
	elif arguements['search']:
		contact.search(arguements['<name>'])
	elif arguements['show_all']:
		contact.show_all_contact()

	else:
		contact.send_text(arguements['<name>'],arguements['<text>'])
		
		