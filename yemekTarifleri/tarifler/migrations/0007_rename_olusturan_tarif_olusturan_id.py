# Generated by Django 5.1.3 on 2024-12-09 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tarifler', '0006_alter_tarif_olusturan'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarif',
            old_name='olusturan',
            new_name='olusturan_id',
        ),
    ]
