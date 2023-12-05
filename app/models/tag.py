import sqlalchemy as sa
from sqlalchemy import Boolean, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql.sqltypes import TIMESTAMP, DateTime
from sqlalchemy.sql.expression import text
# from app.schemas import UserInDB
from typing import List

from app.models.business import BusinessTag
from app.models.user import UserTag

from app.db.base_class import Base

#TAG MODEL - PARENT
class Tag(Base):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
# foreign key connecter to business
    title: Mapped[str] = Column(String, default="Title", nullable=False)
    description: Mapped[str] = Column(String, default="Description", nullable=False)
    color_hex: Mapped[str] = Column(String, default="Color Hex Code", nullable=False)
    icon_url: Mapped[str] = Column(String, default="Icon URL", nullable=False)
    created_timestamp: Mapped[str] = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_timestamp: Mapped[str] = Column(TIMESTAMP(timezone=True), nullable=True, server_default=text('now()'))

# relationships - connect back to child businesstag under business.py

    businesses: Mapped[List["BusinessTag"]] = relationship(back_populates="tag")
# Businesses has tag

    users: Mapped[List["UserTag"]] = relationship(back_populates="tag")
#? does this conflict anything?
