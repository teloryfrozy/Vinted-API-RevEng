from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from config.settings import ALLOW_ORIGINS, DEBUG_MODE
from routers import ads_management, auth, follow_mass
from config.models import lifespan


app = FastAPI(debug=DEBUG_MODE, lifespan=lifespan)
app.mount("/api", app)


app.include_router(ads_management.router)
app.include_router(auth.router)
app.include_router(follow_mass.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOW_ORIGINS,
    allow_methods=["GET", "POST", "DELETE"],
    allow_credentials=True,
)
