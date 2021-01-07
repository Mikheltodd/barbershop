from sqlalchemy import Column, Integer, String
from db.db_connection import Base, engine

class ServiceordeInDB(Base):
    __tablename__ = "serviceorders"
    order_id = Colum(Integer,primary_key=true,autincremet=true)
    order_date = Colum(DateTime, default= datetime.datetime.utcnow)
    order_time = Colum(String)

Base.metadata.create_all(bind=engine)
