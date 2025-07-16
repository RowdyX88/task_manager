"""
Task Management Module
Handles all task-related operations
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Optional

class TaskManager:
    def __init__(self, tasks_file: str):
        self.tasks_file = tasks_file
        self.tasks = self.load_tasks()
    
    def load_tasks(self) -> List[Dict]:
        """Load tasks from file"""
        if os.path.exists(self.tasks_file):
            try:
                with open(self.tasks_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                print("Error: Corrupted tasks file. Starting fresh.")
                return []
        return []
    
    def save_tasks(self):
        """Save tasks to file"""
        with open(self.tasks_file, 'w') as f:
            json.dump(self.tasks, f, indent=2)
    
    def add_task(self):
        """Add a new task"""
        title = input("Enter task title: ").strip()
        if not title:
            print("Task title cannot be empty!")
            return
        
        description = input("Enter task description (optional): ").strip()
        priority = input("Enter priority (high/medium/low): ").strip().lower()
        
        if priority not in ['high', 'medium', 'low']:
            priority = 'medium'
        
        task = {
            'id': len(self.tasks) + 1,
            'title': title,
            'description': description,
            'priority': priority,
            'status': 'pending',
            'created_at': datetime.now().isoformat(),
            'completed_at': None
        }
        
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{title}' added successfully!")
    
    def view_tasks(self):
        """Display all tasks"""
        if not self.tasks:
            print("No tasks found.")
            return
        
        print("\n=== TASKS ===")
        for task in self.tasks:
            status_icon = "✓" if task['status'] == 'completed' else "□"
            print(f"{task['id']}. [{status_icon}] {task['title']} ({task['priority']})")
            if task['description']:
                print(f"   Description: {task['description']}")
        
        input("Press Enter to continue...")
    
    def complete_task(self):
        """Mark a task as completed"""
        self.view_tasks()
        if not self.tasks:
            return
        
        try:
            task_id = int(input("Enter task ID to complete: "))
            task = next((t for t in self.tasks if t['id'] == task_id), None)
            
            if task:
                if task['status'] == 'completed':
                    print(f"Task '{task['title']}' is already completed!")
                    return
                task['status'] = 'completed'
                task['completed_at'] = datetime.now().isoformat()
                self.save_tasks()
                print(f"Task '{task['title']}' marked as completed!")
            else:
                print("Task not found!")
        except ValueError:
            print("Invalid task ID!")
    
    def delete_task(self):
        """Delete a task"""
        self.view_tasks()
        if not self.tasks:
            return
        
        try:
            task_id = int(input("Enter task ID to delete: "))
            task = next((t for t in self.tasks if t['id'] == task_id), None)
            
            if task:
                self.tasks.remove(task)
                self.save_tasks()
                print(f"Task '{task['title']}' deleted!")
            else:
                print("Task not found!")
        except ValueError:
            print("Invalid task ID!")
    
    def search_tasks(self):
        """Search tasks by title or description"""
        query = input("Enter search term: ").strip().lower()
        if not query:
            print("Search term cannot be empty!")
            return
        
        results = []
        for task in self.tasks:
            if (query in task['title'].lower() or 
                query in task['description'].lower()):
                results.append(task)
        
        if results:
            print(f"\n=== SEARCH RESULTS ({len(results)} found) ===")
            for task in results:
                status_icon = "✓" if task['status'] == 'completed' else "□"
                print(f"{task['id']}. [{status_icon}] {task['title']} ({task['priority']})")
        else:
            print("No tasks found matching your search.")
