# Generated by Django 4.1 on 2022-08-28 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_family', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='fecha_nacimiento',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='family',
            name='peso_kg',
            field=models.IntegerField(),
        ),
    ]
