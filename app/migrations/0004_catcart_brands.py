# Generated by Django 3.2.2 on 2021-05-14 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210515_0138'),
    ]

    operations = [
        migrations.AddField(
            model_name='catcart',
            name='brands',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
