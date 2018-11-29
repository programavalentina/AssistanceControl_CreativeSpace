# Generated by Django 2.1.2 on 2018-11-15 19:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20181115_1912'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assistance',
            fields=[
                ('IdAssistance', models.AutoField(primary_key=True, serialize=False)),
                ('Date', models.DateField(verbose_name='Date')),
                ('FKIdCourse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Course')),
            ],
        ),
        migrations.CreateModel(
            name='AssistanceList',
            fields=[
                ('IdAssistanceList', models.AutoField(primary_key=True, serialize=False)),
                ('Estate', models.BooleanField(default=False, verbose_name='1 Assistence; 0 No Assistence')),
                ('FKIdAssistance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Assistance')),
                ('FKLicence', models.ForeignKey(limit_choices_to={'FKLicenceType': 8}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]