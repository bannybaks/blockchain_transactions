from typing import List, Dict

from fastapi import APIRouter, HTTPException, Depends

from config.db_config import connect_to_database
from models.base_models import TransactionID, TrnsactionArchive
from utils.db_helper import get_archives, get_transaction_by_id


router = APIRouter()


@router.get(
    "/transactions/",
    response_model=list[TrnsactionArchive],
    summary="Get transactions from database",
    description=(
        "Returns a list of transaction summaries grouped "
        "by transaction_id"
    )
)
async def get_transactions():
    """Получить список транзакций, уже занесенных в базу данных."""

    try:
        driver = connect_to_database()
        archives = get_archives(driver)
        if archives:
            return archives
        else:
            return {"detail": "Список транзакций пуст"}
    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Ошибка при получении списка транзакций: {error}"
        )

@router.get(
    "/transaction/{transaction_id}",
    response_model=list[TransactionID],
    summary="Get extended information about changing a transaction group",
    description=(
        "Returns detailed information with transaction_id, amount, "
        "date, hash, time, size, cdd_total data about each transaction "
        "in the group"
    )
)
async def get_transaction(
    transaction_id: int,
    driver = Depends(connect_to_database)
):
    """Получить информацию об определенной группе транзакций."""

    try:
        transaction = get_transaction_by_id(driver, transaction_id)
        if transaction:
            return transaction
        else:
            raise HTTPException(
                status_code=404,
                detail="Транзакция не найдена"
            )
        raise NotImplementedError(
            "Метод для получения транзакции из базы данных еще не реализован"
        )
    except HTTPException as http_exception:
        raise http_exception
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Ошибка при получении транзакции: {str(e)}"
        )


@router.get("/database/status")
async def check_database_status(driver = Depends(connect_to_database)):
    """Проверка соединения с базой"""

    try:
        driver.verify_connectivity()
        return {
            "status": "success",
            "message": "Подключение к базе данных установлено"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Ошибка при подключении к базе данных: {str(e)}"
    }
