from pydantic import BaseModel
from typing import List, Optional

#! from

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

#!CREATE
class BusinessCreate(BusinessBase):
    name: str
    address: str
    city: str
    state: str
    postal_code: str
    latitude: float
    longitude: float
    created_timestamp: str
    updated_timestamp: str


#!READ
class BusinessRead(BusinessBase):
    name: str
    address: str
    city: str
    state: str
    postal_code: str
    latitude: float
    longitude: float
    created_timestamp: str
    updated_timestamp: str

#!UPDATE
class BusinessUpdate(BusinessBase):
    name: str
    address: str
    city: str
    state: str
    postal_code: str
    latitude: float
    longitude: float
    created_timestamp: str
    updated_timestamp: str

#!DELETE
