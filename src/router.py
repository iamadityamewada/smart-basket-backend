from fastapi import APIRouter
from src.api.controllers.user import user_router



router = APIRouter(prefix='/api/v1')

router.include_router(user_router, prefix="/user")