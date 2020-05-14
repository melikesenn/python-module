#import datatime
from datetime import datetime

neyivar = dir(datetime)

now = datetime.now()
print(now.now())
xx = datetime.ctime(now) #daha ayrıntılı verir
xy = datetime.strftime(now,'%M')
print(xx)
print(xy)