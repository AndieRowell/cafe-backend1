import sqlalchemy as sa
from sqlalchemy import Boolean, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy.sql.sqltypes import TIMESTAMP, DateTime
from sqlalchemy.sql.expression import text
# from app.schemas import UserInDB
from typing import List

from app.models.user import UserBadge

from app.db.base_class import Base

#BADGE MODEL - PARENT
class Badge(Base):
    __tablename__ = "badges"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
# foreign key connecter to business
    title: Mapped[str] = Column(String, index=True, nullable=False)
    description: Mapped[str] = Column(String, default="Description", nullable=False)
    color_hex: Mapped[str] = Column(String, default="Color Hex Code", nullable=False)
    icon_url: Mapped[str] = Column(String, default="Icon URL", nullable=False)
    created_timestamp: Mapped[str] = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_timestamp: Mapped[str] = Column(TIMESTAMP(timezone=True), nullable=True, server_default=text('now()'))

# relationship
    users: Mapped[List["UserBadge"]] = relationship(back_populates="badge")
