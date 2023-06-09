# Generated by Django 4.1.7 on 2023-03-20 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrient', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crop',
            name='nutrients',
        ),
        migrations.RemoveField(
            model_name='crop',
            name='parent_crop',
        ),
        migrations.AddField(
            model_name='crop',
            name='nutrients',
            field=models.ManyToManyField(related_name='nutrienties', to='nutrient.nutrient'),
        ),
        migrations.AddField(
            model_name='crop',
            name='parent_crop',
            field=models.ManyToManyField(blank=True, null=True, related_name='sub_cropies', to='nutrient.crop'),
        ),
    ]
