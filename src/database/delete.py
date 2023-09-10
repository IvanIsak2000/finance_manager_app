from sqlite3 import connect
from logger import *

def delete_element(name_to_delete: str) -> None:
    with connect('database.db') as db:
        cursor = db.cursor()
        query = """DELETE FROM service WHERE name = ?;"""
        cursor.execute(query, (name_to_delete,))
    delete_success_message = (f'The element {name_to_delete} was'
                              'deleted if it was in the database!')
    logger.info(f'Element {name_to_delete} was removed if it exist')
    return print(delete_success_message)


def delete_all():
    with connect('database.db') as db:
        cursor = db.cursor()
        query = """DROP table service;"""
        cursor.execute(query)
        logger.info('Deleted all data')
        print("All data will be deleted!")
        return print("Please reboot program!")
