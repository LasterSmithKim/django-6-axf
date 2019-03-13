$(document).ready(function(){
    var alltypebtn = document.getElementById("all_type")
    var showsortbtn = document.getElementById("all_sort")

    var typediv = document.getElementById("typediv")
    var sortdiv = document.getElementById("sortdiv")


    var csrf = $('input[name="csrfmiddlewaretoken"]').val()


    typediv.style.display = "none"
    sortdiv.style.display = "none"

    alltypebtn.addEventListener("click",function(){
        typediv.style.display = "block"
        sortdiv.style.display = "none"
    },false)

    showsortbtn.addEventListener("click",function(){
        typediv.style.display = "none"
        sortdiv.style.display = "block"
    },false)

    typediv.addEventListener("click",function(){
        typediv.style.display = "none"

    },false)

    sortdiv.addEventListener("click",function(){  typediv.style.display = "none"
        sortdiv.style.display = "none"
    },false)

    //修改购物车
    var addShoppings = document.getElementsByClassName('addShopping')
    var subShoppings = document.getElementsByClassName('subShopping')

    for ( var i = 0 ; i < addShoppings.length ; i++){
        addShopping = addShoppings[i]

        addShopping.addEventListener('click', function(){
            pid = this.getAttribute('g_id') /*getAttribute 获取自定义属性 */
            $.post('/changecart/0/', {'productid': pid,'csrfmiddlewaretoken': csrf}, function(data){
                if (data.status == 'success'){
                    /*添加成功，把中间的span的innerHTML变成当前的数量*/
                    document.getElementById(pid).innerHTML = data.data
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
                }
            })
        })
    }




})


