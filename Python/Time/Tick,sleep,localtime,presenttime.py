#In python the time instanta are counted since 12 AM , 1st january 1970
#The function time() of the module the returns the total number of ticks spent since 12 AM, 1st january 1970
#A tick can be as the smallest unit to measure  the time

import time
print(time.time())

print(time.localtime(time.time()))


time.sleep(1)
#in second

#Output
"""
1590693082.6978915
#in the form of tuple
time.struct_time(tm_year=2020, tm_mon=5, tm_mday=29,
tm_hour=0, tm_min=41, tm_sec=22, tm_wday=4, tm_yday=150, tm_isdst=0)

"""

import datetime
print(datetime.datetime.now())

# Output : 2020-05-29 00:45:34.018003
