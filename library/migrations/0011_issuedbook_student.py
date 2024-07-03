

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0010_remove_issuedbook_branch'),
    ]

    operations = [
        migrations.AddField(
            model_name='issuedbook',
            name='student',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
