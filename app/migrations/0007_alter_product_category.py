# Generated by Django 3.2.2 on 2021-05-15 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('M', 'Mobile'), ('L', 'Laptops'), ('MF', 'Men'), ('FF', 'Women'), ('ND', 'Networking Devices'), ('TV', 'TVs'), ('FU', 'Furnitures'), ('AP', 'Appliances')], max_length=3),
        ),
    ]
