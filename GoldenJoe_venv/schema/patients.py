from pydantic import BaseModel


# the below code fragment is the Patient object
class Patient(BaseModel):
    patient_id: int
    full_name: str
    age: int
    gender: str
    weight_Kg: float
    height_cm: float
    address: str
    phone_number: str
    medical_history: str
    allergies: str

# the below code fragment is a class used as a model to create a patient

class CreatePatient(BaseModel):
    full_name: str
    age: int
    gender: str
    weight_Kg: float
    height_cm: float
    address: str
    phone_number: str
    medical_history: str
    allergies: str

# below is a list of random patients that will be in-memory storage

Patients: list[Patient] = [
  {
    "patient_id": 1,
    "full_name": "Nneoma Chidinma Okoro",
    "age": 25,
    "gender": "Female",
    "weight_Kg": 85.62,
    "height_cm": 170,
    "address": "14, Ojuelegba Street, Surulere, Lagos",
    "phone_number": "08012345678",
    "medical_history": "Asthma",
    "allergies": "Penicillin"
  },
  {
    "patient_id": 2,
    "full_name": "Olumide Ayodele Adeyemi",
    "age": 30,
    "gender": "Male",
    "weight_Kg": 112.35,
    "height_cm": 145.2,
    "address": "23, Awolowo Road, Ikoyi, Lagos",
    "phone_number": "07011122233",
    "medical_history": "Diabetes",
    "allergies": "Sulfa drugs"
  },
  {
    "patient_id": 3,
    "full_name": "Zainab Bukola Mohammed",
    "age": 68,
    "gender": "Female",
    "weight_Kg": 98.23,
    "height_cm": 150,
    "address": "56, Ogunlana Drive, Surulere, Lagos",
    "phone_number": "08022223333",
    "medical_history": "Hypertension",
    "allergies": "Codeine"
  },
  {
    "patient_id": 4,
    "full_name": "Chukwuemeka Emmanuel Nwosu",
    "age": 55,
    "gender": "Male",
    "weight_Kg": 62.14,
    "height_cm": 161,
    "address": "12, Ademola Street, Ikoyi, Lagos",
    "phone_number": "07033334444",
    "medical_history": "Arthritis",
    "allergies": "Chloroquine"
  },
  {
    "patient_id": 5,
    "full_name": "Aisha Olabisi Sanni",
    "age": 22,
    "gender": "Female",
    "weight_Kg": 58.22,
    "height_cm": 150.4,
    "address": "34, Ojuelegba Street, Surulere, Lagos",
    "phone_number": "08044445555",
    "medical_history": "N/A",
    "allergies": "N/A"
  }

]




    