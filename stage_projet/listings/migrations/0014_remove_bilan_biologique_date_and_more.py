# Generated by Django 4.2.13 on 2024-10-24 00:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0013_remove_hospitalisationlit_lit_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bilan_biologique',
            name='date',
        ),
        migrations.RemoveField(
            model_name='bilan_biologiqueexamens',
            name='prix',
        ),
        migrations.RemoveField(
            model_name='bilan_biologiqueexamens',
            name='resultatmodalite',
        ),
        migrations.RemoveField(
            model_name='bilan_biologiqueexamens',
            name='resultatnumerique',
        ),
        migrations.RemoveField(
            model_name='hospitalisation',
            name='lit',
        ),
        migrations.RemoveField(
            model_name='ordonnance',
            name='date',
        ),
        migrations.AddField(
            model_name='bilan_biologique',
            name='prix',
            field=models.CharField(default='100', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bilan_biologique',
            name='resultatmodalite',
            field=models.CharField(default='positif', max_length=7),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bilan_biologique',
            name='resultatnumerique',
            field=models.CharField(default='122', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hospitalisationlit',
            name='lit',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='listings.lit'),
            preserve_default=False,
        ),
    ]
