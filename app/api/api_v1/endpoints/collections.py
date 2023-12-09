from typing import Any, List, Annotated

from fastapi import APIRouter, Body, Depends, HTTPException, Query, Form

#? is this just for user authentication?
#from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
# from database import SessionLocal, engine

from app import models, schemas, controllers
from app.api import deps
from app.core.config import settings
from app.schemas.drink import Drink

router = APIRouter()

'''
TODO:
- get - read all event collections as anonymous/authenticated user
- post - create new collection (dev)
- put - update collection (dev)
- get - my favorite collection/collections ------ #? is this included in lists instead
- get - get specific collection by id as authenticated user
'''

#!- get - read all event collections as anonymous/authenticated user
@router.get("/", response_model=List[schemas.Collection])
def read_collection(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
#   current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    collection = controllers.collection.get_multi(db, skip=skip, limit=limit)
    return collection

#!- post - create new collection (dev)
@router.post("/", response_model=schemas.Collection)
def create_collection(
    *,
    db: Session = Depends(deps.get_db),
    obj_in: schemas.CollectionBase,
#    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    new_collection = controllers.collection.create_collection(db, obj_in=obj_in)
    return new_collection

@router.post("/add_drink", response_model=schemas.Collection)
def add_drink_to_collection(
    *,
    db: Session = Depends(deps.get_db),
    drink_id: int,
    collection_id: int,
#    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    collection = controllers.collection.add_drink_to_collection(db, drink_id=drink_id, collection_id=collection_id)
    return collection

@router.post("/get_collection_drinks", response_model=List[schemas.Drink])
def get_collection_drinks(
    *,
    db: Session = Depends(deps.get_db),
    collection_id: int,
#    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    drinks = controllers.collection.get_collection_drinks(db, collection_id=collection_id)
    return drinks
