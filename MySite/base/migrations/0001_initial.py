# Generated by Django 4.0 on 2021-12-20 14:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract', models.IntegerField(verbose_name='Номер договора')),
                ('name', models.CharField(max_length=250, verbose_name='Название')),
                ('price', models.IntegerField(default=25, verbose_name='Цена')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
