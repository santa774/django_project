# coding=utf-8
from django.db import models


class BookInfoManager(models.Manager):
    def create_book(self, btitle, bpub_date):
        book = self.create(btitle=btitle, bpub_date=bpub_date, bread=0, bcommet=0, isDelete=False)
        return book


# Create your models here.
class BookInfo(models.Model):
    """
    图书名称：btitle
    图书发布时间：bpub_date
    """
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()
    bread = models.IntegerField(default=0)
    bcommet = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)
    objects = BookInfoManager()

    class Meta():
        db_table = 'booktest_bookinfo'
        pass

    def __str__(self):
        return "%d" % self.pk


class HeroInfoManager(models.Manager):
    def create_hero(self, hname, hgender, hcontent, hbook):
        hero = self.create(hname=hname, hgender=hgender, hcontent=hcontent, hbook=hbook, isDelete=False)
        return hero


class HeroInfo(models.Model):
    """
    英雄姓名：hname
    英雄性别：hgender
    英雄简介：hcontent
    所属图书：hbook
    """
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=100)
    hbook = models.ForeignKey("BookInfo")
    isDelete = models.BooleanField(default=False)
    objects = HeroInfoManager()

    class Meta():
        """
        模型的元数据，可以设置模型在数据库表中的名称，设置排序方式等等
        """
        # 表名 推荐使用：应用名_模型名 格式
        db_table = 'booktest_heroinfo'

    def gender(self):
        if self.hgender:
            return "男"
        else:
            return "女"

    def __str__(self):
        return "%d" % self.pk
