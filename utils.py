"""
Utility functions for the Task Manager application
"""

import os
import sys
from typing import Optional

def display_menu():
    """Display the main menu"""
    print("\n" + "="*40)
    print("           TASK MANAGER MENU")
    print("="*40)
    print("1. Add New Task")
    print("2. View All Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Search Tasks")
    print("6. Exit")
    print("="*40)

def get_user_input(prompt: str) -> str:
    """Get user input with error handling"""
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        print("\nExiting...")
        sys.exit(0)

def validate_file_path(file_path: str) -> bool:
    """Validate if a file path is accessible"""
    try:
        directory = os.path.dirname(file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        return True
    except (OSError, PermissionError):
        return False

def format_timestamp(timestamp: str) -> str:
    """Format timestamp for display"""
    try:
        from datetime import datetime
        dt = datetime.fromisoformat(timestamp)
        return dt.strftime("%Y-%m-%d %H:%M")
    except ValueError:
        return timestamp

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_error(message: str):
    """Print error message with formatting"""
    print(f"❌ ERROR: {message}")

def print_success(message: str):
    """Print success message with formatting"""
    print(f"✅ {message}")

def print_warning(message: str):
    """Print warning message with formatting"""
    print(f"⚠️  WARNING: {message}")

