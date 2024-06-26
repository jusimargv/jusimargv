from datetime import datetime, timedelta, date

tipo_carro    = input("Defina o Tamnho do Carro em P, M, G:") # P,M,G
tempo_pequeno = 30
tempo_medio   = 45
tempo_grande  = 60
data_atual    = datetime.now()
 
if tipo_carro == "P":
    data_estimada =data_atual + timedelta(minutes=tempo_pequeno)
    print(f"O Carro chegou: {data_atual} e ficará pronto às {data_estimada}")
    


elif tipo_carro == "M":
    data_estimada =data_atual + timedelta(minutes=tempo_medio)
    print(f"O Carro chegou: {data_atual} e ficará pronto às {data_estimada}")


else:
   data_estimada =data_atual + timedelta(minutes=tempo_grande)
   print(f"O Carro chegou: {data_atual} e ficará pronto às {data_estimada}")
   
   
print(date.today() - timedelta(days=1))

resultado = datetime(2023, 7, 25, 10, 19, 20) - timedelta(hours=1)
print(resultado.time())

print(datetime.now().date())
   