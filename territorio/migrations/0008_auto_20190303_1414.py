# Generated by Django 2.1.7 on 2019-03-03 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('territorio', '0007_auto_20190303_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atualizacao_territorio',
            name='data_ultima_vez_trabalhado',
            field=models.DateField(null=True, verbose_name='Data da última vez trabalhado'),
        ),
    ]
