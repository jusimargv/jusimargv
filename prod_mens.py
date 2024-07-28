from confluent_kafka import Producer

# Configuração do produtor
conf = {"bootstrap.servers": "localhost:9092"}

producer = Producer(**conf)


# Função de callback para confirmação de entrega
def delivery_report(err, msg):
    if err is not None:
        print(f"Erro: {err}")
    else:
        print(f"Mensagem entregue: {msg.topic()} [{msg.partition()}]")


# Produzir mensagens
topic = "meu_projeto"
for i in range(10):
    producer.produce(topic, key=str(i), value=f"Mensagem {i}", callback=delivery_report)
    producer.poll(0)

producer.flush()
