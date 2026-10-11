from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,Float

Base= declarative_base()

class Product(Base):
    __tablename__ = "products"
    product_id= Column(Integer, primary_key=True, index=True)
    product_name = Column(String(100), nullable=False)
    product_price = Column(Float(10, 2), nullable=False)
    product_image_url = Column(String(500), nullable=True)
