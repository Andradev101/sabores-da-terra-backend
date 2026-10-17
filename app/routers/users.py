from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/", tags=["users"])
async def get_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/me", tags=["users"])
async def get_self():
    return {"username": "fakecurrentuser"}


@router.get("/{id}", tags=["users"])
async def get_user(id: str):
    return {"id": id}

@router.put("/{id}", tags=["users"])
async def update_user(id: str):
    return {"id": id}
 
@router.delete("/{id}", tags=["users"])
async def delete_user(id: str):
    return {"id": id}