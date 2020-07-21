from django.db import models

# Create your models here.

class hezongyy_py1(models.Model):
    ID = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=100)
    cj = models.CharField(max_length=100)
    gg = models.CharField(max_length=100)
    xq = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    class Meta:
        managed = True
        db_table = 'hezongyy_py'

class ysb_lyg1(models.Model):
    ID = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=100)
    cj = models.CharField(max_length=100)
    gg = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    class Meta:
        managed = True
        db_table = 'ysb_lyg'

class longyi_tjzq1(models.Model):
    ID = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=100)
    cj = models.CharField(max_length=100)
    gg = models.CharField(max_length=100)
    xq = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    class Meta:
        managed = True
        db_table = 'longyi_tjzq'
