# Generated by Django 4.2.1 on 2023-06-05 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curs', '0002_alter_curs_durata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curs',
            name='descriere',
            field=models.TextField(blank=True, null=True),
        ),
    ]