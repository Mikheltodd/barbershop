from pydantic import BaseModel
from datetime import datetime


class AppointmentIn(BaseModel):
    appointment_datetime: datetime
    appointment_status: str
    appointment_customer_id: int


class AppointmentOut(BaseModel):
    appointment_id: int
    appointment_datetime: datetime
    appointment_status: str
    appointment_customer_id: int

    class Config:
        orm_mode = True
