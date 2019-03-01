from django.shortcuts import render
from .models import Wheel, Nav, Mustbuy,Shop,MainShow,FoodTypes,Goods
from .forms.login import LoginForm
from django.http import HttpResponse
from django.shortcuts import redirect

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


def market(request,categeryid,cid,sortid):
    leftSlider = FoodTypes.objects.all()
    if cid == '0':
        productList = Goods.objects.filter(categoryid=categeryid)
    else:
        productList = Goods.objects.filter(categoryid=categeryid).filter(childcid=cid)

    #排序
    if sortid == '1':
        productList = productList.order_by('productnum')
    elif sortid == '2':
        productList = productList.order_by('price')
    elif sortid == '3':
        productList = productList.order_by('-price')



    group = leftSlider.get(typeid = categeryid)
    childList = []
    #数据样式 ：全部分类:0#酸奶乳酸菌:103537#牛奶豆浆:103538#面包蛋糕:103540
    childnames = group.childtypenames
    arr1 = childnames.split("#")
    for str in arr1:
    #用#切割后的数据： 全部分类: 0     酸奶乳酸菌:103537      牛奶豆浆:103538       面包蛋糕:103540
        arr2 = str.split(":")
        obj = {"childName":arr2[0],"childId":arr2[1]}
        childList.append(obj)




    return render(request, 'axf/market.html',{'title':'闪送超市','leftSlider':leftSlider,'productList':productList,
                                              'childList':childList, 'categeryid':categeryid, 'cid':cid})


def cart(request):
    return render(request, 'axf/cart.html', {'title':'购物车'})


def mine(request):
    return render(request, 'axf/mine.html', {'title':'我的'})

def login(request):
    if request.method == 'POST':
        f = LoginForm(request.POST)
        if f.is_valid():
            #信息格式没有多大问题，验证账号密码的正确性
            name = f.cleaned_data['username']
            pwd = f.cleaned_data['passwd']
            return redirect('/mine/')
        else:
            return render(request, 'axf/login.html', {'title': '登录', 'form':f, 'error': f.errors})
    else:
        f = LoginForm()
        return render(request, 'axf/login.html', {'title': '登录','form': f})

def register(request):
    return render(request, 'axf/register.html', {'title':'注册'})



















