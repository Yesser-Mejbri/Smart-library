

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0005_student_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='issuedbook',
            name='user',
            field=models.OneToOneField(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
