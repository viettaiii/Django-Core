"""
Script to run Django migrations
"""

import os
import sys
import django
from django.core.management import execute_from_command_line

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo_project.settings')
django.setup()

def run_migrations():
    print("Running Django migrations...")
    
    # Make migrations
    execute_from_command_line(['manage.py', 'makemigrations'])
    
    # Apply migrations
    execute_from_command_line(['manage.py', 'migrate'])
    
    print("Migrations completed successfully!")

if __name__ == '__main__':
    run_migrations()
