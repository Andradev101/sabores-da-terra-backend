from fastapi import APIRouter

router = APIRouter(
    prefix="/orders",
    tags=["orders"]
)

@router.get("/", tags=["orders"])
async def get_orders():
    return [{"username": "Rick"}, {"username": "Morty"}]

@router.get("/{id}", tags=["orders"])
async def get_order(id: str):
    return {"id": id}

@router.get("/{id}", tags=["orders"])
async def get_order(id: str):
    return {"id": id}

@router.put("/{id}", tags=["orders"])
async def update_order(id: str):
    return {"id": id}

@router.delete("/{id}", tags=["orders"])
async def delete_order(id: str):
    return {"id": id}