# Generated by Django 3.1.5 on 2021-02-01 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid19', '0004_covidcases'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=10)),
                ('date', models.DateField(max_length=20)),
                ('open', models.DecimalField(decimal_places=7, max_digits=15)),
                ('high', models.DecimalField(decimal_places=7, max_digits=15)),
                ('low', models.DecimalField(decimal_places=7, max_digits=15)),
                ('close', models.DecimalField(decimal_places=7, max_digits=15)),
                ('adj_close', models.DecimalField(decimal_places=7, max_digits=15)),
                ('volume', models.PositiveIntegerField()),
            ],
            options={
                'unique_together': {('symbol', 'date')},
            },
        ),
    ]
