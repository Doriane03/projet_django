# Generated by Django 4.2.13 on 2024-10-13 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_remove_bilan_biologique_consultation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examen_physique',
            name='etat_de_conscience',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]