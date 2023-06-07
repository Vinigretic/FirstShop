# Generated by Django 4.2.1 on 2023-05-26 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_category_options_alter_product_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_uk',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='category_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='category_uk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_uk',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_en',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_uk',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
    ]
