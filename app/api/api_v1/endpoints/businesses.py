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
- get - read all businesses as anonymous user
- post - create new business (dev)
- put - update business (dev)
- get - my favorite businesses ------ #? is this included in lists instead
- get - get specific business by id as anonymous user
- get - read all businesses as authorized user
- get - get specific business by id as authorized user
'''

#!- get - read all businesses as anonymous user
@router.get("/businesses/", response_model=List[schemas.Business])
def read_businesses(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
#   current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    businesses = controllers.business.get_multi(db, skip=skip, limit=limit)
    return businesses

#!- post - create new business (dev)
@router.post("/businesses/", response_model=schemas.Business)
def create_business(
    *,
    db: Session = Depends(deps.get_db),
    business_in: schemas.BusinessCreate,
#    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    new_business = controllers.user.get_by_id(db, id=business_in.id)
    if new_business:
        raise HTTPException(
            status_code=400,
            detail="The business with this name already exists in the system.",
        )
    return controllers.create_business(db=db, business=business)
