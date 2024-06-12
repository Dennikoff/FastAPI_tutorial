from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from operations.models import operation
from database import get_async_session
router = APIRouter(
    prefix="/operations",
    tags=["Operation"]
)

@router.get("/")
async def get_operations(operation_amount: int, session: AsyncSession = Depends(get_async_session)):
    query = select(operation).where(operation.c.amount == operation_amount)
    result = await session.execute(query)
    return result.all()


