import logging
logging.basicConfig(filename = "myProgramLog.txt", level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
#Logging to Test File
#Example: Buggy Factorial Program
#Factorial 4 is 4*3*2*1 = 24

#logging.DEBUG,logging.INFO,logging.WARNNING,logging.ERROR,logging.CRITICAL
#logging.disable(logging.DEBUG) 

#logging.info() logging.warning() logging.error() logging.critical()[[debug is lowest level]]
logging.debug("Start of program")

def Factorial(n):
    logging.debug('Start of Factorial(%s)' %(n))
    total = 1
    for i in range(1,n + 1):
        total *= i
        logging.debug('i is %s, total is %s' %(i,total))
    logging.debug('Return Value is %s' %(total))
    return total

print(Factorial(4))
logging.debug("End of program")



