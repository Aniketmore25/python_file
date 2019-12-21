import logging 
  
#Create and configure logger 
logging.basicConfig(filename="aniket.log", 
                    format='%(asctime)s %(message)s', 
                    filemode='a')

#Creating an object 
logger=logging.getLogger()
  
#Setting the logger to DEBUG 
logger.setLevel(logging.DEBUG) 
  
#Messages 
logger.debug("debug Message") 
logger.info("it can information") 
logger.warning("Its  a Warning") 
logger.error("it has error") 
logger.critical("Internet is not working") 
