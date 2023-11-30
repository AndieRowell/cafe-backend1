import sqlalchemy as sa
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP, DateTime
from sqlalchemy.sql.expression import text
from app.schemas import UserInDB

from app.db.base_class import Base

#USER MODEL - PARENT
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
# add to given user model...
    created_timestamp = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
# where a profile pic would be added ---> profile_pic = Column()

# relationships
    relationship()

    def to_schema(self):
        return UserInDB(
            id=self.id,
            username=self.username,
            email=self.email,
            hashed_password=self.hashed_password,
            is_active=self.is_active,
            is_superuser=self.is_superuser
# add to given user schema
            created_timestamp=self.created_timestamp
        )
