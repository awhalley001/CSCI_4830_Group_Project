# Generated by Django 4.1.2 on 2022-11-30 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yard_capacity', '0003_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='current_yard_circ_7',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='posts',
            name='dest_track',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='posts',
            name='equipment_number',
            field=models.IntegerField(),
        ),
    ]
