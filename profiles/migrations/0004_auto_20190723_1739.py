# Generated by Django 2.2.3 on 2019-07-23 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20190723_1733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profiles',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='profiles',
            name='campus',
        ),
        migrations.RemoveField(
            model_name='profiles',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='profiles',
            name='region',
        ),
    ]
