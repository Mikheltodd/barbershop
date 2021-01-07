from pydantic import BaseModel


class AppointmentDetailIn(BaseModel):
    appointment_detail_employee: int
    appointment_detail_service: int
    appointment_detail_appointment: int


class AppointmentDetailOut(BaseModel):
    appointment_detail_id: int
    appointment_detail_employee: int
    appointment_detail_service: int
    appointment_detail_appointment: int

    class Config:
        orm_mode = True
