from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app =FastAPI()

@app.get('/status')
async def status():
    return {"message" : "hello i am createing first api"}

@app.get('/home')
async def home():
    return {"message" : "Home "}

@app.get('/go')
async def gp():
    return {"message" : "Go "}

@app.put('/put')
async def gp():
    return {"message" : "put "}

@app.patch('/patch')
async def gp():
    return {"message" : "patch "}

my_db = []

class Course(BaseModel):
    id :int 
    name : str
    price :float
    is_early_bird : Optional[bool] = None
    
@app.get('/course')
def course():
    return my_db

@app.get('/course/{course_id}')
def get_course(course_id :int):
    course =course_id-1
    return my_db[course]

@app.post('/course')
def add_course(course :Course):
    my_db.append(course.dict())
    return my_db[-1]

@app.get('/course/{course_id}')
def delete_course(course_id:int):
    my_db.pop(course_id-1)
    return {"task":"successfully completed"}


