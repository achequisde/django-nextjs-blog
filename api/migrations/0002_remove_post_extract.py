# Generated by Django 4.2.3 on 2023-07-22 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='extract',
        ),
    ]