from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from db.db_connection import get_db
from db.customer_db import CustomerInDB
from db.appointment_db import AppointmentInDB
from models.customer_models import CustomerIn, CustomerOut
from models.appointment_models import AppointmentIn, AppointmentOut

router = APIRouter()


@router.get("/customer/{customer_name}", response_model=CustomerOut)
async def get_customer(customer_name: str, db: Session = Depends(get_db)):
    customer_in_db = db.query(CustomerInDB).get(customer_name)
    if customer_in_db == None:
        raise HTTPException(status_code=404, detail="El cliente no existe")
    return customer_in_db
