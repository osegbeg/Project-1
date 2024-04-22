from fastapi import APIRouter, HTTPException
from schema.patients import Patient, CreatePatient, Patients

patient_router = APIRouter()

@patient_router.get("/", status_code=200)
def all_patients():
    return {"message": "All the Patients in the database queried successfully", "data": Patients}

@patient_router.get("/{patient_id}", status_code=200)
def patient_by_id(patient_id: int):
    for Patient in Patients:
        if Patient['patient_id'] == patient_id:
            return {"message": "Patient queried successfully", "data": Patient}
    raise HTTPException(status_code=404, detail="Patient not found")

@patient_router.post("/", status_code=201)
def create_patient(payload: CreatePatient):
    patient_id = len(Patients) + 1
    new_patient = Patient(
        patient_id=patient_id,
        full_name=payload.full_name,
        age=payload.age,
        gender=payload.gender,
        weight_Kg=payload.weight_Kg,
        height_cm=payload.height_cm,
        address=payload.address,
        phone_number=payload.phone_number,
        medical_history=payload.medical_history,
        allergies=payload.allergies
    )
    Patients.append(new_patient)
    return {"message": "Patient created successfully", "data": new_patient}

@patient_router.put("/{patient_id}", status_code=200)
def update_patient(patient_id: int, payload: CreatePatient):
    current_patient = None
    for patient in Patients:
        if patient['patient_id'] == patient_id:
            current_patient = patient
            break
    if not current_patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    current_patient['full_name'] = payload.full_name
    current_patient['age'] = payload.age
    current_patient['gender'] = payload.gender
    current_patient['weight_Kg'] = payload.weight_Kg
    current_patient['height_cm'] = payload.height_cm
    current_patient['address'] = payload.address
    current_patient['phone_number'] = payload.phone_number
    current_patient['medical_history'] = payload.medical_history
    current_patient['allergies'] = payload.allergies
    return {"message": "Patient updated successfully", "data": current_patient}

    

@patient_router.delete("/{patient_id}", status_code=200)

def delete_patient(patient_id: int):
    for patient in Patients:
        if patient['patient_id'] == patient_id:
            Patients.remove(patient)
            return {"message": "Patient deleted successfully"}
    raise HTTPException(status_code=404, detail="Patient not found")