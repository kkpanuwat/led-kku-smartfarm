import schedule
import time
import datetime
from colorama import Fore, Back, Style, init
init(autoreset=True)
ledStatus = False

def openLED(table=1):
    print(Fore.GREEN + "open LED on Table : {}".format(table))
    global ledStatus
    ledStatus = True

def closeLED(table=1):
    print(Fore.RED + "closed LED on Table : {}".format(table))
    global ledStatus
    ledStatus = False
    

print(Fore.CYAN+"Start Engince LED System")
schedule.every().day.at("08:00").do(openLED,table = 3)
schedule.every().day.at("20:15").do(closeLED, table = 3)

now = datetime.datetime.now()

# # Start Time
start_time_begin = now.replace(hour=8, minute=00, second=0, microsecond=0)
start_time_end = now.replace(hour=20, minute=14, second=0, microsecond=0)


while True:
    now = datetime.datetime.now()
    if(ledStatus == False and now >= start_time_begin and now <= start_time_end):
        openLED(table=3)
    elif(ledStatus == True and now >= start_time_end):
        closeLED(table=3)

    
    
    
    
    
    
    time.sleep(10)