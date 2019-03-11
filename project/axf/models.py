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

class User(models.Model):
   userAccount = models.CharField(max_length=20, unique=True)
   userPasswd = models.CharField(max_length=20)
   userName = models.CharField(max_length=20)
   userPhone = models.CharField(max_length=20)
   userAdderss = models.CharField(max_length=100)
   userImg = models.CharField(max_length=150)
   userRank = models.IntegerField()
   userToken = models.CharField(max_length=50)
   @classmethod
   def createuser(cls,account,passwd,name,phone,address,img,rank,token):
       u = cls(userAccount=account, userPasswd=passwd, userName=name, userPhone=phone,
               userAdderss=address, userImg=img, userRank=rank, userToken=token)
       return u

class Cart(models.Model):
    userAccount = models.CharField(max_length=20)
    productid = models.CharField(max_length=10)
    productnum = models.IntegerField()
    productprice = models.CharField(max_length=10)
    isChose = models.BooleanField(default=True)
    productimg = models.CharField(max_length=150)
    productname = models.CharField(max_length=100)
    orderid = models.CharField(max_length=20, default='0')
    isDelete = models.BooleanField(default=False)
    @classmethod
    def createcart(cls,userAccount,productid,productnum,productprice,isChose,productimg,productname,isDelete):
        c = cls(userAccount=userAccount, productid=productid, productnum=productnum, productprice=productprice,
                isChose=isChose, productimg=productimg, productname=productname, isDelete=isDelete)
        return c













