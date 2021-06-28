import datetime
def calculate_dates(input_date):
    prev_day =  input_date - datetime.timedelta(days = 1)
    next_day =  input_date + datetime.timedelta(days = 1)
    return (prev_day,input_date,next_day)


# print((datetime.date(2020,12,31) + datetime.timedelta(days=1)).day)
print(calculate_dates(datetime.date(2020,12,31)))