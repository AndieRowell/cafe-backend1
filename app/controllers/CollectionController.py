from typing import Any, Dict, Optional, Union
from sqlalchemy.orm import Session
from app.controllers.BaseController import BaseController
from app.models.collection import Collection as CollectionModel
from app.schemas.collection import CollectionBase, CollectionCreate, CollectionUpdate, CollectionInDBBase

# [MODEL, CREATE SCHEMA, UPDATE SCHEMA]
# should it just be get_by_id
class CollectionController(BaseController[CollectionModel, CollectionCreate, CollectionUpdate]):

#! find a collection by id
    def get_drink_by_id(self, db: Session, * id: int):
        return db.query(CollectionModel).filter(CollectionModel.id == id).first()

#! find a collection by title
    def get_collection_by_title(self, db: Session, *, title: str):
        return db.query(CollectionModel).filter(CollectionModel.title == title).first()

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

collection = CollectionController(CollectionModel)
