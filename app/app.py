from fastapi import FastAPI

app = FastAPI()


@app.get('/', tags=['ROOT'])
async def root() -> dict:
    return {"Ping": "Pong"}


@app.get('/todo', tags=["todos"])
async def get_todo() -> dict:
    return {'data': todos}


@app.post('/todo', tags=['todos'])
async def add_todo(todo: dict) -> dict:
    todos.append(todo)
    return {
        'data': 'Todo added successfully'
    }


@app.put("/todo/{id}", tags=["todos"])
async def update_todo(id: int, body: dict) -> dict:
    for todo in todos:
        if int((todo["id"])) == id:
            todo["activity"] = body["activity"]
            return {"data": f"Todo with id {id} was sucessfully modified"}
    return {"data": f"Todo with id {id} was not found"}


@app.delete("/todo/{id}", tags=["todos"])
async def delete_todo(id: int) -> dict:
    for todo in todos:
        if int((todo["id"])) == id:
            todos.remove(todo)
            return {"data": f"Todo with id {id} was sucessfully removed"}
    return {"data": f"Todo with id {id} was not found"}

todos = [
    {
        'id': 1,
        'activity': 'Jogging'
    },
    {
        'id': 2,
        'activity': 'Writing'
    }

]
