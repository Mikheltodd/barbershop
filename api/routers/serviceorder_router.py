from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from db.db_connection import get_db
from db.serviceorder_db import ServiceorderInDB
from models.serviceorder_models import ServiceorderIn, ServiceorderOut

router = APIRouter()

@router.get("/serviceorder/{serviceorder_id}", response_model=ServiceorderOut)
async def get_serviceorder(serviceorder_id: str, db: Session = Depends(get_db)):
    serviceorder_in_db = db.query(ServiceorderInDB).get(serviceorder_id)
    if serviceorder_in_db == None:
        raise HTTPException(status_code=404, detail="El id no existe")
    return serviceorder_in_db