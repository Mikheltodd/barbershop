from pydantic import BaseModel

class ServiceOrderDetailIn(BaseModel):
    service_quantity = int
    service_amount = int

class ServiceOrderDetailOut(BaseModel):
    detail_id = int
    service_id = int
    service_quantity = int
    service_amount = int
    order_id = int
    employee_id = int

    class Config:
        orm_mode = True