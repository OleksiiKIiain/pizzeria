from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from pizzeria.Entities.base import Base


class Pizza(Base):
    __tablename__="pizzas"

    id = Column(Integer,primary_key=True, autoincrement=True)
    name = Column(String ,nullable=False)
    price = Column(Float)
    category_id = Column(Integer,ForeignKey("categories.id"),nullable=False)

    category = relationship("Category",back_populates="pizzas")
