# Generated by Django 3.2.7 on 2021-12-11 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Productname', models.CharField(max_length=100)),
                ('Productid', models.IntegerField()),
                ('Quality', models.IntegerField()),
                ('uploadimage', models.ImageField(upload_to='')),
                ('gram', models.IntegerField()),
                ('Description', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Adminregister_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminid', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=30)),
                ('password', models.CharField(max_length=10)),
                ('phoneno', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=500)),
                ('dob', models.CharField(max_length=20)),
            ],
        ),
    ]
