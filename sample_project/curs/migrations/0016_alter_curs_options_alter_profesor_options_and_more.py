# Generated by Django 4.2.1 on 2023-06-26 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curs', '0015_student_an'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='curs',
            options={'verbose_name_plural': 'cursuri'},
        ),
        migrations.AlterModelOptions(
            name='profesor',
            options={'verbose_name_plural': 'profesori'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['prenume', 'nume'], 'verbose_name_plural': 'studenti'},
        ),
    ]
