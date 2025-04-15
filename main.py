# FastAPI core framework to built apis.
from fastapi import FastAPI
# BaseModle helps in validation of data.
from pydantic import BaseModel
# List 
from typing import List

app =FastAPI()

# generally two models are built to get and to post the data

class Tea(BaseModel):
    id:int
    name:str
    origin:str
    
teas : List[Tea] =[]

# The q is treated as query by server
# POST http://localhost:8000/?q=something
# If You Want q from the Request Body Instead
# You need to define a Pydantic model to receive JSON body data:
# @app.post('/')
# def test(q:str):
#     return 'hello'

@app.get('/')
def read_root():
    return {"message":"Welcome to FastApi-Basics"}

@app.get('/teas')
def get_teas():
    return teas

@app.post('/teas')
def add_tea(tea:Tea):
    teas.append(tea)
    return Tea

@app.put("/teas/{tea_id}")
def update_tea(tea_id:int,updated_tea:Tea):
    for index,tea in enumerate(teas):
        if tea.id == tea_id:
            teas[index]=update_tea
            return update_tea
    return {"error":"Tea not found!"}


@app.delete("/teas/{tea_id}")
def delete_tea(tea_id: int):
    for index, t in enumerate(teas):
        if t.id == tea_id:
            deleted = teas.pop(index)
            return deleted  
    return {"error": "Tea not found"}