from typing import Any, Dict, Optional, Union
from sqlalchemy.orm import Session
from app.controllers.BaseController import BaseController
from app.models.drink import Drink as DrinkModel
from app.schemas.drink import DrinkBase, DrinkCreate, DrinkUpdate, DrinkInDBBase, Drink

'''
TODO:
- drink crud
- drink child relationships
    - businesstag
'''
# [MODEL, CREATE SCHEMA, UPDATE SCHEMA]
# use basecontroller for
class DrinkController(BaseController[DrinkModel, DrinkCreate, DrinkUpdate]):
    def get_by_id(self, db: Session, * id: int):
        return db.query(Drink).filter(Drink.id == id).first()

    def create(self, db: Session, *, obj_in: DrinkCreate) -> Drink:
        db_obj = Drink(
            business_id=obj_in.business_id, #connect to business?
            name=obj_in.name,
            description=obj_in.description,
            price=obj_in.price,
            featured=obj_in.featured,
            ordered_list_number=obj_in.ordered_list_number
            #created_timestamp=obj_in.created_timestamp
            #updated_timestamp=obj_in.updated_timestamp
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
