# Generated by Django 3.1.1 on 2020-10-03 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20201003_1709'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]