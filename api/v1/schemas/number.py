from pydantic import BaseModel, field_validator
from fastapi import HTTPException


class NumberQueryParams(BaseModel):
    number: str
    @field_validator('number')
    def check_valid_number(cls, value):
        try:
            value = int(value)
        except ValueError:
            raise HTTPException(
                400,
                {
                    "number": value,
                    "error": True
                })
        return value
    
class NumberClassificationResponse(BaseModel):
    number: int
    is_prime: bool
    is_perfect: bool
    properties: list
    digit_sum: int
    fun_fact: str
    