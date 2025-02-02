from fastapi import status, FastAPI
from api.v1.routes import api_version_one
from api.utils import settings
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    description=settings.PROJECT_DESCRIPTION
)
app.include_router(api_version_one)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
	return JSONResponse(
		status_code=status.HTTP_200_OK,
		content=f"Hey There👋. Welcome to Numbers API!"
	)