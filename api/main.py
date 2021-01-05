from fastapi import Depends, FastAPI
from routers.customer_router import router as router_customer
from routers.appointment_router import router as router_appointment
api = FastAPI()
api.include_router(router_customer)
api.include_router(router_appointment)
