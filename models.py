from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP
from datetime import datetime
from database import Base
import enum

class CategoryEnum(enum.Enum):
    finished = "finished"
    semi_finished = "semi-finished"
    raw = "raw"


class UnitEnum(enum.Enum):
    mtr = "mtr"
    mm = "mm"
    ltr = "ltr"
    ml = "ml"
    cm = "cm"
    mg = "mg"
    gm = "gm"
    unit = "unit"
    pack = "pack"
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    unit_of_measure = Column(Enum(UnitEnum))
    description = Column(String(250))
    product_image = Column(String(500)) 
    sku = Column(String(100), unique=True)
    category = Column(Enum(CategoryEnum), nullable=False)
    lead_time = Column(Integer)
    created_date = Column(TIMESTAMP, default=datetime.utcnow)
    updated_date = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
