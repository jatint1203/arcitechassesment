# Generated by Django 4.2.7 on 2023-11-14 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.CharField(max_length=10),
        ),
    ]