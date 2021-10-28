import logging
from datetime import datetime
import os,sys
import threading
sys.path.append(os.path.join(os.getcwd()))

def Logger():
    global logPath, resultPath, proDir
    proDir = sys.path[-1]
    resultPath = os.path.join(proDir, "result")
    # create result file if it doesn't exist
    if not os.path.exists(resultPath):
        os.mkdir(resultPath)
    # defined test result file name by localtime
    logPath = os.path.join(resultPath, str(datetime.now().strftime("%Y%m%d%H%M%S")))
    # create test result file if it doesn't exist
    if not os.path.exists(logPath):
        os.mkdir(logPath)
    # defined logger
    logger = logging.getLogger()
    # defined log level
    logger.setLevel(logging.INFO)

    # defined handler
    handler = logging.FileHandler(os.path.join(logPath, "output.log"),encoding="utf-8")
    # defined formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # defined formatter
    handler.setFormatter(formatter)
    # add handler
    logger.addHandler(handler)
    return logger

logger = Logger()




