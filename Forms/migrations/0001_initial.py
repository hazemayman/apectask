# Generated by Django 3.0.5 on 2020-10-10 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=500)),
                ('MobileNumber', models.CharField(max_length=500)),
                ('Univesity', models.CharField(max_length=500)),
                ('Faculty', models.CharField(max_length=500)),
                ('Academic_year', models.CharField(max_length=500)),
                ('First_preference', models.CharField(max_length=500)),
                ('Second_preference', models.CharField(max_length=500)),
                ('Previous_experience', models.CharField(max_length=500)),
                ('Whyapec', models.CharField(max_length=500)),
                ('Hear', models.CharField(max_length=500)),
                ('First_second_pref', models.CharField(max_length=500)),
                ('Percentage', models.CharField(max_length=500)),
                ('Expect', models.CharField(max_length=500)),
                ('PersonalSkills', models.CharField(max_length=500)),
                ('ALone_team', models.CharField(max_length=500)),
                ('Schedule', models.CharField(max_length=500)),
                ('Learn', models.CharField(max_length=500)),
                ('LeaderRadio', models.CharField(max_length=500)),
                ('LeaderChar', models.CharField(max_length=500)),
            ],
        ),
    ]