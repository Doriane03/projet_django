# Generated by Django 4.2.13 on 2024-08-28 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_alter_patient_commune_alter_patient_nationalite_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sortie',
            name='rdvdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
