# Generated by Django 4.2.6 on 2023-10-08 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mladoServer', '0002_alter_personaldata_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldata',
            name='permission',
            field=models.CharField(choices=[('re', 'Резидент'), ('re-p', 'Резидент-партнер'), ('admin', 'Администратор'), ('dew', 'Разработчик')], default='resident', max_length=20),
        ),
        migrations.AlterField(
            model_name='registerlist',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
