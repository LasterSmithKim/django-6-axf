$(document).ready(function(){
    var accunt = document.getElementById('accunt')
    var accunterr = document.getElementById('accunterr')
    var checkerr = document.getElementById('checkerr')

    var pass = document.getElementById('pass')
    var passerr = document.getElementById('passerr')
    var passwd = document.getElementById('passwd')
    var passwderr = document.getElementById('passwderr')

    var submiter = document.getElementById('submiter')
    var csrf = $('input[name="csrfmiddlewaretoken"]').val()


/*    #对象聚焦事件*/
    accunt.addEventListener('focus', function(){
        accunterr.style.display = 'none'
        checkerr.style.display = 'none'
    },false)
/*    #离焦事件*/
    accunt.addEventListener('blur', function(){
        instr = this.value
        if (instr.length < 6 || instr.length > 12){
           accunterr.style.display = 'block'
           return
        }
        /*ajax请求，请求地址，发送的数据，回调函数*/
        $.post('/checkuserid/',{'userid':instr,'csrfmiddlewaretoken': csrf},function(data){
            if(data.status == 'error'){
                checkerr.style.display = 'block'
                submiter.disabled = 'disabled'
            }
        })
    },false)

/*    pass 聚焦事件*/
    pass.addEventListener('focus', function(){
        passerr.style.display = 'none'
    },false)
/*    pass 离焦事件*/
    pass.addEventListener('blur', function(){
        instr = this.value
        if (instr.length < 6 || instr.length > 16){
           passerr.style.display = 'block'
           return
        }
    },false)


    /*    passwd 聚焦事件*/
    passwd.addEventListener('focus', function(){
        passwderr.style.display = 'none'
    },false)
/*    passwd 离焦事件*/
    passwd.addEventListener('blur', function(){
        instr = this.value
        if (instr != pass.value){
            passwderr.style.display = 'block'
            return
        }
    },false)

})