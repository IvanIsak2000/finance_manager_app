from database.class_template import *

Session = sessionmaker(bind=engine)
session = Session()


def add_data(user_service: str, user_amount: str):
    data = Table(user_service, user_amount)
    session.add(data)
    session.commit()
    print("DATA IS UPDATED!")
