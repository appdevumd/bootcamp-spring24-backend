from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = ""

# Create a new client and connect to the server
client = MongoClient(uri, tlsAllowInvalidCertificates=True)

print('testing connection')

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

print('Ran connection check')


from fastapi import FastAPI

app = FastAPI()

from pydantic import BaseModel  # for creating API request models

from fastapi.middleware.cors import CORSMiddleware  # for allowing cross-origin requests

db = client.bootcampApp
# db = client['bootcampApp']

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

# class Item extends/implements BaseModel
class Item(BaseModel):
    name: str

class Element(BaseModel):
    number: int

@app.get('/items')
async def get_items():
    collection = db.todolist
    return list(collection.find())
    # return todo_list_items

@app.post('/add')
async def add_item(item: Item):
    collection = db.todolist
    collection.insert_one(dict(item))
    return {'message': 'success'}

@app.delete('/remove')
async def remove_item(element: Element):
    collection = db.todolist
    nth_item = collection.find().skip(element.number).limit(1)
    collection.delete_one({'_id': nth_item[0]['_id']})

    return {'message': 'success'}
