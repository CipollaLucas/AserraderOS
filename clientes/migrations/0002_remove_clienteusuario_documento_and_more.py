# Generated by Django 4.1.4 on 2023-03-10 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clienteusuario',
            name='documento',
        ),
        migrations.RemoveField(
            model_name='clienteusuario',
            name='pais',
        ),
        migrations.AddField(
            model_name='clienteusuario',
            name='email',
            field=models.EmailField(default='SOME STRING', max_length=254, unique=True, verbose_name='Correo electrónico'),
        ),
        migrations.AddField(
            model_name='clienteusuario',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='clienteusuario',
            name='password',
            field=models.CharField(default=1234, max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clienteusuario',
            name='usuario_activo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='clienteusuario',
            name='usuario_administrador',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='clienteusuario',
            name='apellido',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='clienteusuario',
            name='celular',
            field=models.CharField(blank=True, max_length=30, verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='clienteusuario',
            name='cuit',
            field=models.CharField(max_length=30, unique=True, verbose_name='CUIT/CUIL'),
        ),
        migrations.AlterField(
            model_name='clienteusuario',
            name='nombre',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='clienteusuario',
            name='telefono',
            field=models.CharField(blank=True, max_length=30, verbose_name='Telefono'),
        ),
        migrations.AlterField(
            model_name='clienteusuario',
            name='usuario',
            field=models.CharField(max_length=100, unique=True, verbose_name='Nombre de usuario'),
        ),
    ]
