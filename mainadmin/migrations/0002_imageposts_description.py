# Generated by Django 3.1.3 on 2020-11-26 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainadmin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageposts',
            name='description',
            field=models.CharField(default='sdfs', max_length=150),
            preserve_default=False,
        ),
    ]
