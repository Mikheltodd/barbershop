from fastapi import Depends, FastAPI
from routers.customer_router import router as router_customer
from routers.appointment_router import router as router_appointment
from routers.bill_router import router as router_bill
from routers.discount_router import router as router_discount 
from routers.serviceorder_router import router as router_serviceorder

api = FastAPI()

api.include_router(router_customer)
api.include_router(router_appointment)
api.include_router(router_bill)
api.include_router(router_discount)
api.include_router(router_serviceorder)
