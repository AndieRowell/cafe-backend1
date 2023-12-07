from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel

#! from perspective of dev/admin - info needed to create/update/delete a badge
#! from perspective of a user - info given back to read a badge

'''
TODO:
- base schema
- create schema
- update schema
'''

class Badge(BaseModel):
    title: str
    description: str
    color_hex: str
    icon_url: str
    created_timestamp: datetime
    updated_timestamp: datetime

#!CREATE - dev
class BadgeCreate(BadgeBase):
    pass

#!UPDATE - dev
class BadgeUpdate(BadgeBase):
    pass

#!IN DB - dev
class BadgeInDBBase(BadgeBase):
    id: Optional[int] = None

    class Config:
        from_attributes = True

# badge that inherits from badge in db base to include EVERYTHING
#! Badge
class Badge(BadgeInDBBase):
    pass
