from enum import Enum
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Session
import Main

Base = Main.Base

class TransactionType(Enum):
    SALE = 1
    RETURN = 2
    STOCKPURCHASE = 3
    OTHER = 4

class Transaction(Base):

    __tablename__ = "Transaction"

    _transactionId = Column(Integer(), primary_key=True, autoincrement=True)
    _itemId = Column(Integer(), ForeignKey("Item._itemId"))
    _timestamp = Column(String(200))
    _amount = Column(Integer())
    _transactionType = Column(Integer())

    def AddToDatabase(self, session: Session):
        session.add(Transaction, self)
        session.commit

def Setup():
    Base.metadata.create_all(Main.engine)