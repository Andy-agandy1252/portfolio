# Generated by Django 4.2.7 on 2024-02-02 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfoliosite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='country',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='zipcode',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
