from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Session
import Main
import Transaction

Base = Main.Base

class Item(Base):

    __tablename__ = "Item"

    _itemId = Column(Integer(), primary_key=True, autoincrement=True)
    _name = Column(String(200))
    _categoryId = Column(Integer(), ForeignKey("Category._categoryId"))
    _price = Column(Integer())
    _amountStored = Column(Integer())

    @staticmethod
    def GetFromDatabase(session: Session, itemId: int):
        return session.get(Item, itemId)
    
    @staticmethod
    def GetFromDatabaseByName(session: Session, nameCheck: str):
        return session.query(Item._name).filter_by(name=nameCheck).first()
    
    @staticmethod
    def GetFromDatabaseByCategory(session: Session, categoryId: int):
        return session.query(Item._categoryId).filter_by(name=categoryId).first()
    
    @staticmethod
    def GetAllFromDatabase(session: Session):
        return session.query(Item).all()

    def AddToDatabase(self, session: Session):
        session.add(Item, self)
        session.commit()

    @staticmethod
    def RemoveFromDatabase(session: Session, itemId: int):
        session.delete(Item, itemId)
        session.commit()

    @staticmethod
    def ChangeInDatabase(session: Session, itemId: int, newVal, updateType: int = 1):
        item = Item.GetFromDatabase(session, itemId)
        updateTypes = [item.UpdateName(), item.UpdateCategoryId(), item.UpdatePrice()]
        updateTypes[updateType](newVal)
        session.commit()

    def UpdateName(self, newName: str):
        self._name = newName

    def UpdateCategoryId(self, newCategoryId: int):
        self._categoryId = newCategoryId

    def UpdatePrice(self, newPrice: int):
        self._price = newPrice

    @staticmethod
    def ChangeStockAmount(session: Session, itemId: int, amountChange: int):
        item = Item.GetFromDatabase(session, itemId)
        if amountChange == 0:
            return
        elif amountChange < 0:
            if not item.HasStockAmount(abs(amountChange)):
                return
        item._amountStored += amountChange
        trans = Transaction(_itemId=itemId, _timestamp=0, _amount=amountChange, _transactionType=Transaction.TransactionType.OTHER)
        trans.AddToDatabase(session)
        session.commit()

    def HasStockAmount(self, stockAmount: int) -> bool:
        return self._amountStored >= stockAmount
    
def Setup():
    Base.metadata.create_all(Main.engine)