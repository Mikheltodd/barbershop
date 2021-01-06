from sqlalchemy import Column, Integer, String
from db.db_connection import Base, engine

class ServiceordesInDB(Base):
    __tablename__ = "serviceorders"
    order_id = Colum(Integer,primary_key=true,autincremet=true)
    order_date = Colum(String)
    order_time = Colum(String)

Base.metadata.create_all(bind=engine)
