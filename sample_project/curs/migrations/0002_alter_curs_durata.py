# Generated by Django 4.2.1 on 2023-06-05 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curs',
            name='durata',
            field=models.IntegerField(default=80),
        ),
    ]
