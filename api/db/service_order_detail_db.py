from sqlalchemy import Column, Integer, String, ForeignKey
from db.db_connection import Base, engine

class ServiceOrderDetailInDB(Base):
    __tablename__ = "serviceOrderDetails"
    detail_id = Column(Integer, primary_key=True, autoincrement=True)
    service_id = Column(Integer, ForeignKey("services.service_id"))
    service_quantity = Column(Integer)
    service_amount = Column(Integer)
    order_id = Column(Integer, ForeignKey("serviceOrders.order_id"))
    employee_id = Column (Integer, ForeignKey("employees.employee_id"))

Base.metadata.create_all(bind=engine)

