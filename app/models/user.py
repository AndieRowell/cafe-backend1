import sqlalchemy as sa
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql.sqltypes import TIMESTAMP, DateTime
from sqlalchemy.sql.expression import text
from app.schemas import UserInDB
from typing import List

from app.models.badge import Badge

from app.db.base_class import Base

#USER MODEL - PARENT
class User(Base):
    __tablename__ = "users"

#? should i not have edited to include ": Mapped[str]"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = Column(String, default="Name", nullable=False)
    username: Mapped[str] = Column(String, index=True, default="Username", nullable=False)
    email: Mapped[str] = Column(String, unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = Column(String, nullable=False)
    is_active: Mapped[bool] = Column(Boolean(), default=True)
    is_superuser: Mapped[bool] = Column(Boolean(), default=False)
# add to given user model...
    created_timestamp: Mapped[str] = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
# where a profile pic would be added ---> profile_pic = Column()

# relationship
    badges: Mapped[List["UserBadge"]] = relationship(back_populates="user")


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

#! pivot/child - user badge
#? do i need an id and is that the primary key? or just two foreign keys
class UserBadge (Base):
    __tablename__ = "user_badges"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    badge_id: Mapped[int] = mapped_column(ForeignKey("badge.id"))

# relationship
    user: Mapped["User"] = relationship(back_populates="badges")
    badge: Mapped["Badge"] = relationship(back_populates="users")

#? check if there are conflicts with having both child tables in this file
#! pivot/child - user tag
class UserTag (Base):
    __tablename__ = "user_tags"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    tag_id: Mapped[int] = mapped_column(ForeignKey("tag.id"))

# relationship
    user: Mapped["User"] = relationship(back_populates="tags")
    tag: Mapped["Badge"] = relationship(back_populates="users")
