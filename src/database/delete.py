from sqlite3 import connect
import sys
from time import sleep


def delete_element(name_to_delete: str):
    with connect('database.db') as db:
        cursor = db.cursor()
        query = """DELETE FROM service WHERE name = ?;"""
        cursor.execute(query, (name_to_delete,))
    delete_success_message = (f'The element {name_to_delete} was'
                              'deleted if it was in the database!')
    print(delete_success_message)


def delete_all():
    with connect('database.db') as db:
        cursor = db.cursor()
        query = """DROP table service;"""
        cursor.execute(query)
        print("All data will be deleted!")
        print("The program will be terminated")
    sleep(3)
    sys.exit()
