from schema.doctors import Doctors, Doctor


#This function checks if the doctor with the given ID is available, and returns the doctor object if they are. If the doctor is not available, it returns None.

# def get_available_doctor(doctor_id: int):
# 	doctor = next((doctor for doctor in Doctors if doctor['doctor_id'] == doctor_id and doctor['is_available']), None)
# 	return doctor
def get_available_doctor(doctor_id: int):
    doctor_data = next((doctor for doctor in Doctors if doctor['doctor_id'] == doctor_id and doctor['is_available']), None)
    return Doctor(**doctor_data) if doctor_data else None

