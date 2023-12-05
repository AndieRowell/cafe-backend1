import sqlalchemy as sa
from sqlalchemy import Boolean, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column,
from sqlalchemy.sql.sqltypes import TIMESTAMP, DateTime
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
    address: Mapped[str] = Column(String, default="Address", nullable=False) #what is unique again?
    city: Mapped[str] = Column(String, default="City", nullable=False)
    state: Mapped[bool] = Column(Boolean(), default="State" nullable=False)
    postal_code: Mapped[bool] = Column(Boolean(), default="Postal Code" nullable=False)
# add to given user model...
    latitude: Mapped[float] = Column(Float, default="Latitude", nullable=False)
    longitude: Mapped[float] = Column(Float, default="Longitude", nullable=False)
    created_timestamp: Mapped[str] = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_timestamp: Mapped[str] = Column(TIMESTAMP(timezone=True), nullable=True, server_default=text('now()'))
# where a business pic would be added ---> logo_pic = Column()

# relationships? do i need anything here or is that only in my child/pivots?

#! pivot/child
class BusinessTag (Base):
    __tablename__ = "business_tags"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    business_id: Mapped[int] = mapped_column(ForeignKey("business.id"))
    tag_id: Mapped[int] = mapped_column(ForeignKey("tag.id"))

    business: Mapped[List["Business"]] = relationship(back_populates="business")
    tag: Mapped[List["Tag"]] = relationship(back_populates="tag")

#include pivot/child table under parent and then write it opposite in the connecting parent file

#! example:
# class Parent(Base):
#     __tablename__ = "parent_table"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     child_id: Mapped[int] = mapped_column(ForeignKey("child_table.id"))
#     child: Mapped["Child"] = relationship(back_populates="parents")


# class Child(Base):
#     __tablename__ = "child_table"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     parents: Mapped[List["Parent"]] = relationship(back_populates="child")
#     parents: Mapped[List["Parent"]] = relationship(back_populates="child")
