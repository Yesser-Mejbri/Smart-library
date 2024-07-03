
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_issuedbooks'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='IssuedBooks',
            new_name='IssuedBook',
        ),
    ]
