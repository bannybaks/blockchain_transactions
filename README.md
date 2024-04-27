<a id="anchor"></a>
<div align=center>

   # BitcoinGraphLoader

   ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
   ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
   ![FastAPI](https://img.shields.io/badge/fastapi-8A2BE2.svg?style=for-the-badge&logo=FastAPI&logoColor=white)
   ![Neo4j](https://img.shields.io/badge/Neo4j-%23009639.svg?style=for-the-badge&logo=Neo4j&logoColor=white)
</div>


1. [Description](#Description)
2. [Installation and use](#Installation-and-use)
3. [Documentation](#documentation)
4. [Author](#author)

## Description:

Backend application for loading bitcoin transaction data into the neo4j graph database every 24 hours for the previous day.

#### **How ​​it works:**

*Loading data* -
Through a prepared data download pipeline, data on Bitcoin transactions is downloaded every 24 hours from the resource https://blockchair.com/dumps

*Reading archives, converting data to the required format* -
Next, the downloaded archive will be unzipped to the root after the download is complete.

*Data upload* - Upon completion of working with the archive, the data is uploaded to the database

>**Note:**
> *When the service is started for the first time before 00:00, a manual launch of the data loading/unloading script from the container command line is required:*
`$ sudo docker exec <CONTAINER ID> python /app/load_data.py`


## Installation and use

1. Clone the repository into the workspace:
```bash
git clone git@github.com:bannybaks/blockchain_transactions.git
```
2. In the root directory of the project, create a file with environment variables `.env` and fill it with `.env.example`:
```
URL_DB='neo4j://localhost:7687'
USER_DB=<your username>
PASSWORD_DB=<your password>
```
3. Start building the application from the root directory:
```bash
sudo docker-compose up -d
```

## Documentation

Available after starting the service:

**swagger** - `http://<localhost OR ip remote host machine>:8000/docs/`
**redoc** - `http://<localhost OR ip remote host machine>:8000/redoc/`

## Author

**Pavel Smirnov**

[![Telegram Badge](https://img.shields.io/badge/-B1kas-blue?style=social&logo=telegram&link=https://t.me/B1kas)](https://t.me/ B1kas) [![Yamail Badge](https://img.shields.io/badge/baksbannysmirnov@yandex.ru-FFCC00?style=flat&logo=ycombinator&logoColor=red&link=mailto:baksbannysmirnov@yandex.ru)](mailto:baksbannysmirnov @yandex.ru)
