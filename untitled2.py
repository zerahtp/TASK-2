from kafka import KafkaConsumer
import json

# Kafka Consumer'ını yapılandırma
consumer = KafkaConsumer(
    'test_topic',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Belirli sayıda mesaj alma
max_messages = 10  # Alınacak maksimum mesaj sayısı
messages = []

try:
    for i, message in enumerate(consumer):
        print(f"Received: {message.value}")
        messages.append(message.value)
        if i + 1 >= max_messages:
            break
finally:
    # Verileri dosyaya yazma
    with open('output_data.json', 'w', encoding='utf-8') as f:
        json.dump(messages, f, ensure_ascii=False, indent=4)

    # Bağlantıyı kapatma
    consumer.close()
