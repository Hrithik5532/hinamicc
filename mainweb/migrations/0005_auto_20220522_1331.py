# Generated by Django 3.0.5 on 2022-05-22 08:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainweb', '0004_subcribeusers'),
    ]

    operations = [
        migrations.AddField(
            model_name='ipmodel',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='scrapbookimg',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='ipmodel',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='scrapbook',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='scrapbookimg',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='subcribeusers',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='subcribeusers',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
