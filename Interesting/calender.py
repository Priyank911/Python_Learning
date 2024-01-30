from calendar import month
from datetime import datetime

now = datetime.now()
y,m= now.year , now.month

print()
print(month(y,m))