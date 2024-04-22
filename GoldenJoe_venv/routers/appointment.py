from typing import Annotated
from datetime import datetime, date, time
from fastapi import APIRouter, HTTPException, Form, Depends
from fastapi.responses import JSONResponse
from schema.appointment import appointments, Appointment, AppointmentCreate
from schema.doctors import Doctor, CreateDoctor, Doctors
from schema.patients import Patient, CreatePatient, Patients
from services.availability import get_available_doctor

appointment_router = APIRouter()

@appointment_router.post("/appointments", status_code=201)
def create_appointment(
    patient_id: int,
    appointment_date: date = Form(...),
    appointment_time: time = Form(...),
    doctor: Doctor = Depends(get_available_doctor)
):
    if not doctor:
        raise HTTPException(status_code=404, detail="No available doctor for the selected time and date")
    
    appointment = Appointment(
        patient_id=patient_id,
        doctor_id=doctor.doctor_id,
        appointment_date=appointment_date,
        appointment_time=appointment_time,
        is_completed=False
    )
    appointments.append(appointment)
    return JSONResponse(status_code=201, content={"message": "Appointment created successfully", "data": appointment})

# the below code allows to find th appointment, update the appointment status and make the doctor available again

@appointment_router.put("/{appointment_id}", status_code=200)
def complete_appointment(appointment_id: int, completed: bool):
	# Find the appointment
	appointment = next((appointment for appointment in appointments if appointment.id == appointment_id), None)
	if not appointment:
		return JSONResponse(status_code=404, content={"message": "Appointment not found"})

	# Update the appointment status
	appointment.completed = completed
	# Make the doctor available again
	doctor = next((doctor for doctor in Doctors if doctor.id == appointment.doctor_id), None)
	doctor.available = True
	return JSONResponse(status_code=200, content={"message": "Appointment completed successfully"})

# the below code is to create the endpoint that cancels the appointment

@appointment_router.delete("/{appointment_id}", status_code=200)
def cancel_appointment(appointment_id: int):
	# Find the appointment
	appointment = next((appointment for appointment in appointments if appointment.id == appointment_id), None)
	if not appointment:
		return JSONResponse(status_code=404, content={"message": "Appointment not found"})

	# Update the appointment status
	appointment.completed = True
	# Make the doctor available again
	doctor = next((doctor for doctor in Doctors if doctor.id == appointment.doctor_id), None)
	doctor.available = True
	return JSONResponse(status_code=200, content={"message": "Appointment canceled successfully"})
