$(document).ready(function(){
    /* ---Navbar--- */
    $(window).on("scroll", function(){
        if($(this).scrollTop() > 90){
            $(".navbar").addClass("navbar-shrink");
        }
        else{
            $(".navbar").removeClass("navbar-shrink")
        }
    });

    /* ---owl carousel Cliente--- */
    $('.clientes-carousel').owlCarousel({
        loop:true,
        margin:0,
        autoplay:true,
        responsiveClass:true,
        responsive:{
            0:{
                items:2,
            },
            600:{
                items:2,
            },
            1000:{
                items:4,
            }
        }
    });
    /* ---owl carousel depoiments--- */
    $('.depoiments-carousel').owlCarousel({
        loop:true,
        margin:0,
        // autoplay:true,
        responsiveClass:true,
        responsive:{
            0:{
                items:1,
            },
            600:{
                items:2,
            },
            1000:{
                items:3,
            }
        }
    });
    /* ---scrolling - scrollit --- */
    $(function(){
        $.scrollIt({
            topOffset: 0
        });
    });
    /* --- navbar - collapse --- */
    $(".nav-link").on("click", function(){
        $(".navbar-collapse").collapse("hide");
    });
    /* --- Cookies --- */
    const cookieContainer = document.querySelector(".cookie-container")
    const cookieButton = document.querySelector(".cookie-btn")  

    cookieButton.addEventListener("click", () =>{
        cookieContainer.classList.remove("active");
        localStorage.setItem("cookieBannerDisplayed", "true")
    });
    setTimeout(() => {
        if(!localStorage.getItem("cookieBannerDisplayed")){
            cookieContainer.classList.add("active");
        }
    }, 2000);

});
