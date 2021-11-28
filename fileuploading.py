from fastapi import FastAPI ,File ,UploadFile
from pydantic import BaseModel
from typing import Optional
app = FastAPI()
@app.post('/fileuploading')
async def root(file:UploadFile = File(...) ):
    return {'filename':file.filename}
