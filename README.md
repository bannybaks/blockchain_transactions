# Bitcoin from Blockchair


## Описание:

Бэкенд-приложение по загрузке данных по bitcoin транзакциям в графовую БД neo4j.



- Разработана структура хранения данных по транзакциям и адресам в терминах графовой БД Neo4j;  

- Подготовлен пайплайн загрузки данных (чтение архивов, преобразование данных к необходимому формату, загрузка данных в графовую БД);  

- *[На рассмотрении]* Интерфейс для просмотра транзакций по введённому адресу через веб-приложение (FastAPI + Swagger);  

- *[На рассмотрении]*  Прогон данных через пайплан загрузки по времени (на сайте blockchair архивы за прошедший день появляются ежедневно в 23:59:59).

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

    
    Address:
        address: block address
        ...
```


