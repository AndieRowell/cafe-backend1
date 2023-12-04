import sqlalchemy as sa
from sqlalchemy import Boolean, Column, Integer, String, Float,
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP, DateTime
from sqlalchemy.sql.expression import text
# from app.schemas import UserInDB

from app.db.base_class import Base

#DRINK MODEL - PARENT
class Drink(Base):
    __tablename__ = "drinks"

    id = Column(Integer, primary_key=True, index=True)
# foreign key connecter to business
    business_id = Column(Integer, foreign_key=True, index=True)
    name = Column(String, index=True)
# where a drink image would be added ---> logo_pic = Column()
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    featured = Column(Boolean(), nullable=False) #compare to is superuser?
    ordered_list_number = Column(Integer, nullable=True)
    created_timestamp = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_timestamp = Column(TIMESTAMP(timezone=True), nullable=True, server_default=text('now()'))

# relationships
    relationship()
