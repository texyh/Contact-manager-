from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()



class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String,nullable=False)
    phonenumber = Column(String(14),nullable=False)







engine = create_engine('sqlite:///app.db')
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()