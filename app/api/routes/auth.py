from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["Auth"],
)


@router.get("/")
async def hello():
    return {"Message": "Hello, users!"}
