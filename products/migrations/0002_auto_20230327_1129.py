# Generated by Django 3.2 on 2023-03-27 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='watchesfor',
            options={'verbose_name_plural': 'WatchesFor'},
        ),
        migrations.AlterField(
            model_name='product',
            name='Watches_For',
            field=models.ForeignKey(blank=True, choices=[('MEN', 'Men'), ('WOMEN', 'Women'), ('CHILDREN', 'Children')], null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.watchesfor'),
        ),
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.DecimalField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], decimal_places=2, max_digits=6, null=True),
        ),
    ]
