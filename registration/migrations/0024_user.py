# Generated by Django 3.2.12 on 2022-11-04 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0023_alter_comment_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, null=True)),
                ('last_name', models.CharField(max_length=80, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50, null='False')),
                ('time', models.TimeField(auto_now=True)),
                ('date', models.DateField(auto_now=True)),
                ('image', models.ImageField(upload_to='uploads/%Y/%m/%d/')),
                ('phone', models.CharField(max_length=13)),
            ],
        ),
    ]
