# Generated by Django 4.2.13 on 2024-08-30 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_antecedant_chirurgical_autre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antecedant_chirurgical',
            name='autre',
            field=models.TextField(blank=True, null=True),
        ),
    ]