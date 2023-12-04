import sqlalchemy as sa
from sqlalchemy import Boolean, Column, Integer, String, Float,
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP, DateTime
from sqlalchemy.sql.expression import text
# from app.schemas import UserInDB

from app.db.base_class import Base

#REVIEW MODEL - PARENT
class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
# foreign key connecter to user
    user_id = Column(Integer, foreign_key=True)
# foreign key connector to business
    business_id = Column(Integer, foreign_key=True)
    body = Column(String, nullable=True)
    star_rating = Column(Integer, nullable=True)
    created_timestamp = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_timestamp = Column(TIMESTAMP(timezone=True), nullable=True, server_default=text('now()'))

# relationships
    relationship()
