# Generated by Django 3.2.12 on 2022-11-04 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0020_auto_20221103_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='time',
            field=models.TimeField(auto_now=True),
        ),
    ]
