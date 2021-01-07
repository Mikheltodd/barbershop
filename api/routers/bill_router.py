from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from db.db_connection import get_db
from db.customer_db import CustomerInDB
from db.bill_db import BillInDB
from db.discount_db import DiscountInDB
from db.serviceorder_db import ServiceorderInDB
from models.customer_models import CustomerIn, CustomerOut
from models.bill_models import BillIn, BillOut
from models.discount_models import DiscountIn, DiscountOut
from models.serviceorder_models import ServiceorderIn, ServiceorderOut

router = APIRouter()


