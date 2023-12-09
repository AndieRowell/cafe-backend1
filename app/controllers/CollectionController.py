from typing import Any, Dict, List, Optional, Union
from sqlalchemy.orm import Session
from app.controllers.BaseController import BaseController
from app.models.collection import Collection as CollectionModel, CollectionTrackerDrink
from app.models.drink import Drink
from app.schemas.collection import CollectionBase, CollectionCreate, CollectionUpdate, CollectionInDBBase
from app.schemas.drink import DrinkBase

# [MODEL, CREATE SCHEMA, UPDATE SCHEMA]
# should it just be get_by_id
class CollectionController(BaseController[CollectionModel, CollectionCreate, CollectionUpdate]):


#! find a collection by title
    def get_collection_by_title(self, db: Session, *, title: str):
        return db.query(CollectionModel).filter(CollectionModel.title == title).first()
#! find a collection by id
    def get_collection_by_id(self, db: Session, *, id: int):
        return db.query(CollectionModel).filter(CollectionModel.id == id).first()

#! create collection
    def create_collection(self, db: Session, *, obj_in: CollectionBase) -> CollectionModel:
        db_obj = CollectionModel(
            user_id=obj_in.user_id,
            title=obj_in.title,
            ordered_list_number=obj_in.ordered_list_number,
            contact_info=obj_in.contact_info,
            website_url=obj_in.website_url,
            instagram_handle=obj_in.instagram_handle,
            event_promotion_time_start=obj_in.event_promotion_time_start,
            event_promotion_time_stop=obj_in.event_promotion_time_stop,
            event_promotion_banner=obj_in.event_promotion_banner,
            favorite=obj_in.favorite,
            created_timestamp=obj_in.created_timestamp,
            updated_timestamp=obj_in.updated_timestamp
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def add_drink_to_collection(self, db: Session, *, drink_id: int, collection_id: int) -> CollectionModel:
        db_obj = CollectionTrackerDrink(
            drink_id=drink_id,
            collection_tracker_id=collection_id
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        c = db.query(CollectionModel).filter(CollectionModel.id == collection_id).first()
        return c

    def get_collection_drinks(self, db: Session, *, collection_id: int) -> List[Drink]:
        return db.query(CollectionTrackerDrink, Drink)\
            .filter(CollectionTrackerDrink.collection_tracker_id == collection_id)\
            .join(CollectionTrackerDrink.drink).all()

collection = CollectionController(CollectionModel)
