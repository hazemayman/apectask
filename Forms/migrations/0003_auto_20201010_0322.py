# Generated by Django 3.0.5 on 2020-10-10 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forms', '0002_auto_20201010_0318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='ALone_team',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='application',
            name='Academic_year',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='application',
            name='Expect',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='application',
            name='Faculty',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='application',
            name='First_preference',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='application',
            name='First_second_pref',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='application',
            name='Hear',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='application',
            name='LeaderChar',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='application',
            name='LeaderRadio',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='application',
            name='Learn',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='application',
            name='MobileNumber',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='application',
            name='Name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='application',
            name='Percentage',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='application',
            name='PersonalSkills',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='application',
            name='Previous_experience',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='application',
            name='Schedule',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='application',
            name='Second_preference',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='application',
            name='Univesity',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='application',
            name='Whyapec',
            field=models.TextField(max_length=1000),
        ),
    ]
