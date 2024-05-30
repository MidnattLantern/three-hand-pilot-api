# Generated by Django 3.2.25 on 2024-05-20 09:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('address_book', '0003_alter_address_contact_email'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0002_product_serial_number_prefix'),
    ]

    operations = [
        migrations.CreateModel(
            name='SerialNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('serial_number', models.CharField(max_length=50)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('partnering_end', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='address_book.address')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'ordering': ['-updated_at'],
            },
        ),
    ]