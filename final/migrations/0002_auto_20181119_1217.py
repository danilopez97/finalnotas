# Generated by Django 2.1.3 on 2018-11-19 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('final', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignacion',
            name='nota',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
