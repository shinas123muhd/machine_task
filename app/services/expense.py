from app.main import app
from app.schema.ExpenseSchema import ExpenseModel, ResponseModel
from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.database import get_db
from app.models.expense import Expense

@app.post('/expenses/',response_model=ResponseModel)
def post_expense(item: ExpenseModel, db: Session = Depends(get_db)):
    if not item:
        return HTTPException
    db_item = Expense(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
@app.get('/expenses', response_model=ResponseModel)
def get_expense(item: ExpenseModel, db: Session = Depends(get_db)):
    db_item = db.query(Expense).all()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item