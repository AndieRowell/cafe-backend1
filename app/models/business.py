import sqlalchemy as sa
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP, DateTime
from sqlalchemy.sql.expression import text
# from app.schemas import UserInDB

from app.db.base_class import Base

#USER MODEL - PARENT
class User(Base):
    __tablename__ = "businesses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String, unique=True, index=True, nullable=False)
    city = Column(String, nullable=False)
    state = Column(Boolean(), default=True)
    postal_code = Column(Boolean(), default=False)
# add to given user model...
    latitude = Column()
    longitude = Column()
    created_timestamp = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_timestamp = Column(TIMESTAMP(timezone=True), nullable=True, server_default=text('now()'))
# where a business pic would be added ---> logo_pic = Column()

# relationships
    relationship()
