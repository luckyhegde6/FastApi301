from ast import List
from fastapi import FastAPI
from model import Todo

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "fastApi-301"}

todos = []

# Get All Todos
@app.get("/todos")
async def get_todos():
    return {"todos": todos}
# Get Single todos
@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo":todo}
    return {"message": "id not found"}
# Create a Todo
@app.post("/todos")
async def create_todo(todo : Todo):
    todos.append(todo)
    return {"message": f"Todo has been added with id - {todo.id}"}

# Update a Todo
@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, todo_obj: Todo):
    for todo in todos:
        if todo.id == todo_id:
            todo.id = todo_id
            todo.item = todo_obj.item
            return {"todo":todo}
    return {"message": "id not found"}

# Delete a Todo
@app.delete("/todos/{todo_id}")
async def delete_todo(id: int):
    for todo in todos:
        if todo.id == id:
            todos.remove(todo)
            return {"message":f"todo with id - {id}, item -{todo.item} has been deleted"}
    return {"message": "id not found"}