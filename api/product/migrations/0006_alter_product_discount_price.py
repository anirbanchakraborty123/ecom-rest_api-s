# Generated by Django 3.2.8 on 2021-10-26 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_product_discount_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount_price',
            field=models.FloatField(blank=True, default=True, null=True),
        ),
    ]
