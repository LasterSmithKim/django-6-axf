$(document).ready(function(){
    //修改购物车
    var addShoppings = document.getElementsByClassName('addShopping')
    var subShoppings = document.getElementsByClassName('subShopping')
    var csrf = $('input[name="csrfmiddlewaretoken"]').val()

    for ( var i = 0 ; i < addShoppings.length ; i++){
        addShopping = addShoppings[i]

        addShopping.addEventListener('click', function(){
            pid = this.getAttribute('g_id') /*getAttribute 获取自定义属性 */
            $.post('/changecart/0/', {'productid': pid,'csrfmiddlewaretoken': csrf}, function(data){
                if (data.status == 'success'){
                    /*添加成功，把中间的span的innerHTML变成当前的数量*/
                    document.getElementById(pid).innerHTML = data.data
                    document.getElementById(pid+"price").innerHTML = data.price
                }else {
                    if (data.data == -1){
                        var href = 'http://' + window.location.host + '/login/'
                        window.location.href = href
                    }
                }
            })
        })
    }

    for ( var i = 0 ; i < subShoppings.length ; i++){
        subShopping = subShoppings[i]

        subShopping.addEventListener('click', function(){
            pid = this.getAttribute('g_id') /*getAttribute 获取自定义属性 */
            $.post('/changecart/1/', {'productid': pid,'csrfmiddlewaretoken': csrf}, function(data){
                if (data.status == 'success'){
                    /*添加成功，把中间的span的innerHTML变成当前的数量*/
                    document.getElementById(pid).innerHTML = data.data
                    document.getElementById(pid+"price").innerHTML = data.price
                     /*数量减到 0 删除li元素*/
                    if(data.data == 0){
                        var li = document.getElementById(pid+'li')
                        li.parentNode.removeChild(li)
                    }
                }
            })
        })
    }


    var ischoses = document.getElementsByClassName("confirm")
    for (var j = 0;j < ischoses.length; j++){
        ischose = ischoses[j]
        ischose.addEventListener("click", function(){
            pid = this.getAttribute('goodsid')
            $.post("/changecart/2/",{'productid': pid,'csrfmiddlewaretoken': csrf}, function(data){
                if (data.status == 'success'){
                    console.log(data.data)
                    var s = document.getElementById(pid+"a")
                    s.innerHTML = data.data
                    console.log(data.data)
                }
            })
        },false)
    }

    var ok = document.getElementById("ok")
    ok.addEventListener("click", function(){
        var f = confirm("确认是否下单？")
        if (f) {
            $.post("/saveoder/", {'csrfmiddlewaretoken': csrf}, function(data){
                if (data.status = 'success'){
                    window.location.href = ('http://' + window.location.host + '/cart/')
                    }
            })
        }
    },false)



})