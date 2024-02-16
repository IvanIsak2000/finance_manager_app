import logging
import datetime
import os 
from constants import log_folder

if not os.path.exists(log_folder):
    os.makedirs(log_folder)

data = datetime.datetime.today().ctime().split()
filename = f'{log_folder}/{data[1]}_{data[2]}__Time_{"_".join(data[3].split(":"))}.log'
logging.basicConfig(filename=filename, level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s {%(pathname)s:%(lineno)d} %(message)s'
                    )
logger = logging.getLogger(__name__)