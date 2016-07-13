import logging

logging.basicConfig(filename="test.log", format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.warning('is when this event was logged.')
# logging.debug("This message should go to the log file")
# logging.info("So should this")
logging.warning("And this message is printed too")
