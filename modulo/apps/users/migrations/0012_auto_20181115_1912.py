# Generated by Django 2.1.2 on 2018-11-15 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20181115_1753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assistance',
            name='FKIdCourse',
        ),
        migrations.RemoveField(
            model_name='assistance',
            name='FKLicence',
        ),
        migrations.DeleteModel(
            name='Assistance',
        ),
    ]
