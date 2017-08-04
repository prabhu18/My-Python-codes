import datetime



x  =  datetime.date.today() - datetime.datetime.strptime('2015-12-31', "%Y-%m-%d").date()
print type(x.days)