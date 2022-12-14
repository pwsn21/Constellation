# Generated by Django 4.1.3 on 2022-11-19 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('employeenumber', models.CharField(max_length=10, verbose_name='Employee ID')),
            ],
        ),
        migrations.CreateModel(
            name='dops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dops_date', models.DateTimeField(verbose_name='DOPS Date')),
                ('msnumber', models.IntegerField(verbose_name='Milestone Number')),
                ('comments', models.TextField(blank=True)),
                ('mentor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='milestonetracker.user')),
            ],
        ),
    ]
