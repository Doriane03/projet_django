# Generated by Django 4.2.13 on 2024-08-30 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_sortie_rdvdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='antecedant_chirurgical',
            name='autre',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]