# Generated by Django 4.0.1 on 2022-12-08 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_alter_category_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogs',
            old_name='tarih',
            new_name='date',
        ),
    ]
