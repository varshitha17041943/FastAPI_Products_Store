from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
url="mysql+mysqlconnector://root:varshithareddy%401704@localhost:3306/productfastapi"
engine=create_engine(url)
LocalSession=sessionmaker(bind=engine,autoflush=True)

