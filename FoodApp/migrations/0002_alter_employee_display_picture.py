# Generated by Django 4.2.2 on 2023-06-23 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Display_picture',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='pics'),
        ),
    ]