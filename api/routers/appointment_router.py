from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from db.db_connection import get_db
from db.customers_db import CustomerInDB
from db.appointments_db import AppointmentInDB
from models.customer_models import CustomerIn, CustomerOut
from models.appointment_models import AppointmentIn, AppointmentOut

router = APIRouter()


@router.get("/customer/booking/", response_model=AppointmentOut)
async def book_appointment(appointment_in: AppointmentIn, db: Session = Depends(get_db)):
    customer_in_db = db.query(CustomerInDB).get(appointment_in.customer)
    if customer_in_db == None:
        raise HTTPException(status_code=404, detail="El cliente no existe")
    appointment_in_db = AppointmentInDB(**appointment_in.dict())
    db.add(appointment_in_db)
    db.commit()
    db.refresh(appointment_in_db)

    return customer_in_db
