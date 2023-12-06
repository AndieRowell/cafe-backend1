from typing import Any, List, Annotated

from fastapi import APIRouter, Body, Depends, HTTPException, Query, Form

#? is this just for user authentication?
#from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
# from database import SessionLocal, engine

from app import models, schemas, controllers
from app.api import deps
from app.core.config import settings

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
@router.get("/", response_model=List[schemas.Drink])
def read_drink(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
#   current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    drinks = controllers.drink.get_multi(db, skip=skip, limit=limit)
    return drinks

#!- post - create new business (dev)
@router.post("/", response_model=schemas.Drink)
def create_drink(
    *,
    db: Session = Depends(deps.get_db),
    drink_in: schemas.DrinkCreate,
#    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    new_drink = controllers.drink.get_by_id(db, id=drink_in.id)
    if new_drink:
        raise HTTPException(
            status_code=400,
            detail="The drink with this name already exists in the system.",
        )
    return new_drink
