from fastapi import APIRouter

router = APIRouter(
    prefix="/suppliers",
    tags=["suppliers"]
)

@router.get("/", tags=["suppliers"])
async def get_suppliers():
    return [{"username": "Rick"}, {"username": "Morty"}]

@router.get("/{id}", tags=["suppliers"])
async def get_supplier(id: str):
    return {"id": id}

@router.get("/{id}", tags=["suppliers"])
async def get_supplier(id: str):
    return {"id": id}

@router.put("/{id}", tags=["suppliers"])
async def update_supplier(id: str):
    return {"id": id}

@router.delete("/{id}", tags=["suppliers"])
async def delete_supplier(id: str):
    return {"id": id}