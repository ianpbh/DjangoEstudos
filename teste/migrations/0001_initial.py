# Generated by Django 3.0.2 on 2020-01-15 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artigo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('data', models.DateTimeField(verbose_name='data de publicacao')),
            ],
        ),
        migrations.CreateModel(
            name='ImagemArtigo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=100)),
                ('ativo', models.IntegerField(default=0)),
                ('artigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teste.Artigo')),
            ],
        ),
    ]
