import logging
import datetime

data = datetime.datetime.today().ctime().split()
filename = f'{data[1]}_{data[2]}_{"_".join(data[3].split(":"))}.log'
logging.basicConfig(filename=filename, level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s {%(pathname)s:%(lineno)d} %(message)s'
                    )
logger = logging.getLogger(__name__)
