import time
import calendar

class Time_Date:
    current_local_time = time.localtime(time.time())
    def current_time(self):
        localtime = time.asctime(self.current_local_time)
        return localtime
    def current_month_calender(self):
        month = self.current_local_time.tm_mon
        year = self.current_local_time.tm_year
        mycalendar = calendar.month(year,month)
        return mycalendar
    def sleep(self,time_for_sleep=2):
        time.sleep(time_for_sleep)
    def greet_main(self):
        h = self.current_local_time.tm_hour
        m = self.current_local_time.tm_min
        if h in range(4,12):
            return 'good morning'
        elif h in range(12,16):
            return 'g noon'
        elif h in range(16,21):
            return 'g eve'
        else:
            return 'good night'

# o = Time_Date()
# print(o.greet_main())