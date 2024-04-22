from fastapi import FastAPI
from routers.patients import patient_router
from routers.doctors import doctor_router
from routers.appointment import appointment_router

app = FastAPI()

app.include_router(router=patient_router, prefix='/patient', tags=['patient'])
app.include_router(router=doctor_router, prefix='/doctor', tags=['doctor'])
app.include_router(router=appointment_router, prefix='/appointment', tags=['appointment'])

@app.get('/')
def index():
    return {'message': 'Welcome to the world where hospitality and technology waltz to the tune of your convenience'}