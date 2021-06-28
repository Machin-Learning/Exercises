import datetime
def check_date(year,month,day):
    cd = True
    try:
        date = datetime.date(year,month,day)
        cd =  True
    except ValueError:
        cd = False
    
    return (cd)