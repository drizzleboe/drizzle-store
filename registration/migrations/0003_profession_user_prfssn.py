# Generated by Django 4.0.3 on 2022-04-08 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_remove_user_prfssn_delete_profession'),
    ]

    operations = [
        migrations.CreateModel(
            name='profession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='prfssn',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.profession'),
        ),
    ]