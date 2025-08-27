import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django.utils import timezone
from books.models import Author, Book

class Command(BaseCommand):
    help = 'Tạo dữ liệu mẫu cho model Author và Book'

    def handle(self, *args, **kwargs):
        # Xóa dữ liệu cũ (tùy chọn)
        Book.objects.all().delete()
        Author.objects.all().delete()

        # Tạo dữ liệu mẫu cho Author
        authors = [
            {"name": "Nguyen Van A", "email": "nguyenvana@example.com"},
            {"name": "Tran Thi B", "email": "tranthib@example.com"},
            {"name": "Le Van C", "email": "levanc@example.com"},
            {"name": "Pham Thi D", "email": "phamthid@example.com"},
            {"name": "Hoang Van E", "email": "hoangvane@example.com"},
        ]
        author_objects = [Author(**data) for data in authors]
        Author.objects.bulk_create(author_objects)
        self.stdout.write(self.style.SUCCESS(f'Tạo thành công {len(author_objects)} authors'))

        # Tạo dữ liệu mẫu cho Book
        genres = ['fiction', 'non-fiction', 'sci-fi']
        books = []
        for i in range(50):  # Tạo 50 books
            publication_date = timezone.now().date() - timedelta(days=random.randint(0, 365*5))
            book = Book(
                title=f"Book Title {i+1}",
                author=random.choice(author_objects),
                publication_date=publication_date,
                genre=random.choice(genres),
                price=round(random.uniform(10.0, 100.0), 2)
            )
            books.append(book)
        Book.objects.bulk_create(books)
        self.stdout.write(self.style.SUCCESS(f'Tạo thành công {len(books)} books'))