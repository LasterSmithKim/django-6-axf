from django.db import models

# Create your models here.


class Wheel(models.Model):
    img = models.CharField(max_length=150)
    name = models.CharField(max_length=20)
    trackid = models.CharField(max_length=20)


class Nav(models.Model):
    img = models.CharField(max_length=150)
    name = models.CharField(max_length=20)
    trackid = models.CharField(max_length=20)


class Mustbuy(models.Model):
    img = models.CharField(max_length=150)
    name = models.CharField(max_length=20)
    trackid = models.CharField(max_length=20)


class Shop(models.Model):
    img = models.CharField(max_length=150)
    name = models.CharField(max_length=20)
    trackid = models.CharField(max_length=20)

class MainShow(models.Model):
    trackid = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    img = models.CharField(max_length=150)
    categoryid = models.CharField(max_length=20)
    brandname = models.CharField(max_length=50)

    img1 = models.CharField(max_length=251)
    productid1 = models.CharField(max_length=10,null=True)
    childcid1 = models.CharField(max_length=20)
    longname1 = models.CharField(max_length=255)
    price1 = models.CharField(max_length=15)
    marketprice1 = models.CharField(max_length=15)

    img2 = models.CharField(max_length=251)
    productid2 = models.CharField(max_length=10,null=True)
    childcid2 = models.CharField(max_length=20)
    longname2 = models.CharField(max_length=255)
    price2 = models.CharField(max_length=15)
    marketprice2 = models.CharField(max_length=15)

    img3 = models.CharField(max_length=251)
    productid3 = models.CharField(max_length=10,null=True)
    childcid3 = models.CharField(max_length=20)
    longname3 = models.CharField(max_length=255)
    price3 = models.CharField( max_length=15)
    marketprice3 = models.CharField(max_length=15)


#market 分类模型
class FoodTypes(models.Model):
    typeid = models.CharField(max_length=10)
    typename = models.CharField(max_length=20)
    childtypenames = models.CharField(max_length=251)
    typesort = models.IntegerField()
    class Meta:
        db_table = "axf_foodtypes"


class Goods(models.Model):
    productid = models.CharField(max_length=20)
    productimg = models.CharField(max_length=255)
    productname = models.CharField(max_length=100)
    productlongname = models.CharField(max_length=200)
    isxf = models.BooleanField(default=0)
    pmdesc = models.BooleanField(default=0)
    specifics = models.CharField(max_length=40)
    price = models.FloatField()
    marketprice = models.FloatField()
    categoryid = models.IntegerField()
    childcid = models.IntegerField()
    childcidname = models.CharField(max_length=100)
    dealerid = models.CharField(max_length=30)
    storenums = models.IntegerField()
    productnum = models.IntegerField()
    class Meta:
        db_table = "axf_goods"