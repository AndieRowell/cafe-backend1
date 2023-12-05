#import sqlalchemy as sa
from sqlalchemy import Boolean, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.sql.expression import text
# from app.schemas import UserInDB
from typing import List

from app.models.collection_tracker import CollectionTrackerDrink
from app.models.business import Business

from app.db.base_class import Base

#DRINK MODEL - PARENT
class Drink(Base):
    __tablename__ = "drinks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
#? need foreign key listed AND relationship
    business_id: Mapped[int] = mapped_column(Integer, ForeignKey("businesses.id"))

    name: Mapped[str] = Column(String, default="Name", index=True)
# where a drink image would be added ---> logo_pic = Column()
    description: Mapped[str] = Column(String, default="Description", nullable=True)
    price: Mapped[float] = Column(Float, default="Price", nullable=False)
    featured: Mapped[bool] = Column(Boolean(), default="Featured", nullable=False) #compare to is superuser?
    ordered_list_number: Mapped[str] = Column(Integer, nullable=True)
    created_timestamp: Mapped[str] = Column(DateTime(timezone=True), nullable=False, server_default=text('now()'))
    updated_timestamp: Mapped[str] = Column(DateTime(timezone=True), nullable=True, server_default=text('now()'))

# relationships
    #pivot relationship
    collection_trackers: Mapped[List["CollectionTrackerDrink"]] = relationship(back_populates="drink")
    #? foreignkey relationship to 1 business
    business: Mapped["Business"] = relationship("Business", back_populates="drinks")
