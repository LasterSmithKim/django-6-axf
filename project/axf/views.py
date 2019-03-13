from django.shortcuts import render
from .models import Wheel, Nav, Mustbuy,Shop,MainShow,FoodTypes,Goods,User,Cart
from .forms.login import LoginForm
from django.http import HttpResponse,JsonResponse
from django.shortcuts import redirect
import os
import time
import random
from django.conf import settings
from django.contrib.auth import logout

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

    token = request.session.get("token")
    if token:
        user = User.objects.get(userToken = token)
        cartlist = Cart.objects.filter(userAccount = user.userAccount)

        for p in productList:
            for c in cartlist:
                if c.productid == p.productid:
                    p.num = c.productnum
                    continue

    return render(request, 'axf/market.html',{'title':'闪送超市','leftSlider':leftSlider,'productList':productList,
                                              'childList':childList, 'categeryid':categeryid, 'cid':cid,
                                             })


def cart(request):
    cartlist = []
    token = request.session.get("token")
    if token:
        user = User.objects.get(userToken=token)
        cartlist = Cart.objects.filter(userAccount=user.userAccount)


    return render(request, 'axf/cart.html', {'title':'购物车', 'cartlist':cartlist})


def mine(request):
    username = request.session.get('username','未登录')
    return render(request, 'axf/mine.html', {'title':'我的','username':username})


#修改购物车
def changecart(request,flag):
    # 判断用户是否登录？
    token = request.session.get('token')
    if token == None:
        #没有登录，ajax请求过来 无法重定向；可以返回json数据 让js接收json数据 进行DOM元素操作 返回-1 表示未登录
        return JsonResponse({'data':'-1', 'status':'error'})

    productid = request.POST.get('productid')
    product = Goods.objects.get(productid = productid)#获取数据库中商品的所有信息
    user = User.objects.get(userToken = token)

    if flag == '0':
        if product.storenums == 0:
            return JsonResponse({"data": -2, "status": "error"})  # -2 库存没有了

        carts = Cart.objects.filter(userAccount =user.userAccount)#取出某个人的所有商品
        c = None
        if carts.count() == 0:
            #一条订单都没有，就直接增加一条订单
            c = Cart.createcart(user.userAccount, productid, 1, product.price, True,
                                product.productimg, product.productlongname, False,)
            c.save()
        else:
            try:
                c = carts.get(productid = productid)#取出某人的某一条商品
                #修改数量和价格
                c.productnum += 1
                c.productprice = "%.2f"%(float(product.price) * c.productnum)
                c.save()
            except Cart.DoesNotExist as e:
                #某人有订单，但是没有该商品的订单，就直接增加一条订单
                c = Cart.createcart(user.userAccount, productid, 1, product.price, True,
                                    product.productimg, product.productlongname, False, )
                c.save()
        #库存减去1
        product.storenums -= 1
        product.save()
        return JsonResponse({'data':c.productnum, 'price':c.productprice, 'status':'success'})


    elif flag == '1':
        carts = Cart.objects.filter(userAccount =user.userAccount)#取出某个人的所有商品
        c = None
        if carts.count() == 0:
            return JsonResponse({"data":-2, "status":"error"})
        else:
            try:
                c = carts.get(productid = productid)#取出某人的某一条商品
                #修改数量和价格
                c.productnum -= 1
                c.productprice = "%.2f"%(float(product.price) * c.productnum)
                if c.productnum == 0:
                    c.delete()
                else:
                    c.save()

            except Cart.DoesNotExist as e:
                return JsonResponse({"data": -2, "status": "error"})
        #库存加上1
        product.storenums += 1
        product.save()
        return JsonResponse({'data': c.productnum, 'price':c.productprice, 'status':'success'})

    elif flag == '2':
        carts = Cart.objects.filter(userAccount=user.userAccount)
        c = carts.get(productid=productid)
        c.isChose = not c.isChose
        c.save()
        str = ''
        if c.isChose:
            str = '√'
        return JsonResponse({'data':str, 'status':'success'})
'''
    elif flag == 3:
        pass
'''










def login(request):
    if request.method == 'POST':
        f = LoginForm(request.POST)
        if f.is_valid():
            #信息格式没有多大问题，验证账号密码的正确性
            nameid = f.cleaned_data['username']
            pwd = f.cleaned_data['passwd']
            try:
                user = User.objects.get(userAccount = nameid)
                if user.userPasswd != pwd :
                    #登录失败
                    f = LoginForm()
                    return render(request, 'axf/login.html', {'title': '登录', 'form': f, 'error': '密码输入错误！'})
            except User.DoesNotExist as e:
                #登录失败
                f = LoginForm()
                return render(request, 'axf/login.html', {'title': '登录', 'form': f, 'error': '用户名不存在！'})
            #登录成功
            userToken = str(time.time() + random.randrange(1, 100000))
            user.userToken = userToken
            user.save()
            request.session['username'] = user.userName
            request.session['token'] = user.userToken

            return redirect('/mine/')
        else:
            f = LoginForm()
            return render(request, 'axf/login.html', {'title': '登录', 'form':f, 'error': '信息格式验证错误！'})
    else:
        f = LoginForm()
        return render(request, 'axf/login.html', {'title': '登录','form': f})



def register(request):
    if request.method == 'POST':
        userAccount = request.POST.get('userAccount')
        userPasswd = request.POST.get('userPasswd')
        userName = request.POST.get('userName')
        userPhone = request.POST.get('userPhone')
        userAdderss = request.POST.get('userAdd')
        userRank = 0
        userToken = str(time.time() + random.randrange(1,100000))
        #头像图片上传
        f = request.FILES['userImg']
        userImg = os.path.join(settings.MEDIA_ROOT, userAccount + '.png')
        with open(userImg,'wb') as fp:
            for data in f.chunks():
                fp.write(data)
        #创建用户到数据库
        user = User.createuser(userAccount, userPasswd, userName, userPhone, userAdderss, userImg, userRank, userToken)
        user.save()
        #sessions数据保持
        request.session['username'] = userName
        request.session['token'] = userToken

        return redirect('/mine/')

    else:
        return render(request, 'axf/register.html', {'title':'注册'})

#退出登录
def quit(request):
    logout(request)
    return redirect('/mine/')

#验证账号是否被注册
def checkuserid(request):
    userid = request.POST.get('userid')

    try:
        user = User.objects.get(userAccount = userid)
        return JsonResponse({'data':'该用户已经被注册','status':'error'})
    except User.DoesNotExist as e:
        return JsonResponse({'data':'可以注册','status':'success'})


















