# Todo API with FastAPI

This project demonstrates how to create a simple Todo API using FastAPI. The API allows users to perform CRUD (Create, Read, Update, Delete) operations on a list of Todo items. This is a great starting point for understanding API development with FastAPI and Pydantic for data validation. Future plans include integrating a real database for persistent storage.

### Task Description:

The task involves the following steps:

1. Define the Todo Model
   - Create a Pydantic `BaseModel` named `Todo` with the fields: `name`, `due_date`, and `description`.
2. Create FastAPI Application
   - Initialize a FastAPI application with the title "Todo API" and version "V1".
3. Set Up In-Memory Storage
   - Use an in-memory list, `store_todo`, to store the Todo items.
4. Implement CRUD Operations
   - Create Todo: Define a POST endpoint `/todo/` to create a new Todo item.
   - Read All Todos: Define a GET endpoint `/todo/` to retrieve all Todo items.
   - Read Single Todo: Define a GET endpoint `/todo/{id}` to retrieve a specific Todo item by its index.
   - Update Todo: Define a PUT endpoint `/todo/{id}` to update a specific Todo item by its index.
   - Delete Todo: Define a DELETE endpoint `/todo/{id}` to delete a specific Todo item by its index.
   - Include error handling for non-existent Todo items using HTTP exceptions.

### Future Plans

- Integrate a real database for persistent storage of Todo items.
- Add authentication and authorization mechanisms.
- Implement additional features such as filtering and searching Todo items.
