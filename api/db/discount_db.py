from sqlalchemy import Column, Integer, String
from db.db_connection import Base, engine

class DiscountInDB(Base):
    __table__ = "discounts"
    discount_id = Colum(Integer, primary_key=true, autoincrement=true)
    discount_name = Colum(String)
    discount_value= Colum(Integer)

Base.metadata.create_all(bind=engine)
