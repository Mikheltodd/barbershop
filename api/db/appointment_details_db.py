from sqlalchemy import Column, Integer, String
from db.db_connection import Base, engine


class AppointmentDetailInDB(Base):
    __tablename__ = "appointment_details"
    appointment_detail_id = Column(
        Integer, primary_key=True, autoincrement=True)
    appointment_detail_employee = Column(
        Integer, ForeignKey("categories.category_id"))
    appointment_detail_service = Column(
        Integer, ForeignKey("services.service_id"))
    appointment_detail_appointment = Column(
        Integer, ForeignKey("appointments.appointment_id"))


Base.metadata.create_all(bind=engine)
