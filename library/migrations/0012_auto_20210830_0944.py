

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0011_issuedbook_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issuedbook',
            old_name='student',
            new_name='student_id',
        ),
    ]
