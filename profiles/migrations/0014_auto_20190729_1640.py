# Generated by Django 2.2.3 on 2019-07-29 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0013_auto_20190727_1645'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profiles',
            old_name='bishop',
            new_name='bacenta',
        ),
        migrations.RenameField(
            model_name='profiles',
            old_name='branch',
            new_name='centre',
        ),
        migrations.RenameField(
            model_name='profiles',
            old_name='hostel',
            new_name='hostel_address',
        ),
        migrations.RenameField(
            model_name='profiles',
            old_name='yearAppointed',
            new_name='layschool',
        ),
        migrations.RemoveField(
            model_name='profiles',
            name='Occupation',
        ),
        migrations.RemoveField(
            model_name='profiles',
            name='address',
        ),
        migrations.RemoveField(
            model_name='profiles',
            name='country',
        ),
        migrations.RemoveField(
            model_name='profiles',
            name='region',
        ),
        migrations.RemoveField(
            model_name='profiles',
            name='yearOrdained',
        ),
    ]
