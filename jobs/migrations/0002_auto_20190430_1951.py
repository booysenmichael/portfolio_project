# Generated by Django 2.1.7 on 2019-04-30 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='image',
            new_name='imagefun',
        ),
    ]
