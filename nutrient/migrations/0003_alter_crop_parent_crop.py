# Generated by Django 4.1.7 on 2023-03-21 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrient', '0002_remove_crop_nutrients_remove_crop_parent_crop_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crop',
            name='parent_crop',
            field=models.ManyToManyField(blank=True, related_name='sub_cropies', to='nutrient.crop'),
        ),
    ]
