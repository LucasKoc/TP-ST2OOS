from fastapi import FastAPI
from app.api.routes import car_routes

app = FastAPI()

# Include the car routes
app.include_router(car_routes.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Car Rental API"}