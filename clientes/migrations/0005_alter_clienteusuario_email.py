# Generated by Django 4.1.4 on 2023-03-12 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_alter_clienteusuario_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clienteusuario',
            name='email',
            field=models.EmailField(default='correo@example.com', max_length=254, unique=True, verbose_name='Correo electrónico'),
        ),
    ]