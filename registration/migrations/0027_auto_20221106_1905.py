# Generated by Django 3.2.12 on 2022-11-06 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0026_alter_user_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emails', models.EmailField(max_length=254)),
                ('time', models.TimeField(auto_now=True)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='uploads/default-image.webp', upload_to='uploads/%Y/%m/%d/'),
        ),
    ]