
## Contact Manager Application
-
#### Description
This is simple command line  contact manager application that using Docopt as its command line arguement parser.
It also using twilio  to send one-way texts to people in the contacts.
#### Features
   + Adding  a contact      
         manager.py add name phone.     _eg. manager.py add 'emeka onwuzulike' 08064715300_
   + Searching a the contact list    
         manager.py search name         _eg. manager.py search emeka_    
         if there are multiple emeka in the in the contacts, the application will prompt you with a list of all contacts
         that contains emeka in the name. you are required to specify which one. eg which emeka? [1]  onwuzulike [2] adaobi    i.e _emeka onwuzulike_, and _emeka adaobi_.After you response, the phone number of your choice will be displayed.



