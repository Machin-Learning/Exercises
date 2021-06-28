# import datetime    
# month, year = input('Enter the month & year: ').split()  
# result = True if datetime.datetime.strptime('13 '+' '+month+' '+year, '%d %m %Y').weekday()==4 else False
import datetime
def check_friday_13(yr,mon):
    result = True if datetime.datetime.strptime('13 '+' '+mon+' '+yr, '%d %m %Y').weekday()==4 else False
    day = datetime.datetime.strptime('13 '+' '+mon+' '+yr, '%d %m %Y').day()
    return datetime.date(yr,mon,day),result

print(check_friday_13(2020,3))