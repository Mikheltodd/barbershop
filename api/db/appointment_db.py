from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
import datetime
from db.db_connection import Base, engine


class AppointmentInDB(Base):
    __tablename__ = "appointments"
    appointment_id = Column(Integer, primary_key=True, autoincrement=True)
    appointment_datetime = Column(DateTime, default=datetime.datetime.utcnow)
    appointment_status = Column(String)
    customer = Column(Integer, ForeignKey("customers.customer_id"))


Base.metadata.create_all(bind=engine)
