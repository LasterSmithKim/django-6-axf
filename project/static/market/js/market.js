$(document).ready(function(){
    var alltypebtn = document.getElementById("all_type")
    var showsortbtn = document.getElementById("all_sort")

    var typediv = document.getElementById("typediv")
    var sortdiv = document.getElementById("sortdiv")

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




})


