from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import Optional
from database import sessionlocal
import models

app = FastAPI()

class user(BaseModel):
    id:int
    firstname:str
    lastname:str
    email:str
    password : str
    on_offer:bool


    class config:
        orm_mode = True


db = sessionlocal()

@app.get('/')
def index():
    return {"message":"Hello word "}


@app.get('/users', response_model=user, status_code=200)
def getallusers():
    users=db.query(models.user).all()

    return users


@app.get('/user/{user_id}', response_model=user, status_code=status.HTTP_200_OK)
def getuserbyid(user_id:int):
    user = db.query(models.user).filter(models.user.Id== user_id ).first()
    return user


@app.post('/users', response_model=user, status_code=status.HTTP_201_CREATED)
def createuser(user:user):
    newuser=models.user(
         Id = user.id,
         firstname = user.firstname,
         lastname = user.lastname,
         email = user.email,
         password = user.password
    )
    db.add(newuser)
    db.commit()

    return newuser

@app.put('/user/{user_id}', response_model=user, status_code=status.HTTP_200_OK)
def updateuser(user_id:int, user:user):
    usertoupdate=db.query(models.user).filter(models.user.Id == user_id).first()
    usertoupdate.firstname=user.firstname
    usertoupdate.lastname = user.lastname
    usertoupdate.email = user.email
    usertoupdate.password = user.password

    db.commit()
    return usertoupdate

    
@app.delete('/user/{user_id}')
def deleteuser(user_id:int):
    pass



