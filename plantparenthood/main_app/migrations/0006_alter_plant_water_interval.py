# Generated by Django 4.0.6 on 2022-09-06 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_plant_water_interval'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='water_interval',
            field=models.IntegerField(help_text='(Enter days between waterings.)'),
        ),
    ]
