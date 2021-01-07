from pydantic import BaseModel
from datetime import datetime

class ServiceordersIn(BaseModel):
    order_date: datetime
    order_time: str

class ServiceordersOut(BaseModel):
    id: int
    order_date: datetime
    order_time: str

    class Config:
        orm_mode= True
        