# Generated by Django 3.0.4 on 2021-01-07 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platform1_0', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='hezongyy_yp',
            fields=[
                ('ID', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cj', models.CharField(max_length=100)),
                ('gg', models.CharField(max_length=100)),
                ('xq', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('price2', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'hezongyy_yp',
                'managed': True,
            },
        ),
    ]
