# Generated by Django 3.1.3 on 2020-11-10 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contacts', '0005_auto_20201110_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmedia',
            name='url',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
