from fastapi import Depends, FastAPI
# from routers.appointment_detail_router import router as router_appointment_detail
from routers.appointment_router import router as router_appointment
# from routers.bill_router import router as router_bill
from routers.category_router import router as router_category
from routers.customer_router import router as router_customer
from routers.discount_router import router as router_discount
# from routers.employee_router import router as router_employee
# from routers.position_router import router as router_position
# from routers.discount_router import router as router_discount
from routers.employee_router import router as router_employee
from routers.position_router import router as router_position
# from routers.service_order_detail_router import router as router_service_order_detail
from routers.service_order_router import router as router_service_order
from routers.service_router import router as router_service

api = FastAPI()

# api.include_router(router_appointment_detail)
api.include_router(router_appointment)
# api.include_router(router_bill)
api.include_router(router_category)
api.include_router(router_customer)
# api.include_router(router_discount)
api.include_router(router_employee)
# api.include_router(router_position)
api.include_router(router_discount)
api.include_router(router_position)
# api.include_router(router_employee)

# api.include_router(router_service_order_detail)
api.include_router(router_service_order)
api.include_router(router_service)
