import random
from datetime import timedelta
from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from books.models import Author, Book
from django.core.files import File
import os

class Command(BaseCommand):
    help = 'Tạo dữ liệu mẫu cho model Author và Book'

    def handle(self, *args, **kwargs):
        fake = Faker('vi_VN')
        Book.objects.all().delete()
        Author.objects.all().delete()

        # Tạo dữ liệu mẫu cho Author
        authors = [
            Author(name=fake.name(), email=fake.email())
            for _ in range(20)
        ]
        Author.objects.bulk_create(authors)
        self.stdout.write(self.style.SUCCESS(f'Tạo thành công {len(authors)} authors'))

        # Tạo dữ liệu mẫu cho Book
        genres = ['fiction', 'non-fiction', 'sci-fi']
        statuses = ['available', 'out_of_stock', 'discontinued']
        books = []
        # Giả lập một file ảnh mẫu (tạo file tạm hoặc dùng file có sẵn)
        for _ in range(100):
            book = Book(
                title=fake.sentence(nb_words=4)[:-1],
                author=random.choice(authors),
                publication_date=timezone.now().date() - timedelta(days=random.randint(0, 365*5)),
                genre=random.choice(genres),
                price=round(random.uniform(10.0, 100.0), 2),
                status=random.choice(statuses)
            )
            books.append(book)
        Book.objects.bulk_create(books, batch_size=50)
        self.stdout.write(self.style.SUCCESS(f'Tạo thành công {len(books)} books'))