"""
Configuration settings for the Task Manager application
"""

import os
from pathlib import Path

# Application settings
APP_NAME = "Task Manager"
APP_VERSION = "1.0.0"
APP_AUTHOR = "Learning Project"

# File paths
DEFAULT_TASKS_FILE = "tasks.json"
BACKUP_TASKS_FILE = "tasks_backup.json"
LOG_FILE = "task_manager.log"

# Task settings
MAX_TITLE_LENGTH = 100
MAX_DESCRIPTION_LENGTH = 500
VALID_PRIORITIES = ['high', 'medium', 'low']
DEFAULT_PRIORITY = 'medium'

# Display settings
MENU_WIDTH = 40
MAX_TASKS_PER_PAGE = 10

# Date and time formats
DATE_FORMAT = "%Y-%m-%d"
TIME_FORMAT = "%H:%M:%S"
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

# Colors for terminal output (if supported)
COLORS = {
    'success': '\033[92m',  # Green
    'error': '\033[91m',    # Red
    'warning': '\033[93m',  # Yellow
    'info': '\033[94m',     # Blue
    'reset': '\033[0m'      # Reset
}

# Feature flags
ENABLE_BACKUP = True
ENABLE_LOGGING = True
ENABLE_COLORS = True

def get_app_directory():
    """Get the application directory"""
    return Path(__file__).parent.absolute()

def get_tasks_file_path():
    """Get the full path to the tasks file"""
    return get_app_directory() / DEFAULT_TASKS_FILE

def get_backup_file_path():
    """Get the full path to the backup file"""
    return get_app_directory() / BACKUP_TASKS_FILE

def get_log_file_path():
    """Get the full path to the log file"""
    return get_app_directory() / LOG_FILE
