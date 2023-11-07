import datetime
data_str = '06/11/2023 15:08:20'
data = datetime.datetime.strptime(date_str, '%d/%m/%Y $H:%M:%S')
print(data.day)
print(data.month)
print(data.year)