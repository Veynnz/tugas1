# Generated by Django 5.1.1 on 2024-10-01 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
