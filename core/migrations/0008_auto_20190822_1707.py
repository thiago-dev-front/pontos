# Generated by Django 2.2.4 on 2019-08-22 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20190822_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontosturisticos',
            name='avaliacoes',
            field=models.ManyToManyField(blank=True, to='avaliacoes.Avaliacao'),
        ),
    ]