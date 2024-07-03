

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_issuedbook_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='issuedbook',
            name='branch',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
