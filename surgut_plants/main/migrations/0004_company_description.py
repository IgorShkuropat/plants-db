# Generated by Django 3.2.3 on 2021-05-28 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210528_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='description',
            field=models.TextField(default=0, max_length=100, verbose_name='Описание'),
            preserve_default=False,
        ),
    ]
