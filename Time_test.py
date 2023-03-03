import time
from datetime import datetime, timedelta
from time import sleep

for i in range(0, 1000):
    sleep(10)
    start_time = datetime.now()
    time_limit = timedelta(minutes=1)
    end_time = datetime.now()
    elapsed_time = end_time-start_time
    if elapsed_time > time_limit:
        print("time is over")
        break
