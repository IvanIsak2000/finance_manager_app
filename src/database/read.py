from database.class_template import *


Session = sessionmaker(bind=engine)
session = Session()


def read_data():
    ## Создать отображение графика расходов.

    for i in session.query(Table).all():
        print(i.name, i.amount)
