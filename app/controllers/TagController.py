from typing import Any, Dict, Optional, Union
from sqlalchemy.orm import Session
from app.controllers.BaseController import BaseController
from app.models.tag import Tag as TagModel
from app.schemas.tag import TagBase, TagCreate, TagUpdate

'''
TODO:
- drink crud
- drink child relationships
    - businesstag
'''
# [MODEL, CREATE SCHEMA, UPDATE SCHEMA]
# should it just be get_by_id
class TagController(BaseController[TagModel, TagCreate, TagUpdate]):
    def create_tag(self, db: Session, *, obj_in: TagBase) -> TagModel:
        db_obj = TagModel(
            title=obj_in.title,
            description=obj_in.description,
            color_hex=obj_in.color_hex,
            icon_url=obj_in.icon_url,
            created_timestamp=obj_in.created_timestamp,
            updated_timestamp=obj_in.updated_timestamp,

        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

tag = TagController(TagModel)

# {
#   "title": "Coffee",
#   "description": "Good coffee",
#   "color_hex": "string",
#   "icon_url": "string",
#   "created_timestamp": "2023-12-08T21:11:32.574Z",
#   "updated_timestamp": "2023-12-08T21:11:32.574Z"
# }
