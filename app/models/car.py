from pydantic import BaseModel

class Car(BaseModel):
    plate_number: str = "00XX00"
    brand: str = "Toyota"
    price: int = 1
    is_rented: bool = False
    rental_dates: dict = {"begin": None, "end": None}

