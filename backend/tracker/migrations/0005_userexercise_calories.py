# Generated by Django 5.0.6 on 2024-06-22 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_userfood_calories'),
    ]

    operations = [
        migrations.AddField(
            model_name='userexercise',
            name='calories',
            field=models.IntegerField(default=0),
        ),
    ]
