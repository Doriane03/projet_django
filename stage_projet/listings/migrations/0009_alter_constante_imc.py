# Generated by Django 4.2.13 on 2024-07-24 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_sortie_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constante',
            name='imc',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]