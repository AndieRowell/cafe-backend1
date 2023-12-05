import sqlalchemy as sa
from sqlalchemy import Boolean, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy.sql.sqltypes import TIMESTAMP, DateTime
from sqlalchemy.sql.expression import text
# from app.schemas import UserInDB
from typing import List

from app.models.collection_tracker import CollectionTrackerDrink

from app.db.base_class import Base

#DRINK MODEL - PARENT
class Drink(Base):
    __tablename__ = "drinks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
#? do i connect foreign key connecter to business or is that only in relationship?
    business_id = Column(Integer, foreign_key=True, index=True)

    name: Mapped[str] = Column(String, default="Name", index=True)
# where a drink image would be added ---> logo_pic = Column()
    description: Mapped[str] = Column(String, default="Description", nullable=True)
    price: Mapped[float] = Column(Float, default="Price", nullable=False)
    featured: Mapped[bool] = Column(Boolean(), default="Featured", nullable=False) #compare to is superuser?
    ordered_list_number: Mapped[str] = Column(Integer, nullable=True)
    created_timestamp: Mapped[str] = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_timestamp: Mapped[str] = Column(TIMESTAMP(timezone=True), nullable=True, server_default=text('now()'))

# relationships
    collection_trackers: Mapped[List["CollectionTrackerDrink"]] = relationship(back_populates="drink")
