# API

## Project

- What Bash scripting should not be used for
- What is an API
- What is a REST API
- What are microservices
- What is the CSV format
- What is the JSON format
- Python style guide:
- Package and module name style
- Class name style
- Variable name style
- Function name style
- Constant name style
- What is CapWords or CamelCase

## Tasks

- Gather data from an API
  - Write a Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.
  - Requirements:
    - You must use urllib or requests module
    - The script must accept an integer as a parameter, which is the employee ID
    - The script must display on the standard output the employee TODO list progress in this exact format:
    - First line: Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
    - EMPLOYEE_NAME: name of the employee
    - NUMBER_OF_DONE_TASKS: number of completed tasks
    - TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of completed and non-completed tasks
    - Second and N next lines display the title of completed tasks: Tab TASK_TITLE (with 1 tabulation + 1 space before)

- Export to CSV
  - Using what you did in the task #0, extend your Python script to export data in the CSV format.
  - Requirements:
    - Records all tasks that are owned by this employee
    - Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"

- Export to JSON
  - Using what you did in the task #0, extend your Python script to export data in the JSON format.
  - Requirements:
    - Records all tasks that are owned by this employee
    - Format must be: { "USER_ID": [ {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}}, ... ]}

- Dictionary of list of dictionaries mandatory
  - Using what you did in the task #0, extend your Python script to export data in the JSON format.
  - Requirements:
    - Records all tasks from all employees
    - Format must be: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
