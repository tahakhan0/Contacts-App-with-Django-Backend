# Generated by Django 3.1.3 on 2020-11-10 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contacts', '0003_auto_20201110_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='zipcode',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
    ]