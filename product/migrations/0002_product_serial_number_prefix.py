# Generated by Django 3.2.25 on 2024-05-15 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='serial_number_prefix',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
