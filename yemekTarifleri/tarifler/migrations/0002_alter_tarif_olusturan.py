# Generated by Django 5.1.3 on 2024-11-28 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarifler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarif',
            name='olusturan',
            field=models.CharField(max_length=50),
        ),
    ]