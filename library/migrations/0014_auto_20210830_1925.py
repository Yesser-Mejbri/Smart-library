

from django.db import migrations, models
import library.models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0013_auto_20210830_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuedbook',
            name='expiry_date',
            field=models.DateField(default=library.models.expiry),
        ),
        migrations.AlterField(
            model_name='issuedbook',
            name='issued_date',
            field=models.DateField(auto_now=True),
        ),
    ]
