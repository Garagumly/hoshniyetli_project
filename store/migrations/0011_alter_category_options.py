# Generated by Django 4.1 on 2023-04-23 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_category_remove_brand_category_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'children'},
        ),
    ]
