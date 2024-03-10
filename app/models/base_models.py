from typing import Dict, Optional


from pydantic import BaseModel


class TransactionID(BaseModel):
    transaction_id: int
    amount: int
    date: str
    hash: str
    time: str
    size: int
    weight: int
    version: int
    lock_time: int
    is_coinbase: bool
    has_witness: bool
    input_count: int
    output_count: int
    input_total: int
    input_total_usd: float
    output_total: int
    output_total_usd: float
    fee: int
    fee_usd: float
    fee_per_kb: float
    fee_per_kb_usd: float
    fee_per_kwu: float
    fee_per_kwu_usd: float
    cdd_total: float

    class Config:
        schema_extra = {
            "example": {
                "transaction_id": 1,
                "amount": 1000,
                "date": "2024-03-07 00:05:57",
                "hash": "hash_value",
                "time": "00:05:57",
                "size": 100,
                "weight": 200,
                "version": 1,
                "lock_time": 0,
                "is_coinbase": False,
                "has_witness": False,
                "input_count": 2,
                "output_count": 3,
                "input_total": 2000,
                "input_total_usd": 20.0,
                "output_total": 1500,
                "output_total_usd": 15.0,
                "fee": 500,
                "fee_usd": 5.0,
                "fee_per_kb": 5.0,
                "fee_per_kb_usd": 0.5,
                "fee_per_kwu": 10.0,
                "fee_per_kwu_usd": 1.0,
                "cdd_total": 100.0
            }
        }


class TrnsactionArchive(BaseModel):
    transaction_id: int
    count: int

    class Config:
        schema_extra = {
            "example": {
                "transaction_id": 1,
                "count": 1000,
            }
        }
