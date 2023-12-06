from typing import Any, Dict, Optional, Union
from sqlalchemy.orm import Session
from app.controllers.BaseController import BaseController
from app.models.business import Business as BusinessModel, BusinessTag as BusinessTagModel
from app.schemas.business import BusinessBase, BusinessCreate, BusinessUpdate, BusinessInDBBase, Business

'''
TODO:
- business crud
- business child relationships
    - businesstag
'''
# [MODEL, CREATE SCHEMA, UPDATE SCHEMA]
# use basecontroller for
class BusinessController(BaseController[BusinessModel, BusinessCreate, BusinessUpdate]):
    def get_by_id(self, db: Session, * id: int):
        return db.query(Business).filter(Business.id == id).first()

    def create(self, db: Session, *, obj_in: BusinessCreate) -> Business:
        db_obj = Business(
            name=obj_in.name,
            address=obj_in.address,
            city=obj_in.city,
            state=obj_in.state,
            postal_code=obj_in.postal_code,
            latitude=obj_in.latitude,
            longitude=obj_in.longitude,
            #created timestamp
            #updated timestamp
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    #* code searching keyword and getting back nearby cafes to user location
    # def get_nearby_cafes(db: Session, keyword: str, latitude: float, longitude: float):
    #     user_location = f'POINT({longitude} {latitude})'
    #     return db.query(Business).filter(
    #         BusinessModel. ____ .contains([keyword]),
    #         BusinessModel.locations.ST_DWithin(user_location, 0.1)).all()
