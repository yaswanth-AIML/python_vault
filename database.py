from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
db_url="Data_base_url"#give your data base url
engine=create_engine(db_url)
session=sessionmaker(autocommit=False,autoflush=False,bind=engine)
