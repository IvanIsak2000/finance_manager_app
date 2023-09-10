from database.class_template import *
from sqlalchemy import exc
from logger import *


Session = sessionmaker(bind=engine)
session = Session()


def add_data(user_service: str, user_amount: str) -> str:
    try:
        data = Table(user_service, user_amount)
        session.add(data)
        session.commit()
        logger.info(f'Added <{user_service}> <{user_amount}>')
        return "Successful! Data updated."
    except exc.IntegrityError:
        session.rollback()
        logger.error('Exist data')
        return 'Error! This data already exists.'

    except Exception as e:
        session.rollback()
        logger.exception(e)
        return e
