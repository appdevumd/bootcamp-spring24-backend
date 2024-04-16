from fastapi import FastAPI

app = FastAPI()

from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

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
    number: int

class Element(BaseModel):
    number: int

@app.get('/items')
async def get_items():
    return todo_list_items

@app.post('/add')
async def add_item(item: Item):
    todo_list_items.append({'name': item.name, 'number': item.number})  # method 1
    todo_list_items.append((item.name, item.number))  # method 2
    return {'message': 'success'}


@app.delete('/remove')
async def remove_item(element: Element):
    if element.number > len(todo_list_items):
        return {'message': 'index too large'}
    else:
        todo_list_items.pop(element.number)
        return {'message': 'success'}
