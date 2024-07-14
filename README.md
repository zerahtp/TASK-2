# Web Scraping and Kafka Integration Project
This project demonstrates how to scrape data from a web page, send it to a Kafka topic, save the data from Kafka to a file, and provide a REST API to access the saved data. The project is divided into three main parts: scraping and sending data to Kafka, consuming data from Kafka and saving to a file, and serving the data via a REST API.

## Prerequisites
Before running the project, ensure you have the following installed:

- Python 3.7+
- Docker
- Docker Compose
- Kafka

## Project Structure
- **docker-compose.yml:** Docker Compose file to set up Kafka and Zookeeper.
- **untitled1.py:** Script to scrape data from the web page and send it to a Kafka topic.
- **untitled2.py:** Script to consume data from the Kafka topic and save it to a JSON file.
- **untitled3.py:** Flask application to serve the saved data via a REST API.
- **output_data.json:** The file where the consumed Kafka data is stored.

## Setup Instructions
**1.Clone the Repository:**
```
git clone <repository-url>
cd <repository-directory>
```

**2.Set Up Virtual Environment:**
```
python -m venv myenv
myenv\Scripts\activate
```

**3.Start Kafka and Zookeeper:**
```
docker-compose up -d
docker ps
docker exec -it <Kafka_Container_ID> bash
kafka-topics.sh --create --topic test_topic --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1
```

**4.Install Required Python Packages:**
```
pip install requests pandas
pip install beautifulsoup4
pip install kafka-python
```

## Running the Scripts
**1.Scrape Data and Send to Kafka:**
Run the script to scrape data from the web page and send it to the Kafka topic test_topic.
```
python untitled1.py
```

**2.Consume Data from Kafka and Save to File:**
Run the script to consume data from the Kafka topic and save it to output_data.json.
```
python untitled2.py
```

**3.Start the REST API Service:**
Run the Flask application to serve the data via a REST API.
```
python untitled3.py
```


