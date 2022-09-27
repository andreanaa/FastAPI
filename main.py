from typing import Union

from fastapi import FastAPI

from pydantic import BaseModel

class Mahasiswa(BaseModel):
    NIM:int
    Name:str

app = FastAPI()
data = {}

@app.get("/")
def read_root():
    return data
    # return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

@app.post("/")
async def add_mahasiswa(m:Mahasiswa):
    data_maha = {
        "NIM": m.NIM, 
        "Name": m.Name 
    }
    data[m.NIM] = data_maha
    return {"message" : "sucess adding mahasiswa"}
    