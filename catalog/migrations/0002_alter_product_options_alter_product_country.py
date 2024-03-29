# Generated by Django 5.0.3 on 2024-03-19 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name', 'category', 'price'), 'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
        migrations.AlterField(
            model_name='product',
            name='country',
            field=models.CharField(blank=True, choices=[('1', 'Россия'), ('2', 'Беларусь'), ('3', 'Китай')], null=True, verbose_name='Страна производства'),
        ),
    ]
