# Generated by Django 3.2.6 on 2022-07-01 20:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainweb', '0006_auto_20220702_0141'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidates',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
