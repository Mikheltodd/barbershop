from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from api.db.db_connection import get_db
from api.db.service_order_details_db import ServiceOrderDetailInDB
from api.models.service_order_detail_models import ServiceOrderDetailIn, ServiceOrderDetailOut

router = APIRouter()


@router.get("/detail/{detail_id}", response_model=ServiceOrderDetailOut)
async def get_detail(detail_id: int, db: Session = Depends(get_db)):
    detail_in_db = db.query(ServiceOrderDetailIn).get(detail_id)
    if detail_in_db == None:
        raise HTTPException(status_code=404, detail="Detalle no encontrado")
    return detail_in_db


@router.post("/detail/create/")
async def new_service_order_detail(order_service_detail_in: ServiceOrderDetailIn, db: Session = Depends(get_db)):

    service_order_detail_in_db = ServiceOrderDetailInDB(
        **order_service_detail_in.dict())

    db.add(service_order_detail_in_db)
    db.commit()
    db.refresh(service_order_detail_in_db)

    return {"Mensaje": "Detalle creado correctamente."}
