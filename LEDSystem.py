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
    


schedule.every().day.at("20:11").do(openLED)
schedule.every().day.at("20:15").do(closeLED)

now = datetime.datetime.now()

# Start Time
start_time_begin = now.replace(hour=19, minute=0, second=0, microsecond=0)
start_time_end = now.replace(hour=20, minute=14, second=0, microsecond=0)


while True:
    if(ledStatus == False and now >= start_time_begin and now <= start_time_end):
        openLED()
    
    schedule.run_pending()
    time.sleep(1)