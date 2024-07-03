

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_student_roll_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issuedbook',
            name='branch',
        ),
    ]
