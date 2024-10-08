# Generated by Django 4.2.13 on 2024-09-05 02:23

from django.db import migrations, models
from django.utils import timezone

class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0015_alter_sortie_decesliea'),
    ]

    operations = [
        migrations.AddField(
            model_name='bilan_imagerie',
            name='date',
            field=models.DateTimeField(default=timezone.now, auto_now_add=True),
            
        ),
        migrations.AddField(
            model_name='constante',
            name='date',
            field=models.DateTimeField(default=timezone.now, auto_now_add=True),
            
        ),
        migrations.AddField(
            model_name='ordonnance',
            name='date',
            field=models.DateTimeField(default=timezone.now, auto_now_add=True),
            
        ),
        migrations.AddField(
            model_name='ordonnancemedicament',
            name='date',
            field=models.DateTimeField(default=timezone.now, auto_now_add=True),
            
        ),
    ]
