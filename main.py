from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import Optional


# Pydantic models for request/response schemas
class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: Optional[float] = None


class ItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None


class ItemResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: Optional[float] = None


app = FastAPI()


# Existing endpoint
@app.get("/getHello")
async def root():
    return {"message": "Hello"}


# POST /api/items - Create item
@app.post("/api/items", status_code=status.HTTP_201_CREATED)
async def create_item(item: ItemCreate):
    return {
        "id": 1,
        "name": item.name,
        "description": item.description or "Sample description",
        "price": item.price or 1000,
        "created": True
    }


# GET /api/items/{id} - Get single item
@app.get("/api/items/{id}")
async def get_item(id: int):
    return {
        "id": id,
        "name": f"Sample Item {id}",
        "description": "This is a mock item for testing",
        "price": 1000 + (id * 100)
    }


# GET /api/items - Get items list
@app.get("/api/items")
async def get_items(limit: int = 10, offset: int = 0):
    items = []
    for i in range(offset + 1, offset + limit + 1):
        items.append({
            "id": i,
            "name": f"Sample Item {i}",
            "description": f"Description for item {i}",
            "price": 1000 + (i * 100)
        })
    return {
        "items": items,
        "total": limit,
        "offset": offset,
        "limit": limit
    }


# PUT /api/items/{id} - Update item
@app.put("/api/items/{id}")
async def update_item(id: int, item: ItemUpdate):
    return {
        "id": id,
        "name": item.name or f"Updated Item {id}",
        "description": item.description or "Updated description",
        "price": item.price or 2000,
        "updated": True
    }


# DELETE /api/items/{id} - Delete item
@app.delete("/api/items/{id}")
async def delete_item(id: int):
    return {
        "id": id,
        "deleted": True,
        "message": f"Item {id} has been deleted"
    }
