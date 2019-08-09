# Generated by Django 2.2.3 on 2019-07-17 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profiles',
            name='Center',
        ),
        migrations.RemoveField(
            model_name='profiles',
            name='Firstname',
        ),
        migrations.RemoveField(
            model_name='profiles',
            name='Lastname',
        ),
        migrations.AddField(
            model_name='profiles',
            name='branch',
            field=models.TextField(default='Ashaiman'),
        ),
        migrations.AddField(
            model_name='profiles',
            name='campus',
            field=models.TextField(default='Legon'),
        ),
        migrations.AddField(
            model_name='profiles',
            name='center',
            field=models.TextField(default='Tema'),
        ),
        migrations.AddField(
            model_name='profiles',
            name='firstname',
            field=models.TextField(default='Ama'),
        ),
        migrations.AddField(
            model_name='profiles',
            name='lastname',
            field=models.TextField(default='Mensah'),
        ),
    ]
