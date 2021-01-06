from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from db.db_connection import Base, engine

class BillsInDb(Base):
    __tablename__ = "bills"
    bill_id = Colum(Integer, primary_key=true, autoincrement=true)
    bill_date = Colum(DateTime, default=datetime.datetime.utcnow)
    bill_discount = Colum(Integer)
    discount = Column(Integer, ForeignKey("discounts.discount_id"))
    customer = Column(Integer, ForeignKey("customers.customer_id"))
    order = Column(Integer, ForeignKey("sericeorders.order_id"))

Base.metadata.create_all(bind=engine)

