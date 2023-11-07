import datetime
formato = '%d/%m/%Y $H:%M:%S'
agora = datetime.datetime(2023, 11, 6, 15, 8, 40)
agora_str = agora.strftime(formato)
print(agora)
