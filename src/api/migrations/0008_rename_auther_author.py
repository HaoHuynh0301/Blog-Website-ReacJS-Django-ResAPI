# Generated by Django 3.2.3 on 2021-06-08 07:55

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0007_auther_role'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Auther',
            new_name='Author',
        ),
    ]