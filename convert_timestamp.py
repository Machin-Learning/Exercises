import datetime
def convert_timestamp(unix_timestamp):
    date = datetime.datetime.utcfromtimestamp(unix_timestamp)
    return date

print(convert_timestamp(1293851200.0))