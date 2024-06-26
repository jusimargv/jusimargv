from datetime import datetime, timezone, timedelta
import pytz

data = datetime.now(pytz.timezone("Europe/Oslo"))
data2 = datetime.now(pytz.timezone("America/New_York"))
data3 = datetime.now(pytz.timezone("America/Sao_Paulo"))
data_Sao_Paulo = datetime.now(timezone(timedelta(hours= -3)))
print(data3)
print(data)
print(data2)
print(data_Sao_Paulo)