<a id="anchor"></a>
<div align=center>

  # BitcoinGraphLoader

  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
  ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
  ![FastAPI](https://img.shields.io/badge/fastapi-8A2BE2.svg?style=for-the-badge&logo=FastAPI&logoColor=white)
  ![Neo4j](https://img.shields.io/badge/Neo4j-%23009639.svg?style=for-the-badge&logo=Neo4j&logoColor=white)
</div>


1. [Описание](#описание)
2. [Установка и использование](#установка-и-использование)
3. [Использование](#использование)
4. [Документация](#документация)
5. [Автор](#автор)

## Описание:

Бэкенд-приложение по загрузке данных bitcoin транзакций в графовую БД neo4j каждые 24 часа за предыдущие сутки.

#### **Как это работает:**

*Загрузка данных* -
Через подготовленый пайплайн загрузки данных каждые 24 часа происходит загрузка данных по транзакциям Bitcoin с ресурса https://blockchair.com/dumps

*Чтение архивов, преобразование данных к необходимому формату* -
Далее скачанный архив по завершению загрузки разархивируется в корень

*Выгрузка данных* - По завершению работы с архивом данные заливаются в базу

>**Note:**  
> *При первом запуске сервиса до 00:00 требуется ручной запуск скрипта загрузки/выгрузки данных из командной строки контейнера:*  
`$ sudo docker exec <CONTAINER ID> python /app/load_data.py` 


## Установка и использование

1. Склонировать репозиторий в рабочее пространство:
```bash
git clone git@github.com:bannybaks/blockchain_transactions.git
```
2. В корневой дирректории проекта создать файл с переменными окружения `.env` и наполнить его по `.env.example`:
```
URL_DB='neo4j://localhost:7687'    
USER_DB=<your username>
PASSWORD_DB=<your password>
```
3. Из корневой дирректории запустить сборку приложения:
```bash
sudo docker-compose up -d
```

## Документация

Доступна после запуска сервиса:

**swagger** - `http://<localhost OR ip remote host mashine>:8000/docs/`  
**redoc** - `http://<localhost OR ip remote host mashine>:8000/redoc/`

## Автор

**Павел Смирнов**

[![Telegram Badge](https://img.shields.io/badge/-B1kas-blue?style=social&logo=telegram&link=https://t.me/B1kas)](https://t.me/B1kas) [![Yamail Badge](https://img.shields.io/badge/baksbannysmirnov@yandex.ru-FFCC00?style=flat&logo=ycombinator&logoColor=red&link=mailto:baksbannysmirnov@yandex.ru)](mailto:baksbannysmirnov@yandex.ru)
