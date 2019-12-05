# Generated by Django 2.2.6 on 2019-12-03 16:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=100)),
                ('idade', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=50)),
                ('logradouro', models.CharField(max_length=100)),
                ('numero', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Procedimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
                ('valor', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Dentista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crm', models.CharField(max_length=20)),
                ('nome', models.CharField(max_length=100)),
                ('idade', models.CharField(max_length=100)),
                ('endereco', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pwII.Endereco')),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atendida', models.CharField(choices=[('1', 'Atendido'), ('2', 'Aberto'), ('3', 'Cancelado')], default='2', max_length=1)),
                ('dataConsulta', models.DateField()),
                ('horaConsulta', models.TimeField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultas', to='pwII.Cliente')),
                ('dentista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultas2', to='pwII.Dentista')),
                ('procedimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='procedimento_fk', to='pwII.Procedimento')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='endereco',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pwII.Endereco'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
