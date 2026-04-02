from app.database import Base
from sqlalchemy import Column, String, Integer, Float

class Expense(Base):
    __tablename__ = "expense"
    id=(Column(Integer, primary_key=True, unique=True, index=True))
    name=Column(String)
    amount = Column(Float)
    category = Column(String)

