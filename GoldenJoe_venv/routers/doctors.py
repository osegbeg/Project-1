from fastapi import APIRouter, HTTPException
from schema.doctors import Doctor, CreateDoctor, Doctors

doctor_router = APIRouter()

@doctor_router.get("/", status_code=200)
def all_doctors():
    return {"message": "All the Doctors in the database queried successfully", "data": Doctors}

@doctor_router.get("/{doctor_id}", status_code=200)
def doctor_by_id(doctor_id: int):
    for doctor in Doctors:
        if doctor['doctor_id'] == doctor_id:
            return {"message": "doctor queried successfully", "data": doctor}
    raise HTTPException(status_code=404, detail="doctor not found")

@doctor_router.post("/", status_code=201)
def create_doctor(payload: CreateDoctor):
    doctor_id = len(Doctors) + 1
    new_doctor = Doctor(
        doctor_id=doctor_id,
        full_name=payload.full_name,
        specialty=payload.specialty,
        address=payload.address,
        phone_number=payload.phone_number,
        is_available=payload.is_available
    )
    Doctors.append(new_doctor)
    return {"message": "doctor created successfully", "data": new_doctor}

@doctor_router.put("/{doctor_id}", status_code=200)
def update_doctor(doctor_id: int, payload: CreateDoctor):
    current_doctor = None
    for doctor in Doctors:
        if doctor['doctor_id'] == doctor_id:
            current_doctor = doctor
            break
    if not current_doctor:
        raise HTTPException(status_code=404, detail="doctor not found")
    current_doctor['full_name'] = payload.full_name
    current_doctor['specialty'] = payload.specialty
    current_doctor['address'] = payload.address
    current_doctor['phone_number'] = payload.phone_number
    current_doctor['is_available'] = payload.is_available
    return {"message": "doctor updated successfully", "data": current_doctor}

    

@doctor_router.delete("/{doctor_id}", status_code=200)

def delete_doctor(doctor_id: int):
    for doctor in Doctors:
        if doctor['doctor_id'] == doctor_id:
            Doctors.remove(doctor)
            return {"message": "doctor deleted successfully"}
    raise HTTPException(status_code=404, detail="doctor not found")