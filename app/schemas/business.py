from pydantic import BaseModel
from typing import List, Optional

#! from perspective of dev/admin - info needed to create/update/delete a business
#! from perspective of a user - info given back to read a business
# consider CRUD
'''
TODO:
- base schema
- create schema
- update schema
'''

class BusinessBase(BaseModel):
    name: str
    address: str
    city: str
    state: str
    postal_code: str
    latitude: float
    longitude: float
    created_timestamp: str
    updated_timestamp: str

#!CREATE - dev
class BusinessCreate(BusinessBase):
    pass

#!UPDATE - dev
class BusinessUpdate(BusinessBase):
    pass

#!IN DB - dev
class BusinessInDBBase(BusinessBase):
    id: Optional[int] = None
