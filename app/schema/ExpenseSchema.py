from pydantic import BaseModel

class ExpenseModel(BaseModel):
    name : str
    amount:float
    category : str

class ResponseModel(BaseModel):
    id:int
    name : str
    amount: float
    category : str
    