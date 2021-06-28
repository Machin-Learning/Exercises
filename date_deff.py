import datetime
date1 = datetime.date(2011,1,1)
date2 = datetime.date(2021,1,1)
def date_diff(Date1,Date2):
    delta = Date2 - Date1
    return (delta)

print(date_diff(date1,date2))
