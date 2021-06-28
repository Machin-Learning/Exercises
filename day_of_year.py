import datetime
import random
def day_of_year():
    chosen_date = datetime.date(random.randint(2000,9000),random.randint(1,12),random.randint(1,31))
    day_of_the_year = str(chosen_date.timetuple().tm_yday)
    return chosen_date,day_of_the_year

date = datetime.date(8004,4,23)

print(day_of_year())