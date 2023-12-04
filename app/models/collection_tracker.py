import sqlalchemy as sa
from sqlalchemy import Boolean, Column, Integer, String, Float,
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP, DateTime
from sqlalchemy.sql.expression import text
# from app.schemas import UserInDB

from app.db.base_class import Base

#TRACKER/COLLECTION MODEL - PARENT
class Collection(Base):
    __tablename__ = "collection_tracker"

    id = Column(Integer, primary_key=True, index=True)
# foreign key connecter to business
    user_id = Column(Integer, foreign_key=True, index=True)
    title = Column(String, index=True)
# where a list image would be added ---> logo_pic = Column()
    ordered_list_number = Column(Integer, nullable=True)
    contact_info = Column(String, nullable=True)
    website_url = Column(String, nullable=True)
    instagram_handle = Column(String, nullable=True)
    event_promotion_time_start = Column(TIMESTAMP(timezone=True), nullable=True, server_default=text('now()'))
    event_promotion_time_stop = Column(TIMESTAMP(timezone=True), nullable=True, server_default=text('now()'))
    event_promotion_banner = Column(String, nullable=True)
    favorite = Column(Boolean(), nullable=False) #compare to is superuser?
    created_timestamp = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_timestamp = Column(TIMESTAMP(timezone=True), nullable=True, server_default=text('now()'))

# relationships
    relationship()
