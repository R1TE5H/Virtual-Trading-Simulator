from typing import TypedDict
from datetime import datetime 
from Stock import Stock

class TransactionDetails(TypedDict):
    stock: Stock
    shares: float  
    transaction_type: str
    time: str

class Transaction:
    def __init__(self, shares, transaction_type, stock):
        self.__stock = stock
        self.__shares = shares
        self.__transaction_type = transaction_type
        self.__time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def get_details(self) -> TransactionDetails:
        return {
            "stock": self.__stock,
            "shares": self.__shares,
            "transaction_type": self.__transaction_type,
            "time": self.__time
        }