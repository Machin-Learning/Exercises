import datetime
def leap_year(input_date):
    i = input_date
    if i.year%4==0 and i.year%100==0 and i.year%400==0:
        return ('Leap Year')
    else:
        return ('Non Leap Year')


i = datetime.date(2000,1,1)
print(leap_year(i))