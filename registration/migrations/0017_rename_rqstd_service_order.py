# Generated by Django 3.2.12 on 2022-11-02 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0016_rqstd_service_staff'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='rqstd_service',
            new_name='order',
        ),
    ]
