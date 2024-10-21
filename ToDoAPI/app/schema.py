from pydantic import BaseModel
from datetime import datetime

class TodoBase(BaseModel):
    name: str
    due_date: str
    description: str

class Todo(TodoBase):    
    class Config():
        from_attributes = True

class ShowTodo(BaseModel):
    id: int
    name: str
    due_date: str
    description: str
    created_at: datetime
    modified_at: datetime

    class Config():
        from_attributes = True
