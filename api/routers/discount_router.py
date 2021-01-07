from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from db.db_connection import get_db
from db.discount_db import DiscountInDB
from models.discount_models import DiscountIn, DiscountOut

router = APIRouter()

