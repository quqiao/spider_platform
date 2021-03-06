# Generated by Django 3.0.4 on 2020-12-18 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_id', models.CharField(default='', max_length=30, verbose_name='卡号')),
                ('card_user', models.CharField(default='', max_length=10, verbose_name='姓名')),
                ('add_time', models.DateField(auto_now=True, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '银行卡账户_基本信息',
                'verbose_name_plural': '银行卡账户',
            },
        ),
    ]
