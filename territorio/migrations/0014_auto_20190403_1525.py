# Generated by Django 2.1.7 on 2019-04-03 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('territorio', '0013_auto_20190329_1923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formulario',
            name='ADM',
        ),
        migrations.AddField(
            model_name='formulario',
            name='user',
            field=models.BooleanField(null=True, verbose_name='ADM'),
        ),
    ]