from django.shortcuts import render
from .models import Wheel, Nav, Mustbuy,Shop,MainShow

# Create your views here.

def home(request):
    wheelList = Wheel.objects.all()
    navList = Nav.objects.all()
    mustbuyList = Mustbuy.objects.all()

    shopList = Shop.objects.all()
    shop_img = shopList[0]
    shop_1_3 = shopList[1:3]
    shop_3_7 = shopList[3:7]
    shop_7_11 = shopList[7:11]

    main_shows = MainShow.objects.all()

    return render(request, 'axf/home.html',{'title':'主页','wheelList':wheelList,'navList':navList,'mustbuyList':mustbuyList,
                                            'shop_img':shop_img,'shop_1_3':shop_1_3,'shop_3_7':shop_3_7,'shop_7_11':shop_7_11,
                                            'main_shows':main_shows})


def market(request):
    return render(request, 'axf/market.html',{'title':'闪送超市'})


def cart(request):
    return render(request, 'axf/cart.html',{'title':'购物车'})


def mine(request):
    return render(request, 'axf/mine.html',{'title':'我的'})
