# Generated by Django 2.2.3 on 2019-07-27 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0012_profiles_imagefile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='imagefile',
            field=models.FileField(null=True, upload_to='images/', verbose_name='Image'),
        ),
    ]
