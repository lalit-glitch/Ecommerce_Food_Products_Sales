# Generated by Django 3.2.7 on 2021-12-11 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Owner', '0002_alter_adminmodel_uploadimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminmodel',
            name='uploadimage',
            field=models.ImageField(upload_to=None),
        ),
    ]