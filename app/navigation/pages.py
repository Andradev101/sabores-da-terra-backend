from fastapi import APIRouter
router = APIRouter()

@router.get("/")
def home():
    return {"Hello": "World"}

@router.get("/dashboards")
def get_dashboard():
    return {"Hello": "World"}


# Admin navigation

admin_router = APIRouter(
    prefix="/admin",
    tags=["admin"]
)

@admin_router.get("")
def get_admin():
    return {"Hello": "World"}