from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from pizzeria.Entities.base import Base


class Category(Base):
    __tablename__="categories"

    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String,nullable = False)
    pizzeria_id = Column(Integer,ForeignKey('pizzarias.id'),nullable=False)

    pizzeria=relationship("Pizzeria", back_populates="categories")
    pizzas = relationship("Pizza", back_populates="category")