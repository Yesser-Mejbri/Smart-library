# Generated by Django 4.2.8 on 2023-12-12 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0015_student_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, upload_to='books/'),
        ),
    ]