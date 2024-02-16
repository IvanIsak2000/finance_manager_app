from database.model import *
import logging 

logger = logging.getLogger(__name__)
logger.info('Read module start')

def read_data():
    with Session(engine) as session:
        logger.info('Connected to db')
        items = {}
        for i in session.query(Waste).all():
            items[i.name] = i.amount
        names = list(items.keys())
        amounts = list(items.values())
        logger.info('Data from database: <%s> <%s>', names, amounts)
        return names, amounts

