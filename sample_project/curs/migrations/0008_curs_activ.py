# Generated by Django 4.2.1 on 2023-06-05 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curs', '0007_curs_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='curs',
            name='activ',
            field=models.BooleanField(default=True),
        ),
    ]
