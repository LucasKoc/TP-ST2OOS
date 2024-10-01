from pydantic import BaseModel, Field, validator
from datetime import date

class RentRequest(BaseModel):
    begin: date
    end: date

    @validator("end")
    def check_dates(cls, end, values):
        begin = values.get("begin")
        if begin and end < begin:
            raise ValueError("End date must be after the begin date")
        return end
