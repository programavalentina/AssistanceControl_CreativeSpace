# Generated by Django 2.1.2 on 2018-11-10 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assistance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Estate', models.BooleanField(default=False, verbose_name='1 Assistence; 0 No Assistence')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('IdCourse', models.AutoField(primary_key=True, serialize=False)),
                ('NameCourse', models.CharField(max_length=45)),
                ('Description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ListStudents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FKIdCourse', models.ManyToManyField(to='users.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('Licence', models.AutoField(primary_key=True, serialize=False, verbose_name='Licence Student')),
                ('Name1', models.CharField(max_length=50, verbose_name='Name')),
                ('Name2', models.CharField(blank=True, max_length=50)),
                ('Name3', models.CharField(blank=True, max_length=50)),
                ('LastName1', models.CharField(blank=True, max_length=50)),
                ('LastName2', models.CharField(blank=True, max_length=50)),
                ('BirthDate', models.DateField(verbose_name='Birth Name')),
                ('Email', models.EmailField(max_length=80)),
                ('Phone', models.PositiveIntegerField(blank=True, verbose_name='Contact Phone')),
            ],
        ),
        migrations.CreateModel(
            name='StudentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.TextField()),
                ('FKLicence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Student')),
            ],
        ),
        migrations.AddField(
            model_name='liststudents',
            name='FKLicence',
            field=models.ManyToManyField(to='users.Student'),
        ),
        migrations.AddField(
            model_name='assistance',
            name='FKLicence',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Student'),
        ),
    ]
