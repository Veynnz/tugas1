# Generated by Django 5.1.1 on 2024-10-01 15:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_product_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('TECH', 'Technology'), ('CLO', 'Clothes'), ('HOUSE', 'House Things'), ('MISC', 'Miscellaneous')], default='MISC', max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(5)]),
        ),
    ]
