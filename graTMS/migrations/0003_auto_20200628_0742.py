# Generated by Django 3.0.7 on 2020-06-28 07:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('graTMS', '0002_auto_20200628_0737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='last_modified_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='entry_modifiers', to=settings.AUTH_USER_MODEL),
        ),
    ]
