from datetime import datetime
from enum import Enum
from typing import List, Optional
from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, ValidationError
from operations.router import router as router_operation

app = FastAPI(title="Trading App")

app.include_router(
    router_operation
)