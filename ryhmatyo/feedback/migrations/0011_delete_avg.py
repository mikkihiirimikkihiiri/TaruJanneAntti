# Generated by Django 4.1.1 on 2022-10-04 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0010_remove_avg_amount_alter_avg_avg_rating_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='avg',
        ),
    ]
