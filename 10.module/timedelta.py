from datetime import datetime, timedelta

current_time=datetime.nonw()
print("현재 시간:",current_time)   

time_interval=timedelta(hours=1,minutes=30)
future_time=current_time+time_interval
print("1시간 30분 후의 시간:",future_time)