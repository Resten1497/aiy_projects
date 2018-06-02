from datetime import datetime
import parser



now = datetime.now()
weekday=now.weekday()
ymd=str(now.year)+"."+now.strftime('%m')+"."+str(now.day)
data=parser.get_diet(2,ymd,weekday)
print(data)