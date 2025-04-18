# Generated by Django 5.2 on 2025-04-18 23:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='preco_compra',
            new_name='buy_price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='categoria',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='quantidade',
            new_name='quantity',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='preco_venda',
            new_name='sale_price',
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
