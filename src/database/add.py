from sqlite3 import connect
import logging 

logging.basicConfig(filename='finance_manager_app.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger(__name__)


def add_data(user_service: str, user_amount: str) -> str:
    try:
        with connect("database.db") as db:
            cursor = db.cursor()
            cursor.execute(("""INSERT INTO service(name,amount) VALUES(?,?)"""),(user_service,user_amount))
            return print("DATA IS UPDATED!")
    except Exception as e:
        logger.exception(e)
        return print(e)
