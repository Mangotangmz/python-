# Generated by Django 2.0.7 on 2018-08-01 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backweb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atype',
            name='f_typeid',
            field=models.IntegerField(null=True),
        ),
    ]
