# Generated by Django 4.0.1 on 2022-02-14 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_cityonne_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cityonne',
            name='datenaissance',
            field=models.DateField(),
        ),
    ]
