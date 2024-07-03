

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_issuedbook_branch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issuedbook',
            name='user',
        ),
    ]
