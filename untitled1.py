import requests
from bs4 import BeautifulSoup
from kafka import KafkaProducer
import json
import time

# Web sayfasından veri çekme
base_url = "https://scrapeme.live/shop/"
response = requests.get(base_url)
soup = BeautifulSoup(response.content, 'html.parser')

# Ürün detay sayfalarına gitmek için URL'leri çekme
product_urls = [a['href'] for a in soup.select('.product a.woocommerce-LoopProduct-link')]

# Kafka Producer'ını yapılandırma
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         api_version=(0, 11, 5),
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

products = []

# Her bir ürün sayfasına gidip detayları alma
for url in product_urls:
    product_response = requests.get(url)
    product_soup = BeautifulSoup(product_response.content, 'html.parser')
    
    try:
        name = product_soup.find("h1", class_="product_title").text
        price_element = product_soup.find("p", class_="price")
        if price_element:
            price_text = price_element.find("span", class_="woocommerce-Price-amount amount").text
            # Remove currency symbol and any other non-numeric characters except the decimal point
            price = ''.join(filter(lambda x: x.isdigit() or x == '.', price_text))
        else:
            price = "N/A"
        
        stock_status = product_soup.find("p", class_="stock").text if product_soup.find("p", class_="stock") else "In Stock"
        
        product = {
            "name": name,
            "price": price,
            "stock": stock_status
        }
        products.append(product)

        # Kafka konusuna gönderme
        producer.send('test_topic', value=product)
        print(f"Sent: {product}")
        time.sleep(1)  # Her veri arasında 1 saniye bekletme
    except AttributeError as e:
        print(f"Error processing product at {url}")
        print(e)

# Bağlantıyı kapatma
producer.flush()

print("Products:", products)
