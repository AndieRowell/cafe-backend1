#import sqlalchemy as sa
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.sql.expression import text
from typing import List
# from app.schemas import UserInDB
from app.models.tag import Tag

from app.db.base_class import Base

#BUSINESS MODEL - PARENT
class Business(Base):
    __tablename__ = "businesses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = Column(String, default="Name", nullable=False)
    address: Mapped[str] = Column(String, default="Address", nullable=False)
    city: Mapped[str] = Column(String, default="City", nullable=False)
    state: Mapped[str] = Column(String(), default="State", nullable=False)
    postal_code: Mapped[str] = Column(String(), default="Postal Code", nullable=False)
# add to given user model...
    latitude: Mapped[float] = Column(Float, nullable=False)
    longitude: Mapped[float] = Column(Float, nullable=False)
    created_timestamp: Mapped[str] = Column(DateTime(timezone=True), nullable=False, server_default=text('now()')) #change to DateTime?
    updated_timestamp: Mapped[str] = Column(DateTime(timezone=True), nullable=True, server_default=text('now()')) #change to DateTime?
# where a business pic would be added ---> logo_pic = Column()

# relationships? do i need anything here or is that only in my child/pivots?
    tags: Mapped[List["BusinessTag"]] = relationship(back_populates="business")
    #BusinessTag refers to child class
    #businesses refers to businesses relationship under child

#! pivot/child
class BusinessTag (Base):
    __tablename__ = "business_tags"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    business_id: Mapped[int] = mapped_column(ForeignKey("business.id"))
    tag_id: Mapped[int] = mapped_column(ForeignKey("tag.id"))

# relationship
    business: Mapped["Business"] = relationship(back_populates="tags")
    tag: Mapped["Tag"] = relationship(back_populates="businesses")
    #tag has businesses relationship
