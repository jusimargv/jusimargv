from confluent_kafka import Consumer, KafkaException

# Configuração do consumidor
conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'meu_grupo',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(**conf)

# Assinar o tópico
consumer.subscribe(['meu_projeto'])

try:
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                raise KafkaException(msg.error())
        print(f'Recebido: {msg.value().decode("utf-8")}')
except KeyboardInterrupt:
    pass
finally:
    consumer.close()
