# Generated by Django 3.0.8 on 2020-07-31 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0003_auto_20200731_1616'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='artistportfolio',
            unique_together=set(),
        ),
    ]
