from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.sql.expression import true
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:123@localhost/user_db", echo=True)

Base =  declarative_base()


sessionlocal= sessionmaker(bind=engine)
