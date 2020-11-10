# Generated by Django 3.1.2 on 2020-11-10 21:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20201109_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to=settings.AUTH_USER_MODEL, verbose_name='Учитель'),
        ),
    ]
