# ToDoList

This repository contains a complete Todo List application, which includes a backend API built with FastAPI and a frontend interface. The application allows users to create, read, update, and delete (CRUD) todo items, and it serves as a comprehensive example of a full-stack web application.

### Project Structure

- Backend: Implemented using FastAPI, providing a RESTful API for managing todo items.
- Frontend:

## Backend

The backend is built using FastAPI, a modern web framework for building APIs with Python 3.7+ based on standard Python type hints.

### Features

- Create, read, update, and delete todo items.
- In-memory storage for simplicity (future plans include integrating a real database).
- FastAPI for rapid development and automatic interactive API documentation.

### Endpoints

- `POST /todo/`: Create a new todo item.
- `GET /todo/`: Retrieve all todo items.
- `GET /todo/{id}`: Retrieve a specific todo item by its ID.
- `PUT /todo/{id}`: Update a specific todo item by its ID.
- `DELETE /todo/{id}`: Delete a specific todo item by its ID.

### Running the Backend

To run the FastAPI backend, use the following commands:
`pip install fastapi uvicorn` - Install dependencies
`uvicorn main:app --reload` - Run the application

## Fronted
