from datetime import datetime
from typing import List, Dict, Optional, Any

from fastapi.responses import JSONResponse
from neo4j import GraphDatabase

from models.base_models import TransactionID


def get_archives(driver: GraphDatabase) -> JSONResponse:
    """Список архивов, уже занесенных в базу данных."""

    try:
        session = driver.session()
        result = session.run(
            "MATCH (a:Transaction) RETURN a.transaction_id AS transaction_id, "
            "count(a) AS count"
        )

        transactions = [
            {
                "transaction_id": record["transaction_id"],
                "count": record["count"]
            } for record in result
        ]

    except Exception as error:
        print(f"An error occurred while fetching archives: {error}")

    response_content = {
        "transactions": transactions,
        "count": len(transactions)
    }

    return JSONResponse(content=response_content)


def get_transaction_by_id(
    driver: GraphDatabase,
    transaction_id: int
) -> JSONResponse:
    """10 транзакций из базы данных по идентификатору."""

    query = (
        "MATCH (t:Transaction {transaction_id: $transaction_id}) "
        "RETURN t LIMIT 10"
    )
    session = driver.session()
    result = session.run(query, transaction_id=transaction_id)
    transactions = []
    for record in result:
        transaction_data = record["t"]
        transaction = {
            "transaction_id": transaction_data.get("transaction_id"),
            "amount": transaction_data.get("amount"),
            "date": transaction_data.get("date"),
            "hash": transaction_data.get("hash"),
            "time": transaction_data.get("time"),
            "size": transaction_data.get("size"),
            "cdd_total": transaction_data.get("cdd_total"),
        }
        transactions.append(transaction)
    
    response_content = {
        "transactions": transactions,
        "count": len(transactions)
    }
    return JSONResponse(content=response_content)


def load_data_to_database(driver: GraphDatabase, data_file_path: str):
    """Выгрузка данных из файла в БД."""

    try:
        with open(data_file_path, 'r') as file:
            next(file)
            session = driver.session()
            for line in file:
                transaction_data = line.strip().split('\t')
                transaction_args = {}
                for field, value in zip(
                    TransactionID.__fields__, transaction_data
                ):
                    if TransactionID.__fields__[field].type_() is bool:
                        value = value.lower() == 'true'
                    transaction_args[field] = (
                        TransactionID.__fields__[field].type_(value)
                    )
                transaction = TransactionID(**transaction_args)
                session.run(
                    "CREATE (t:Transaction $props)",
                    props=transaction.dict()
                )

        print("Данные успешно загружены в базу данных Neo4j")
    except Exception as e:
        print(f"Ошибка при загрузке данных в базу данных Neo4j: {e}")
