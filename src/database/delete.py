from logger import *
from database.model import *
from constants import * 


def delete_element(name_to_delete: str) -> str:
    with Session(engine) as session:
        try:
            stmt = delete(Waste).where(Waste.name==name_to_delete)
            session.add(stmt)
            session.commit()
            logger.info(THE_ITEM_HAS_BEEN_DELETED)
            return THE_ITEM_HAS_BEEN_DELETED
        except Exception as e:
            logger.error(e)
            return 'Most likely there is no such name'


def delete_all():
    with Session(engine) as session:
        try:
            stmt = delete(Waste)
            session.execute(stmt)
            session.commit()
            logger.info(EVERYTHING_HAS_BEEN_DELETED)
            return EVERYTHING_HAS_BEEN_DELETED
        except sqlalchemy.orm.exc.UnmappedInstanceError:
            logger.error('Name not found')
            return'Name not found'
        except Exception as e:
            logger.error(e)
            return e 
                
