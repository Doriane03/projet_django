# Generated by Django 4.2.13 on 2024-07-16 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_alter_patient_nom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='sexe',
            field=models.CharField(choices=[('féminin', 'Féminin'), ('masculin', 'Masculin')], max_length=100),
        ),
    ]