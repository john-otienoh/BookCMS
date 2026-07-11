from django.contrib.postgres.operations import TrigramExtension
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('catalog', '0004_book_tags'),   
    ]

    operations = [
        TrigramExtension(),
    ]