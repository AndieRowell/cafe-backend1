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


    #* code searching keyword and getting back nearby cafes to user location
    # def get_nearby_cafes(db: Session, keyword: str, latitude: float, longitude: float):
    #     user_location = f'POINT({longitude} {latitude})'
    #     return db.query(Business).filter(
    #         BusinessModel. ____ .contains([keyword]),
    #         BusinessModel.locations.ST_DWithin(user_location, 0.1)).all()
