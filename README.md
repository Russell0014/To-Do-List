# To-Do List Application

This is a simple command-line To-Do List application written in Python. It uses pandas for data manipulation and storage.

## File Structure

- `To-Do-List.py`: This is the main Python script that runs the application.
- `task.csv`: This is the CSV file where the tasks are stored.

## Installation

Before running the application, you need to install the required dependencies. You can install pandas using pip:

```bash
pip install pandas
```

## How to Use

1. Run the `To-Do-List.py` script.
2. You will be presented with a menu with the following options:
    - 'A' for add: Add a new task to the list. You will be asked to enter the task and its due date.
    - 'D' for delete: Delete a task from the list. You will be asked to enter the row number of the task to delete.
    - 'P' for print: Print all tasks.
    - 'Q' for quit: Quit the application.

## Dependencies

- Python 3
- pandas