# Generated by Django 4.2.13 on 2024-09-04 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0011_remove_consultation_histoiredemaladie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultation',
            name='motifdeconsultation',
            field=models.TextField(blank=True, null=True),
        ),
    ]