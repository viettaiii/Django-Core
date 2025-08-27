"""
Script to create demo data for the Django Core Table Demo
Run this after running migrations to populate the database with sample data.
"""

import os
import sys
import django
from django.contrib.auth import get_user_model
from decimal import Decimal
from datetime import datetime, timedelta
import random

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo_project.settings')
django.setup()

from products.models import Category, Product

User = get_user_model()

def create_demo_data():
    print("Creating demo data...")
    
    # Create superuser if it doesn't exist
    if not User.objects.filter(username='admin').exists():
        admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin123'
        )
        print("Created admin user (username: admin, password: admin123)")
    else:
        admin_user = User.objects.get(username='admin')
    
    # Create sample users
    sample_users = [
        {'username': 'john_doe', 'email': 'john@example.com', 'first_name': 'John', 'last_name': 'Doe'},
        {'username': 'jane_smith', 'email': 'jane@example.com', 'first_name': 'Jane', 'last_name': 'Smith'},
        {'username': 'bob_wilson', 'email': 'bob@example.com', 'first_name': 'Bob', 'last_name': 'Wilson'},
        {'username': 'alice_brown', 'email': 'alice@example.com', 'first_name': 'Alice', 'last_name': 'Brown'},
        {'username': 'charlie_davis', 'email': 'charlie@example.com', 'first_name': 'Charlie', 'last_name': 'Davis'},
    ]
    
    for user_data in sample_users:
        if not User.objects.filter(username=user_data['username']).exists():
            user = User.objects.create_user(
                username=user_data['username'],
                email=user_data['email'],
                first_name=user_data['first_name'],
                last_name=user_data['last_name'],
                password='password123'
            )
            # Randomly set some users as inactive
            if random.choice([True, False, False, False]):  # 25% chance
                user.is_active = False
                user.save()
    
    print(f"Created {len(sample_users)} sample users")
    
    # # Create categories
    # categories_data = [
    #     {'name': 'Electronics', 'description': 'Electronic devices and gadgets'},
    #     {'name': 'Clothing', 'description': 'Apparel and fashion items'},
    #     {'name': 'Books', 'description': 'Books and educational materials'},
    #     {'name': 'Home & Garden', 'description': 'Home improvement and gardening supplies'},
    #     {'name': 'Sports', 'description': 'Sports equipment and accessories'},
    #     {'name': 'Toys', 'description': 'Toys and games for all ages'},
    # ]
    
    # categories = []
    # for cat_data in categories_data:
    #     category, created = Category.objects.get_or_create(
    #         name=cat_data['name'],
    #         defaults={'description': cat_data['description']}
    #     )
    #     categories.append(category)
    
    # print(f"Created {len(categories)} categories")
    
    # # Create products
    # products_data = [
    #     # Electronics
    #     {'name': 'Smartphone Pro Max', 'price': 999.99, 'category': 'Electronics'},
    #     {'name': 'Wireless Headphones', 'price': 199.99, 'category': 'Electronics'},
    #     {'name': 'Laptop Computer', 'price': 1299.99, 'category': 'Electronics'},
    #     {'name': 'Smart Watch', 'price': 299.99, 'category': 'Electronics'},
    #     {'name': 'Tablet Device', 'price': 499.99, 'category': 'Electronics'},
        
    #     # Clothing
    #     {'name': 'Cotton T-Shirt', 'price': 19.99, 'category': 'Clothing'},
    #     {'name': 'Denim Jeans', 'price': 79.99, 'category': 'Clothing'},
    #     {'name': 'Running Shoes', 'price': 129.99, 'category': 'Clothing'},
    #     {'name': 'Winter Jacket', 'price': 199.99, 'category': 'Clothing'},
    #     {'name': 'Baseball Cap', 'price': 24.99, 'category': 'Clothing'},
        
    #     # Books
    #     {'name': 'Python Programming Guide', 'price': 39.99, 'category': 'Books'},
    #     {'name': 'Django Web Development', 'price': 49.99, 'category': 'Books'},
    #     {'name': 'Data Science Handbook', 'price': 59.99, 'category': 'Books'},
    #     {'name': 'Machine Learning Basics', 'price': 44.99, 'category': 'Books'},
        
    #     # Home & Garden
    #     {'name': 'Garden Hose', 'price': 29.99, 'category': 'Home & Garden'},
    #     {'name': 'Tool Set', 'price': 89.99, 'category': 'Home & Garden'},
    #     {'name': 'Plant Pot Set', 'price': 34.99, 'category': 'Home & Garden'},
        
    #     # Sports
    #     {'name': 'Basketball', 'price': 24.99, 'category': 'Sports'},
    #     {'name': 'Tennis Racket', 'price': 79.99, 'category': 'Sports'},
    #     {'name': 'Yoga Mat', 'price': 39.99, 'category': 'Sports'},
        
    #     # Toys
    #     {'name': 'Building Blocks Set', 'price': 49.99, 'category': 'Toys'},
    #     {'name': 'Remote Control Car', 'price': 69.99, 'category': 'Toys'},
    #     {'name': 'Board Game Collection', 'price': 34.99, 'category': 'Toys'},
    # ]
    
    # stock_statuses = ['in_stock', 'low_stock', 'out_of_stock']
    # users = list(User.objects.all())
    
    # for prod_data in products_data:
    #     category = Category.objects.get(name=prod_data['category'])
        
    #     if not Product.objects.filter(name=prod_data['name']).exists():
    #         Product.objects.create(
    #             name=prod_data['name'],
    #             description=f"High-quality {prod_data['name'].lower()} from our {category.name.lower()} collection.",
    #             price=Decimal(str(prod_data['price'])),
    #             category=category,
    #             stock_status=random.choice(stock_statuses),
    #             is_active=random.choice([True, True, True, False]),  # 75% active
    #             created_by=random.choice(users),
    #         )
    
    # print(f"Created {len(products_data)} products")
    print("\nDemo data creation complete!")
    print("\nYou can now:")
    print("1. Run the development server: python manage.py runserver")
    print("2. Visit http://127.0.0.1:8000/ to see the demo")
    print("3. Login to admin at http://127.0.0.1:8000/admin/ (admin/admin123)")

if __name__ == '__main__':
    create_demo_data()
