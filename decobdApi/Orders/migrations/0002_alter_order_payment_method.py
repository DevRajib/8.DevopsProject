# Generated by Django 4.0.3 on 2024-07-11 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('Cash on Delivery', 'Cash on Delivery'), ('Full Payment', 'Full Payment')], default='Full Payment', max_length=50),
        ),
    ]
