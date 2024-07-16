## NOTE

1.I put in a significant amount of effort to Dockerize the project but unfortunately, I was not successful. Nonetheless, I am sharing the Dockerfile files I worked on below. When I couldn't get them to work using Dockerfiles, I followed the manual instructions outlined in the README and was able to accomplish the task this way.

Here are the Dockerfile files I used while attempting to Dockerize:

<--- insert file directory and Dockerfile files here --->

2.After pulling the project to your local environment, please delete the "output_data.json" file. I included this file as an example of the result generated when I ran the project myself. You will need to delete it, as following the specified steps will generate the file on your end as well.

# Web Scraping and Kafka Integration Project

This project demonstrates how to scrape data from a web page, send it to a Kafka topic, save the data from Kafka to a file, and provide a REST API to access the saved data. The project is divided into three main parts:

**1.Scraping and Sending Data to Kafka**

**2.Consuming Data from Kafka and Saving to a File**

**3.Serving the Data via a REST API**

## 1. Scraping and Sending Data to Kafka
In this section, we use Python to scrape product data from a webpage and send the data to a Kafka topic. Below, I explain the **untitled1.py** file that performs this task.

Scrape Data:

- We use the requests library to fetch the content of the web page.
- The BeautifulSoup library is used to parse the HTML and extract product details such as name, price, and stock status.

Send Data to Kafka:

- A Kafka producer is configured using the kafka-python library.
- The extracted data is sent to a Kafka topic named test_topic at 1-second intervals.

## 2. Consuming Data from Kafka and Saving to a File
This part involves consuming the data from the Kafka topic and saving it to a JSON file. Below, I explain the **untitled2.py** file that performs this task.

Configure Kafka Consumer:

- The kafka-python library is used to configure a Kafka consumer.

Consume and Save Data:

- The consumer reads messages from the test_topic.
- The data is saved to a file named output_data.json.

## 3. Serving the Data via a REST API
This part sets up a simple REST API using Flask to serve the data saved in the JSON file. Below, I explain the **untitled3.py** file that performs this task.

Set Up Flask Application:

- The Flask framework is used to create a simple web server.
- The server provides an endpoint /data to return the data from the output_data.json file.


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

Create a virtual environment to isolate the project's dependencies and activate it.
```
python -m venv myenv
myenv\Scripts\activate
```

**3.Start Kafka and Zookeeper:**

Use Docker Compose to start Kafka and Zookeeper. This step ensures that both services are up and running, which are required for messaging in this project.
```
docker-compose up -d
```
Verify that the Kafka and Zookeeper containers are running.You should see containers for both Kafka and Zookeeper listed.
```
docker ps
```
Replace "<Kafka_Container_ID>" with the actual container ID for Kafka, which you can get from the "docker ps" command.
```
docker exec -it <Kafka_Container_ID> bash
```
Inside the Kafka container, create a topic named test_topic:This command creates a Kafka topic with the specified configurations.
```
kafka-topics.sh --create --topic test_topic --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1
```

**4.Install Required Python Packages:**

Install the required Python packages in your virtual environment. These packages include libraries for web scraping, Kafka integration, and setting up the Flask web server.
```
pip install requests pandas
pip install beautifulsoup4
pip install kafka-python
pip install kafka-python-ng
pip install flask
```

## Running the Scripts

After setting up your environment and ensuring Kafka is running, you can execute the Python scripts in the following order:

**1.Scrape Data and Send to Kafka:**
Run the script to scrape data from the web page and send it to the Kafka topic test_topic.
```
python untitled1.py
```
As an example, I share with you the result I get when I run this file

![Ekran görüntüsü 2024-07-16 190147](https://github.com/user-attachments/assets/16f6b577-0a83-4d06-808d-09259901fc49)


**2.Consume Data from Kafka and Save to File:**
Run the script to consume data from the Kafka topic and save it to output_data.json.
```
python untitled2.py
```
As an example, I share with you the result I get when I run this file

![Ekran görüntüsü 2024-07-16 190215](https://github.com/user-attachments/assets/6f202355-5702-4ff7-91c9-f6494e4a9be2)


**3.Start the REST API Service:**
Run the Flask application to serve the data via a REST API.
```
python untitled3.py
```
After successfully running your Flask application, you will see a message like the one below in the terminal:
```
Running on http://127.0.0.1:5000
```

You can view your Flask application by pasting this URL into your browser. To see a specific data output of your app, you need to add /data to the end of the URL. For example, enter the following address in your browser:
```
http://127.0.0.1:5000/data
```
When you go to this address, you will see the data output generated by your application.

![Ekran görüntüsü 2024-07-16 190451](https://github.com/user-attachments/assets/183743a1-731f-44a8-9555-ffbc3023d2fd)



