# Generated by Django 3.2.7 on 2021-11-16 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_contact_timestamp'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ('-timestamp',)},
        ),
    ]