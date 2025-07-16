#!/usr/bin/env python3
"""
Task Manager - Main Application
A simple command-line task management system
"""

from tasks import TaskManager
from utils import display_menu, get_user_input
from config import DEFAULT_TASKS_FILE

def main():
    print("=== Task Manager v1.0 ===")
    task_manager = TaskManager(DEFAULT_TASKS_FILE)
    while True:
        display_menu()
        choice = get_user_input("Enter your choice (1-6): ")
        if choice == "1":
            task_manager.add_task()
        elif choice == "2":
            task_manager.view_tasks()
        elif choice == "3":
            task_manager.complete_task()
        elif choice == "4":
            task_manager.delete_task()
        elif choice == "5":
            task_manager.search_tasks()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
