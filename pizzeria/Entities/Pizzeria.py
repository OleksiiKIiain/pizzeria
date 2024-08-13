from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from pizzeria.Entities.base import Base


class Pizzeria(Base):
    __tablename__="pizzarias"

    id =Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String)
    location = Column(String)

    categories = relationship("Category", back_populates="pizzeria")