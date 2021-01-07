from django.db import models

# Create your models here.

"""用于django admin中"""
class Test(models.Model):
    name = models.CharField(max_length=20)

class Contact(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    email = models.EmailField()
    def __unicode__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    def __unicode__(self):
        return self.name

class Tag(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, )
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

"""用于接口创建中"""
# class Card(models.Model):
#     card_id = models.CharField(max_length=30, verbose_name="卡号", default="")
#     card_user = models.CharField(max_length=10, verbose_name="姓名", default="")
#     add_time = models.DateField(auto_now=True, verbose_name="添加时间")
#
#     class Meta:
#         verbose_name_plural = '银行卡账户'
#         verbose_name = "银行卡账户_基本信息"
#
#     def __str__(self):
#         return self.card_id

"""ORM单表实例"""
class NBA_data(models.Model):
    id = models.AutoField(primary_key=True)  # id会自动创建，可以手动写入
    qy = models.CharField(max_length=32)  # 球员名称
    ccrq = models.CharField(max_length=32)  # 球员出场时间
    df = models.IntegerField()  # 得分
    zg = models.IntegerField()  # 助攻
    lb = models.IntegerField()  # 篮板

"""ORM多表实例"""
class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pub_date = models.DateField()
    publish = models.ForeignKey('Publish', on_delete=models.CASCADE)
    authors = models.ManyToManyField('Author')

class Publish(models.Model):
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=64)
    email = models.EmailField()

class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.SmallIntegerField()
    au_detail = models.OneToOneField("AuthorDetail", on_delete=models.CASCADE)

class AuthorDetail(models.Model):
    gender_choices = (
        (0, "女"),
        (1, "男"),
        (2, "保密"),
    )
    gender = models.SmallIntegerField(choices=gender_choices)
    tel = models.CharField(max_length=32)
    addr = models.CharField(max_length=64)
    birthday = models.DateField()

"""cookie与session"""
class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)



