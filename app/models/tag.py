import sqlalchemy as sa
from sqlalchemy import Boolean, Column, Integer, String, Float,
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP, DateTime
from sqlalchemy.sql.expression import text
# from app.schemas import UserInDB

from app.db.base_class import Base

#TAG MODEL - PARENT
class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
# foreign key connecter to business
    title = Column(String, index=True, nullable=False)
    description = Column(String, nullable=False)
    color_hex = Column(String, nullable=False)
    icon_url = Column(String, nullable=False)
    created_timestamp = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_timestamp = Column(TIMESTAMP(timezone=True), nullable=True, server_default=text('now()'))

# relationships
    relationship()
