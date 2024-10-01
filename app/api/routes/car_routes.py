from fastapi import APIRouter, HTTPException, Depends
from app.models.car import Car
from app.models.rent import RentRequest
from app.services.car_services import add_car, remove_car, car_to_be_rented, list_of_cars, get_car_by_plate, rent_or_return_car
from pydantic import BaseModel # TODO: Create Models for all responses for validators purposes
from typing import Optional

# Define the router
router = APIRouter()

# Get list of unrented cars
@router.get("/cars", response_model=list[Car], summary="Get a list of unrented cars")
def get_unrented_cars():
    """
    Fetch all cars that are currently not rented.
    """
    return list_of_cars()

# Get car details by plate number
@router.get("/cars/{plate_number}", response_model=Car, summary="Get details of a specific car")
def get_car(plate_number: str):
    """
    Get the details of a specific car using its plate number.
    """
    car = get_car_by_plate(plate_number)
    if car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return car

# Rent or return a car
@router.put("/cars/{plate_number}", summary="Rent or return a car")
def rent_or_return(plate_number: str, rent: bool, dates: RentRequest):
    """
    Rent or return a car. To rent a car, provide `rent=true` and rental dates in the request body.
    To return a car, provide `rent=false` without rental dates.
    """
    if dates is None and rent:
        raise HTTPException(status_code=400, detail="Rent dates must be provided")
    try:
        return rent_or_return_car(plate_number, rent, dates)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Add a new car
@router.post("/cars", response_model=Car, summary="Add a new car")
def add_new_car(car: Car):
    """
    Add a new car to the database.
    """
    try:
        add_car(car)
        return {"message": f"Car {car.plate_number} added successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Remove a car by plate number
@router.delete("/cars/{plate_number}", summary="Remove a car by plate number")
def remove_car_by_plate(plate_number: str):
    """
    Remove a car from the database using its plate number.
    """
    try:
        remove_car(plate_number)
        return {"message": f"Car {plate_number} removed successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))