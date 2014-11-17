import logging
import sys

class Logger:
    log = logging.getLogger()
    log_format = logging.Formatter("[%(levelname)s] %(asctime)s # %(message)s")
   
    ch = logging.StreamHandler(sys.stdout)
    fh = logging.FileHandler('log.txt')
        
    @staticmethod
    def enableLogging():
        Logger.log.setLevel(logging.DEBUG)
        
        Logger.ch.setFormatter(Logger.log_format)
        
        Logger.fh.setFormatter(Logger.log_format)
        
        Logger.log.addHandler(Logger.ch)
        Logger.log.addHandler(Logger.fh)