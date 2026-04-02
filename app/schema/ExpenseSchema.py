from pydantic import BaseModel

class ExpenseModel(BaseModel):
    name = str
    amount=float
    category = str

class ResponseModel(BaseModel):
    expense_id:int
    name = str
    amount= float
    category = str
    