# Generated by Django 4.0.5 on 2022-07-20 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0005_delete_paymentgateway'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Brand',
            new_name='Merch',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='brand',
            new_name='merch',
        ),
    ]
