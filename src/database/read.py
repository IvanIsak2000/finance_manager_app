from database.class_template import *
import matplotlib.pyplot as plt 
import matplotlib

matplotlib.use('TkAgg')

Session = sessionmaker(bind=engine)
session = Session()


def read_data():
    items = {}
    for i in session.query(Table).all():
        items[i.name] = i.amount
    names = list(items.keys())
    amounts = list(items.values())
    limit = max(amounts) + (max(amounts)/10)

    fig, ax = plt.subplots()
    bar_container = ax.bar(names, amounts)
    ax.set(ylabel='Amounts ($)', title='Names', ylim=(0, limit))
    ax.bar_label(bar_container, fmt='{:,.0f}')
    plt.show()
