from typing import Annotated
from api.v1.schemas import NumberClassificationResponse, NumberQueryParams
from api.v1.services import number_service
from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


number = APIRouter(prefix="/classify-number", tags=["Numbers"])



@number.get("", response_model=NumberClassificationResponse)
async def classify_number(query: Annotated[NumberQueryParams, Query()]):
    fun_fact = await number_service.get_fun_fact(query.number)
    prime_status = number_service.is_prime(query.number)
    perfect_status = number_service.is_perfect(query.number)
    armstrong_status = number_service.armstrong_number(query.number)

    properties = []
    if armstrong_status:
        properties.append("armstrong")
    if query.number % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")
    
    digit_sum_value = number_service.digit_sum(query.number)
    return JSONResponse(
        status_code=200,  
        content=jsonable_encoder({
            "number": query.number,
            "is_prime": prime_status,
            "is_perfect": perfect_status,
            "properties": properties,
            "digit_sum": digit_sum_value,
            "fun_fact": fun_fact
    }))
