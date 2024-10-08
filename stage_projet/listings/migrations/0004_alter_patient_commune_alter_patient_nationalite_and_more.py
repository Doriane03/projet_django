# Generated by Django 4.2.13 on 2024-08-26 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_remove_patient_numerodelit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='commune',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='patient',
            name='nationalite',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='patient',
            name='quartier',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sexe',
            field=models.CharField(choices=[('féminin', 'féminin'), ('masculin', 'masculin')], max_length=10),
        ),
        migrations.AlterField(
            model_name='patient',
            name='situation_matrimoniale',
            field=models.CharField(max_length=12),
        ),
    ]
