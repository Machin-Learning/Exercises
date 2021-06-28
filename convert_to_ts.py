import datetime,time
date = 'Jan 01 2011 08:36:40 PM'
date = datetime.datetime.strptime(date, "%b %d %Y %H:%M:%S %p")
# dtt = date.timetuple()
# ts = time.mktime(dtt)
# print(ts)
# print(datetime.datetime.utcfromtimestamp(1293851200.0))
# time_str = '13:55:26'
# time_object = datetime.datetime.strptime(time_str, '%H:%M:%S').time()
# print(type(time_object))
# print(time_object)


# from datetime import datetime
# from calendar import timegm
# # tm = '1970-01-01 06:00:00 +0500'
# # fmt = '%Y-%m-%d %H:%M:%S %z'
# print(timegm(datetime.strptime(date, "%b %d %Y %H:%M:%S %p").utctimetuple()))

import arrow
print(arrow.get(date).timestamp())