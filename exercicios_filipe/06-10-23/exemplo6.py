import datetime
agora = datetime.datetime(2023, 11, 6, 15, 8, 20)
intervalo = datetime.timedelta(days=60)
#data_final = agora + intervalo
data_final = agora - intervalo
print(agora)
