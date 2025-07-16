# Task Manager

A simple command-line task management system built with Python.

## Features

- ✅ Add new tasks with title, description, and priority
- 📋 View all tasks with status indicators
- ✅ Mark tasks as completed
- ✅ Delete tasks
- 🔍 Search tasks by title or description
- ✅ Persistent storage using JSON
- 🖥️ Clean command-line interface

## Installation

1. Make sure you have Python 3.7+ installed
2. Clone or download this project
3. Navigate to the project directory

## Usage

Run the application:
```bash
python main.py
```

### Menu Options

1. **Add New Task** - Create a new task with title, description, and priority
2. **View All Tasks** - Display all tasks with their current status
3. **Complete Task** - Mark a task as completed
4. **Delete Task** - Remove a task from the list
5. **Search Tasks** - Find tasks by searching title or description
6. **Exit** - Close the application

## Project Structure

```
task_manager/
├── main.py          # Main application entry point
├── tasks.py         # Task management logic
├── utils.py         # Utility functions
├── config.py        # Configuration settings
├── README.md        # This file
├── requirements.txt # Python dependencies
└── tasks.json       # Task data storage (created automatically)
```

## Configuration

Edit `config.py` to customize:
- File paths for data storage
- Task limits and validation rules
- Display settings
- Feature flags

## Development

This project is designed for learning Python development practices including:
- Code organization and modularity
- Error handling and validation
- File I/O operations
- User interface design
- Configuration management

## Contributing

This is a learning project. Feel free to experiment and modify the code to understand how it works!

## License

This project is for educational purposes.
