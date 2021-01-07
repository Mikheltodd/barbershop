from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from db.db_connection import get_db
from db.serviceorder_db import ServiceorderInDB
from models.serviceorder_models import ServiceorderIn, ServiceorderOut

router = APIRouter()

