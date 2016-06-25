import logging

logging.basicConfig(filename="test.log",level=logging.DEBUG)
logging.debug("This message should go to the log file")
logging.info("So should this")
logging.warning("And this too")

logging.info("Logging date and time:")
logging.info("Logging", format='%(asctime)s', datefmt='%d/%m/%Y %I:%M:%s %p')
