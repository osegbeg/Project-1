from pydantic import BaseModel


# the below code fragment is the Doctor object
class Doctor(BaseModel):
    doctor_id: int
    full_name: str
    specialty: str
    address: str
    phone_number: str
    is_available: bool
    

# the below code fragment is a class used as a model to set-up a Doctor

class CreateDoctor(BaseModel):
    full_name: str
    specialty: str
    address: str
    phone_number: str
    is_available: bool

# below is a list of random patients that will be in-memory storage

Doctors: list[Doctor] = [
{
    "doctor_id": 1,
    "full_name": "Adanna Chiamaka Onyekwere",
    "specialty": "Cardiology",
    "address": "4, Alhaji Masha Street, Surulere, Lagos",
    "phone_number": "08111122233",
    "is_available": True
},
{
    "doctor_id": 2,
    "full_name": "Tunde Oluwatoyin Oyediran",
    "specialty": "Neurology",
    "address": "17, Ribadu Street, Ikoyi, Lagos",
    "phone_number": "07022223333",
    "is_available": True
},

{
    "doctor_id": 3,
    "full_name": "Ngozi Ifeyinwa Okonkwo",
    "specialty": "Pediatrics",
    "address": "25, Oju Olobun Close, Victoria Island, Lagos",
    "phone_number": "08055556666",
    "is_available": True
},

{
    "doctor_id": 4,
    "full_name": "Kunle Temitope Adebiyi",
    "specialty": "Orthopedics",
    "address": "3, Akin Adesola Street, Victoria Island, Lagos",
    "phone_number": "07066667777",
    "is_available": True
},

{
    "doctor_id": 5,
    "full_name": "Chidimma Uchechi Eze",
    "specialty": "Dermatology",
    "address": "10, Musa Yar'Adua Street, Victoria Island, Lagos",
    "phone_number": "08177778888",
    "is_available": True
}

]


