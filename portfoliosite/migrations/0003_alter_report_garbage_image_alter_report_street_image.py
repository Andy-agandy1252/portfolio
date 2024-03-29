# Generated by Django 4.2.7 on 2024-03-04 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfoliosite', '0002_alter_report_garbage_image_alter_report_street_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='garbage_image',
            field=models.ImageField(default='', upload_to='garbage_images/'),
        ),
        migrations.AlterField(
            model_name='report',
            name='street_image',
            field=models.ImageField(default='', upload_to='street_images/'),
        ),
    ]
