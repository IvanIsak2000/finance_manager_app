from database.model import *
from sqlalchemy import exc
from logger import *
from constants import *


def add_data(user_service: str, user_amount: str) -> str:
    with Session(engine) as session:
        try:
            data = Waste(name=user_service, amount=user_amount)
            session.add(data)
            session.commit()
            logger.info(f'Added <{user_service}> <{user_amount}>')
            return DATA_ADD
        except exc.IntegrityError:
            session.rollback()
            logger.error('Exist data')
            return EXIST_DATA
        except Exception as e:
            session.rollback()
            logger.exception(e)
            return e