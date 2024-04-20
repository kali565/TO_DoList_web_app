# To-Do List Web Application

## Introduction
This is a simple To-Do List web application built with Django. It allows users to manage their tasks by creating, updating, and deleting them. Additionally, users can mark tasks as completed or not completed, and filter tasks based on their completion status.

## Features
- **Create Tasks**: Users can add new tasks with a title and description.
- **View Tasks**: Tasks are displayed in a list format, showing their title, description, and completion status.
- **Update Tasks**: Users can edit existing tasks, including changing the title, description, and completion status.
- **Delete Tasks**: Users can remove tasks from the list.
- **Mark Tasks as Completed**: Users can mark tasks as completed or not completed using a checkbox.
- **Filter Tasks**: Users can filter tasks based on their completion status (completed or not completed).
- **Responsive Design**: The application is designed to work well on both desktop and mobile devices.

## Installation
To run this project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://https://github.com/kali565/TO_DoList_web_app/tree/main/todolist
    ```

2. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Apply database migrations**:
    ```bash
    python manage.py migrate
    ```

4. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

5. **Access the application**:
    Visit `http://localhost:8000` in your web browser.

## Usage
1. **Home Page**: Navigate to the home page to view your tasks or create a new one.
2. **Create Task**: Click on the "Add Task" button and fill out the form to create a new task.
3. **Update Task**: Click on the "Edit" button next to the task you want to modify, make your changes, and click "Update Task".
4. **Mark Task as Completed**: Use the checkbox provided to mark a task as completed or not completed.
5. **Delete Task**: Click on the "Delete" button next to the task you want to remove.
6. **Filter Tasks**: Use the filter dropdown to filter tasks based on their completion status.

## Contributing
Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.


