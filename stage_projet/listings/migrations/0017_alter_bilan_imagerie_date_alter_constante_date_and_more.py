# Generated by Django 4.2.13 on 2024-09-08 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0016_bilan_imagerie_date_constante_date_ordonnance_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bilan_imagerie',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='constante',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='ordonnance',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='ordonnancemedicament',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
