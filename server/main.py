from fastapi import FastAPI

app = FastAPI()

from pydantic import BaseModel  # for creating API request models

from fastapi.middleware.cors import CORSMiddleware  # for allowing cross-origin requests

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ['buy food', 'do hw']

todo_list_items = []  # things will get stored here for now

# class Item extends/implements BaseModel
class Item(BaseModel):
    name: str

class Element(BaseModel):
    number: int

@app.get('/items')
async def get_items():
    return todo_list_items

@app.post('/add')
async def add_item(item: Item):
    todo_list_items.append(item.name)
    return {'message': 'success'}

@app.delete('/remove')
async def remove_item(element: Element):
    todo_list_items.pop(element.number)
