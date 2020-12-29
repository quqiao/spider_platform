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