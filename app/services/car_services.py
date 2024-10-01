from app.models.car import Car
from typing import List, Optional
from app.models.rent import RentRequest

# Mock database for cars
cars_db = {
    "11AA22": {"plate_number": "11AA22", "brand": "Ferrari", "price": 100, "is_rented": False,
               "rental_dates": {"begin": None, "end": None}},
    "22BB33": {"plate_number": "22BB33", "brand": "Toyota", "price": 50, "is_rented": False,
               "rental_dates": {"begin": None, "end": None}},
}

# Add a car to the database
def add_car(car: Car) -> bool:
    if car.plate_number in cars_db:
        raise ValueError("Car already exists")
    cars_db[car.plate_number] = car.dict()
    return True

# Remove a car by its plate number
def remove_car(plate_number: str) -> bool:
    if plate_number not in cars_db:
        raise ValueError("Car not found")
    del cars_db[plate_number]
    return True

# List unrented cars
def car_to_be_rented() -> List[Car]:
    unrented_cars = []
    for car in cars_db.values():
        if not car["is_rented"]:
            unrented_cars.append(Car(**car))
    return unrented_cars

# List all cars
def list_of_cars() -> List[Car]:
    cars = []
    for car in cars_db.values():
        cars.append(Car(**car))
    return cars

# Get a car by its plate number
def get_car_by_plate(plate_number: str) -> Optional[Car]:
    car = cars_db.get(plate_number)
    if car:
        return Car(**car)
    return None

# Rent or return a car
def rent_or_return_car(plate_number: str, rent: bool, dates: Optional[RentRequest] = None) -> dict:
    car = cars_db.get(plate_number)
    if car is None:
        raise ValueError("Car not found")

    # if rent is True, rent the car
    if rent:
        # Ensure car is not already rented
        if car["is_rented"]:
            raise ValueError("Car is already rented")
        if not dates:
            raise ValueError("Rent dates must be provided")
        # Validate dates using the RentRequest model
        car["rental_dates"] = dates.dict()
        car["is_rented"] = True
        return {"message": f"Car {plate_number} rented successfully", "dates": dates.dict()}

    # if rent is False, return the car
    else:
        # Ensure car is currently rented
        if not car["is_rented"]:
            raise ValueError("Car is not rented")
        car["is_rented"] = False
        car["rental_dates"] = {"begin": None, "end": None}  # Clear rental dates
        return {"message": f"Car {plate_number} returned successfully"}
