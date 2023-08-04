from sqlite3 import connect
import logging

logging.basicConfig(filename='finance_manager_app.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger(__name__)


def delete_element(name_to_delete: str) -> str:
    try:
        with connect('database.db') as db:
            cursor = db.cursor()
            query = """DELETE FROM service WHERE name = ?;"""
            cursor.execute(query, (name_to_delete,))
        return print(f'"The element " {name_to_delete} was deleted if it was in the database!')
    except Exception as e:
        logger.exception(e)
        return print(e)

def delete_all() -> str:
    try:
        with connect('database.db') as db:
            cursor = db.cursor()
            query = """DROP table service;"""
            cursor.execute(query)
            return print("All data was deleted, please reboot program!")
    except Exception as e:
        logger.exception(e)
        return print(e)

