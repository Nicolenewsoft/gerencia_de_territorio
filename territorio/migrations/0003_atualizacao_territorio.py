# Generated by Django 2.1.7 on 2019-03-01 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('territorio', '0002_auto_20190227_1603'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atualizacao_territorio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_de_inicio', models.DateField(verbose_name='DD-MM-YYYY')),
                ('dirigente', models.CharField(max_length=30)),
                ('quadras', models.CharField(max_length=50)),
                ('data_de_termino', models.DateField(verbose_name='DD-MM-YYYY')),
            ],
        ),
    ]
