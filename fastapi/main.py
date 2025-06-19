from fastapi import FastAPI
app=FastAPI()
# GET, POST, PUT, DELETE
@app.get("/")
def hw():
    return {"message": "Hello World"}

items=[
    {'itemid': 1, 'name': "apple"},
    {'itemid': 2, 'name': "banana"},
    {'itemid': 3, 'name': "cherry"},
    {'itemid': 4, 'name': "dates"}, 
    {'itemid': 5, 'name': "elderberry"}
]

# Example for path parameter
# URL eg. amazon.com/items/2 will return item with itemid=2
@app.get("/items/{itemid}")
def get_items_by_id(itemid:int):
    for item in items:
        if item["itemid"] == itemid:
            return item['name']
    return {"message": "Item not found"} 

# Example for query parameter
# URL eg.  amazon.com/items?n=2 will return first 2 products
@app.get("/items")
def get_items(n:int=None):
    if n:
        return items[:n]
    else:
        return items
    
# POST method example    
@app.post('/items')
def create_item(name:str,id:int):
    newitemid=id
    newitemname=name
    newitem={'itemid':newitemid,'name':newitemname}
    items.append(newitem)
    return {newitemname+" has been added to the list"}

@app.put('/items')
def updateitem(itemid:int,updateditem:str):
    for i in items:
        if i['itemid']==itemid:
            i['name']=updateditem
    return {"Item "+str(itemid)+" has been updated"}

@app.delete('/items')
def deleteitem(id:int):
    for i,t in enumerate(items):
        if t['itemid']==id:
            deleteditems=items.pop(i)
            return {"Item has been deleted"}
    return {"Item Not found"}



