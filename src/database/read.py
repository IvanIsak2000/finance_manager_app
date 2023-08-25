from database.class_template import *


Session = sessionmaker(bind=engine)
session = Session()


def read_data():

    for i in session.query(Table).all():
        print(i)

read_data()
