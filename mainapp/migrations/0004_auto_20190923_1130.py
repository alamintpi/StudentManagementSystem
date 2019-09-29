# Generated by Django 2.1.5 on 2019-09-23 05:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20190830_0029'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='Name',
            new_name='FirstName',
        ),
        migrations.AddField(
            model_name='student',
            name='LastName',
            field=models.CharField(default=django.utils.timezone.now, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.TextField(default=datetime.datetime(2019, 9, 23, 5, 29, 36, 503928, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default=datetime.datetime(2019, 9, 23, 5, 29, 48, 727614, tzinfo=utc), max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='village',
            field=models.CharField(default=datetime.datetime(2019, 9, 23, 5, 30, 8, 647555, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]