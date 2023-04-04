# Generated by Django 4.1.7 on 2023-04-04 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0002_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acessorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'acessório',
            },
        ),
        migrations.CreateModel(
            name='Cor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'cores',
            },
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(default='', max_length=255)),
                ('ano', models.IntegerField(default=0)),
                ('preco', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='veiculo', to='garagem.categoria')),
                ('cor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='veiculo', to='garagem.cor')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='veiculo', to='garagem.marca')),
            ],
            options={
                'verbose_name': 'veículo',
            },
        ),
    ]
