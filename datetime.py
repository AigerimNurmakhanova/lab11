'''
import datetime

dt_now = datetime.datetime.now()
print(dt_now)
'''

'''
from datetime import date

current_date = date.today()
print(current_date)
'''

'''
import datetime

current_date_time = datetime.datetime.now()
current_time = current_date_time.time()
print(current_time)
'''

'''
import datetime

timeobj= datetime.time(8,48,45)
print(timeobj)

ответ: 08:48:45
'''

'''
#timedelta прошлое
import datetime

past_date = datetime.datetime.today() - datetime.timedelta(days=14) 
print(past_date)
'''