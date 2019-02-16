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