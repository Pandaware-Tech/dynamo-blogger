# Generated by Django 3.2.10 on 2022-04-15 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynamo_blogger', '0003_auto_20220415_2035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='color_number',
        ),
    ]
