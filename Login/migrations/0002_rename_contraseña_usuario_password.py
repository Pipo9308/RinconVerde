# Generated by Django 5.0.6 on 2024-06-28 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='contraseña',
            new_name='password',
        ),
    ]
