# Generated by Django 4.2.13 on 2024-08-23 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientlit',
            name='dateoccupation',
            field=models.DateField(auto_now=True, default='2024-08-22'),
            preserve_default=False,
        ),
    ]
