from dataclasses import dataclass
from datetime import datetime
import enum


class TransactionType(str, enum.Enum):
    BUY = "BUY"
    SELL = "SELL"
    GAS = "GAS"
    UNRECOGNIZED = "UNRECOGNIZED"


@dataclass
class Transaction:
    volume: float
    hash: str
    datetime: datetime
    price: float
    total_value: float
    type: TransactionType
