# Generated by Django 4.2.6 on 2023-10-08 20:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mladoServer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldata',
            name='phone',
            field=models.IntegerField(help_text='Номер телефона', validators=[django.core.validators.MaxValueValidator(89999999999)]),
        ),
    ]
