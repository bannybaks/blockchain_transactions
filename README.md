# Bitcoin from Blockchair


## Описание:

Бэкенд-приложение по загрузке данных по bitcoin транзакциям в графовую БД neo4j.


- **Разработана структура хранения данных в графовой БД Neo4j;**  

- **Подготовлен пайплайн загрузки данных (чтение архивов, преобразование данных к необходимому формату, загрузка данных в графовую БД). Загрузка данных из сети по расписанию в 00:00, либо вручную через командную строку в контейнере;**
    >**Attention!**  
    > при первом запуске сервиса до 00:00 требуется ручной запуск скрипта загрузки/выгрузки данных из командной строки контейнера: 
    `$ sudo docker exec <CONTAINER ID> python /app/load_data.py`;  

- **Интерфейс для просмотра списка транзакций и детальной информации по группе транзакций через веб-приложение посредством Swagger;**


>**Note**  
> архивы с данными - https://gz.blockchair.com/bitcoin/transactions/;  


**Структура БД:**
```Markdown
    Transaction:
        hash: Block hash
        time: Block time (UTC)
        size: Block size in bytes
        weight: Block weight in weight units
        version: Version field
        lock_time: Lock time — can be either a block height, or a unix timestamp
        is_coinbase: Is it a coinbase (generating new coins) transaction? (For such a transaction input_count is equal to 1 and means there's a synthetic coinbase input)
        has_witness: Is there a witness part in the transaction (using SegWit)?
        input_count: Number of inputs
        output_count: Number of outputs
        input_total: Input value in satoshi
        input_total_usd: Input value in USD
        output_total: Output value in satoshi
        output_total_usd: Total output value in USD
        fee: Fee in satoshi
        fee_usd: Fee in USD
        fee_per_kb: Fee per kilobyte (1000 bytes) of data in satoshi
        fee_per_kb_usd: Fee for kilobyte of data in USD	
        fee_per_kwu: Fee for 1000 weight units of data in satoshi
        fee_per_kwu_usd: Fee for 1000 weight units of data in USD
        cdd_total: The number of destroyed coindays
```

#### Запуск сервиса
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


### Документация

Доступна после запуска сервиса:

**swagger** - `http://<localhost OR ip remote host mashine>:8000/docs/`  
**redoc** - `http://<localhost OR ip remote host mashine>:8000/redoc/`
