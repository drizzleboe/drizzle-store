# Generated by Django 3.2.12 on 2022-11-07 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0029_alter_staff_uploaded_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='uploaded_on',
            field=models.DateField(auto_now=True),
        ),
    ]
