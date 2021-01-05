from pydantic import BaseModel
from datetime import datetime


class AppointmentIn(BaseModel):
    appointment_datetime: datetime
    appointment_status: str
    customer: int


class AppointmentOut(BaseModel):
    id: int
    appointment_datetime: datetime
    appointment_status: str
    customer: int

    class Config:
        orm_mode = True
