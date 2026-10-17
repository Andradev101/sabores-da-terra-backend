from fastapi import APIRouter

router = APIRouter(
    prefix="/products",
    tags=["products"]
)

@router.get("/", tags=["products"])
async def get_products():
    return [{"username": "Rick"}, {"username": "Morty"}]

@router.get("/{id}", tags=["products"])
async def get_product(id: str):
    return {"id": id}

@router.put("/{id}", tags=["products"])
async def update_product(id: str):
    return {"id": id}
 
@router.delete("/{id}", tags=["products"])
async def delete_product(id: str):
    return {"id": id}