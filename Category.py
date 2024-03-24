from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
import Main

Base = Main.Base

class Category(Base):

    __tablename__ = "Category"

    _categoryId = Column(Integer(), primary_key=True, autoincrement=True)
    _name = Column(String(200), unique=True)

    @staticmethod
    def GetFromDatabase(session: Session, categoryId: int):
        return session.get(Category, categoryId)
    
    @staticmethod
    def GetFromDatabaseByName(session: Session, nameCheck: str):
        return session.query(Category._name).filter_by(name=nameCheck).first()

    @staticmethod
    def GetAllFromDatabase(session: Session):
        return session.query(Category).all()

    def AddToDatabase(self, session: Session):
        session.add(Category, self)
        session.commit()
    
    @staticmethod
    def RemoveFromDatabase(session: Session, categoryId: int):
        session.delete(Category, categoryId)
        session.commit()

    @staticmethod
    def ChangeInDatabase(session: Session, categoryId: str, newName):
        category = Category.GetFromDatabase(session, categoryId)
        category.UpdateName(newName)
        session.commit()

    def UpdateName(self, newName: str):
        self._name = newName

def Setup():
    Base.metadata.create_all(Main.engine)