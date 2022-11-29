# Generated by Django 3.2.12 on 2022-11-03 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0018_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='first_name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='service',
            name='addres',
        ),
        migrations.RemoveField(
            model_name='service',
            name='cont',
        ),
        migrations.RemoveField(
            model_name='service',
            name='gend',
        ),
        migrations.RemoveField(
            model_name='service',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='service',
            name='prfssn',
        ),
        migrations.RemoveField(
            model_name='service',
            name='username',
        ),
        migrations.AddField(
            model_name='service',
            name='button',
            field=models.CharField(default='Nahitaji huduma hii', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='more',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
