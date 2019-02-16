$(document).ready(function(){
    setTimeout(function(){
        swiper1()
        swiper2()
    },100)
})

function swiper1() {
    var mySwiper = new Swiper('#topSwiper', {
        direction: 'horizontal',
        loop: true,
        speed:500,
        autoplay:2000,
        // 如果需要分页器
        pagination: '.swiper-pagination',
        control: true
    })
}

function swiper2() {
    var mySwiper2 = new Swiper('#swiperMenu', {
        slidesPerView:3,
        paginationClickable: true,
        spaceBetween:2,
        loop: false,
    })
}
