# Generated by Django 3.0.8 on 2020-07-25 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200724_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='banner_img',
            field=models.ImageField(blank=True, null=True, upload_to='accounts/banner_img'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='prof_img',
            field=models.ImageField(blank=True, null=True, upload_to='accounts/profile_img'),
        ),
    ]