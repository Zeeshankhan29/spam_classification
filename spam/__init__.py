import logging
import os


logdirs = 'logs'
os.makedirs(logdirs, exist_ok=True)
filepath = os.path.join(logdirs, 'runninglogs.log')
format = logging.Formatter('[%(asctime)s] : [%(name)s] : [%(levelname)s] : [%(message)s]')

file_handler = logging.FileHandler(filepath)
file_handler.setFormatter(format)


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)