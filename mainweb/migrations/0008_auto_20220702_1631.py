# Generated by Django 3.2.6 on 2022-07-02 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainweb', '0007_candidates_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidates',
            name='Additional_info',
        ),
        migrations.AddField(
            model_name='candidates',
            name='additional_info',
            field=models.TextField(blank=True, null=True),
        ),
    ]
