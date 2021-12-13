from enum import unique
from sqlalchemy.sql.schema import PrimaryKeyConstraint
from sqlalchemy.sql.sqltypes import NullType
from database import Base
from sqlalchemy import String, Boolean, Integer, column



class user(Base):
    __tablename__ = 'usertbl'
    Id = column(Integer)
    firstname = column(String(100))
    lastname = column(String(100) )
    email = column(String(50))
    password = column(String(20))


    def __repr__(self):
        return f"<user name={self.firstname + self.lastname} email = {self.email}"