# Generated by Django 4.1.3 on 2022-11-18 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dops',
            name='mentor',
        ),
        migrations.AlterField(
            model_name='user',
            name='employeenumber',
            field=models.CharField(max_length=10, verbose_name='Employee ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='station',
            field=models.CharField(max_length=10, verbose_name='Station'),
        ),
    ]