# Generated by Django 3.1.3 on 2020-11-26 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainadmin', '0004_auto_20201126_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageposts',
            name='image_add',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainadmin.adminpost'),
        ),
    ]
