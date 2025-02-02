from fastapi import APIRouter
from api.v1.routes.number import number

api_version_one = APIRouter(prefix="/api")


api_version_one.include_router(number)