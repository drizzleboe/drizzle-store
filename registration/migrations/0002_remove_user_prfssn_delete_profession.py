# Generated by Django 4.0.3 on 2022-04-08 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='prfssn',
        ),
        migrations.DeleteModel(
            name='profession',
        ),
    ]
