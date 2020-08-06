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

class longyi_yp1(models.Model):
    ID = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=100)
    cj = models.CharField(max_length=100)
    gg = models.CharField(max_length=100)
    xq = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    class Meta:
        managed = True
        db_table = 'longyi_yp'

class scjuchuang_py1(models.Model):
    ID = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=100)
    cj = models.CharField(max_length=100)
    gg = models.CharField(max_length=100)
    xq = models.CharField(max_length=100)
    price1 = models.CharField(max_length=100)
    price2 = models.CharField(max_length=100)
    price3 = models.CharField(max_length=100)
    class Meta:
        managed = True
        db_table = 'scjuchuang_py'

class ypzdw_jtj1(models.Model):
    ID = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=100)
    cj = models.CharField(max_length=100)
    gg = models.CharField(max_length=100)
    sj = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    class Meta:
        managed = True
        db_table = 'ypzdw_jtj'

class scytyy_ypzq1(models.Model):
    ID = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=100)
    cj = models.CharField(max_length=100)
    gg = models.CharField(max_length=100)
    xq = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    class Meta:
        managed = True
        db_table = 'scytyy_ypzq'