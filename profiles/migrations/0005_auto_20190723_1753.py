# Generated by Django 2.2.3 on 2019-07-23 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20190723_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='Occupation',
            field=models.CharField(default='Doctor', max_length=120),
        ),
        migrations.AddField(
            model_name='profiles',
            name='address',
            field=models.CharField(default='null', max_length=120),
        ),
        migrations.AddField(
            model_name='profiles',
            name='bishop',
            field=models.CharField(default='Doctor', max_length=120),
        ),
        migrations.AddField(
            model_name='profiles',
            name='branch',
            field=models.CharField(default='null', max_length=120),
        ),
        migrations.AddField(
            model_name='profiles',
            name='callNumber',
            field=models.CharField(default='null', max_length=120),
        ),
        migrations.AddField(
            model_name='profiles',
            name='campus',
            field=models.CharField(default='null', max_length=120),
        ),
        migrations.AddField(
            model_name='profiles',
            name='city',
            field=models.CharField(default='null', max_length=120),
        ),
        migrations.AddField(
            model_name='profiles',
            name='country',
            field=models.CharField(default='null', max_length=120),
        ),
        migrations.AddField(
            model_name='profiles',
            name='dob',
            field=models.CharField(default='null', max_length=120),
        ),
        migrations.AddField(
            model_name='profiles',
            name='gender',
            field=models.CharField(default='null', max_length=120),
        ),
        migrations.AddField(
            model_name='profiles',
            name='hostel',
            field=models.CharField(default='null', max_length=120),
        ),
        migrations.AddField(
            model_name='profiles',
            name='lastname',
            field=models.CharField(default='null', max_length=120),
        ),
        migrations.AddField(
            model_name='profiles',
            name='maritalStatus',
            field=models.CharField(default='null', max_length=120),
        ),
        migrations.AddField(
            model_name='profiles',
            name='ministry',
            field=models.CharField(default='null', max_length=120),
        ),
        migrations.AddField(
            model_name='profiles',
            name='profession',
            field=models.CharField(default='null', max_length=120),
        ),
        migrations.AddField(
            model_name='profiles',
            name='qualification',
            field=models.CharField(default='null', max_length=120),
        ),
        migrations.AddField(
            model_name='profiles',
            name='region',
            field=models.CharField(default='null', max_length=120),
        ),
        migrations.AddField(
            model_name='profiles',
            name='whatsappNumber',
            field=models.CharField(default='null', max_length=120),
        ),
        migrations.AddField(
            model_name='profiles',
            name='yearAppointed',
            field=models.CharField(default='null', max_length=120),
        ),
        migrations.AddField(
            model_name='profiles',
            name='yearOrdained',
            field=models.CharField(default='null', max_length=120),
        ),
        migrations.AlterField(
            model_name='profiles',
            name='firstname',
            field=models.CharField(default='null', max_length=120),
        ),
    ]
