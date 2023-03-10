# Generated by Django 4.1.5 on 2023-01-23 02:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fund',
            name='image',
            field=models.ImageField(blank=True, upload_to='photos/%y/%m/%d'),
        ),
        migrations.AddField(
            model_name='fund',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
