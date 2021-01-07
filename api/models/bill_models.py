from pydantic import BaseModel
from datetime import datetime

class BillsIn(BaseModel):
    bill_date: datetime
    bill_Total: int 
    bill_discount: int 
    discount: int
    customer: int
    order: int

class BillOut(BaseModel):
    id:int
    bill_date: datetime
    bill_Total: int 
    bill_discount: int 
    discount: int
    customer: int
    order: int

    class config:
        orm_mode = True
