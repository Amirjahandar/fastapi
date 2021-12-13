from database import Base, engine
from models import user

print("creating database.......")


Base.metadata.create_all(engine)







