

from django.db import migrations, models
import library.models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='IssuedBooks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=13)),
                ('issued_date', models.DateField(auto_now=True)),
                ('expiry_date', models.DateField(default=library.models.expiry)),
            ],
        ),
    ]
