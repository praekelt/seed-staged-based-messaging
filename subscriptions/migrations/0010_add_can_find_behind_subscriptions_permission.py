# Generated by Django 2.1.2 on 2018-11-27 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0009_auto_20181126_1111'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='behindsubscription',
            options={'permissions': (('can_find_behind_subscriptions', 'Can find behind subscriptions'),)},
        ),
    ]
