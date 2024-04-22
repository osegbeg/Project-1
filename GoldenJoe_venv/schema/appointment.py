from pydantic import BaseModel
from datetime import datetime, date, time
from typing import Annotated
from fastapi import Form

class Appointment(BaseModel):
    appointment_id: int
    patient_id: int
    doctor_id: int
    appointment_date: str
    appointment_time: str
    is_completed: bool

class AppointmentCreate(BaseModel):
    patient_id: int
    doctor_id: int
    appointment_date: date = Form(...),
    appointment_time: time = Form(...),
    is_completed: bool
    
appointments = [
    Appointment(
        appointment_id=1,
        patient_id=1,
        doctor_id=1,
        appointment_date="2024-06-01",
        appointment_time="10:00",
        is_completed=False
    ),
    Appointment(
        appointment_id=2,
        patient_id=2,
        doctor_id=2,
        appointment_date="2024-04-02",
        appointment_time="11:00",
        is_completed=False
    ),
    Appointment(
        appointment_id=3,
        patient_id=3,
        doctor_id=3,
        appointment_date="2024-05-08",
        appointment_time="12:00",
        is_completed=False
    ),
]