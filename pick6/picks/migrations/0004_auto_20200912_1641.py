# Generated by Django 3.1.1 on 2020-09-12 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picks', '0003_auto_20200912_1637'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Team',
            new_name='Selections',
        ),
    ]
