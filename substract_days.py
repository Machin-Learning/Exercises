import datetime
import random

def subtract_days():
    chosen_date = datetime.date(random.randint(2000,10000),random.randint(1,12),random.randint(1,31))
    new_date = chosen_date - datetime.timedelta(days=5)
    return (chosen_date,new_date)

print(subtract_days())