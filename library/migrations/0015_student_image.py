

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0014_auto_20210830_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
