# Generated by Django 4.1.7 on 2023-03-05 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0003_alter_payment_client'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sellitem',
            old_name='product_id',
            new_name='product',
        ),
    ]
