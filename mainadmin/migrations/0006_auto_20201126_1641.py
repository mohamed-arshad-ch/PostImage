# Generated by Django 3.1.3 on 2020-11-26 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainadmin', '0005_auto_20201126_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageposts',
            name='image_add',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adminposts', to='mainadmin.adminpost'),
        ),
    ]