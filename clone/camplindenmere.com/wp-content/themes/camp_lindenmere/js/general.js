var $ = jQuery.noConflict();
var headerOuterHeight_;

$(document).ready(function () {
    setTimeout(function () {
        $(".inner-loader").fadeOut();
    }, 2000);
    if ($('.gallery-slider').length) {
        var slideCount = $('.slideCount');
        var slickSlide = $('.gallery-slider');

        slickSlide.on('init reInit afterChange', function (event, slick, currentSlide, nextSlide) {
            //currentSlide is undefined on init -- set it to 0 in this case (currentSlide is 0 based)
            var i = (currentSlide ? currentSlide : 0) + 1;
            if (i < 10) {
                $(this).find('.slideCount').html('<span class="slideCountItem">0' + i + '</span> ' + '/' + ' <span class="slideCountAll">0' + slick.slideCount + '</span>');
            } else {
                $(this).find('.slideCount').html('<span class="slideCountItem">' + i + '</span> ' + '/' + ' <span class="slideCountAll">' + slick.slideCount + '</span>');
            }
        });

        slickSlide.slick({
            slide: '.bc-gallery__single-slide',
            slideToShow: 1,
            centerMode: true,
            centerPadding: '325px',
            arrows: true,
            prevArrow: '<button type="button" class="slide-btn slick-prev"><svg width="32px" height="12px" viewBox="0 0 32 12" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><g id="Interactions-&amp;-Icons" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><g id="Icons" transform="translate(-257.000000, -291.000000)" stroke="#00AFD7" stroke-width="3"><g id="Component/Element/Icon/Long-Arrow/Left" transform="translate(261.000000, 293.000000)"><polyline id="Path-2-Copy" transform="translate(13.731709, 4.434876) scale(-1, -1) translate(-13.731709, -4.434876) " points="3.55271368e-15 8.86975167 27.4634178 8.86975167 18.5936661 -1.77635684e-15"></polyline></g></g></g></svg></button>',
            nextArrow: '<button type="button" class="slide-btn slick-next"><svg width="31px" height="12px" viewBox="0 0 31 12" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><g id="Interactions-&amp;-Icons" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><g id="Icons" transform="translate(-330.000000, -292.000000)" stroke="#00AFD7" stroke-width="3"><g id="Component/Element/Icon/Long-Arrow/Right" transform="translate(330.000000, 293.000000)"><polyline id="Path-2" points="3.55271368e-15 8.86975167 27.4634178 8.86975167 18.5936661 -1.77635684e-15"></polyline></g></g></g></svg></button>',
            responsive: [
                {
                    breakpoint: 767,
                    settings: {
                        centerMode: false,
                        centerPadding: '0',
                    }
                },
                {
                    breakpoint: 991,
                    settings: {
                        centerPadding: '100px',
                    }
                },
                {
                    breakpoint: 1200,
                    settings: {
                        centerPadding: '200px',
                    }
                },
                {
                    breakpoint: 1250,
                    settings: {
                        centerPadding: '225px',
                    }
                },
            ]
        });

    }




    $('.mobile_slider').slick({
        autoplay: false,
        loop: false,
        infinite: false,
        slidesToScroll: 1,
        slidesToShow: 1,
        nav: false,
        arrows: false,
        dots: true,
        adaptiveHeight: true
    });




    if ($('.story-slider').length) {
        var slideCount = $('.slideCount');
        var slickSlide = $('.story-slider');

        slickSlide.on('init reInit afterChange', function (event, slick, currentSlide, nextSlide) {
            var j = (currentSlide ? currentSlide : 0) + 1;

            if (j < 10) {
                var k = '0' + j;

            } else {
                var k = j;
            }

            if (slick.slideCount < 10) {
                var kt = '0' + slick.slideCount;
            } else {
                var kt = slick.slideCount;
            }
            $(this).find('.slideCount').html('<span class="slideCountItem">' + k + '</span> ' + '/' + ' <span class="slideCountAll">' + kt + '</span>');
        });

        slickSlide.slick({
            slide: '.slide-story',
            slidesToScroll: 1,
            slidesToShow: 1,
            prevArrow: '<button type="button" class="slide-btn slick-prev"><svg width="32px" height="12px" viewBox="0 0 32 12" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><g id="Interactions-&amp;-Icons" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><g id="Icons" transform="translate(-257.000000, -291.000000)" stroke="#00AFD7" stroke-width="3"><g id="Component/Element/Icon/Long-Arrow/Left" transform="translate(261.000000, 293.000000)"><polyline id="Path-2-Copy" transform="translate(13.731709, 4.434876) scale(-1, -1) translate(-13.731709, -4.434876) " points="3.55271368e-15 8.86975167 27.4634178 8.86975167 18.5936661 -1.77635684e-15"></polyline></g></g></g></svg></button>',
            nextArrow: '<button type="button" class="slide-btn slick-next"><svg width="31px" height="12px" viewBox="0 0 31 12" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><g id="Interactions-&amp;-Icons" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><g id="Icons" transform="translate(-330.000000, -292.000000)" stroke="#00AFD7" stroke-width="3"><g id="Component/Element/Icon/Long-Arrow/Right" transform="translate(330.000000, 293.000000)"><polyline id="Path-2" points="3.55271368e-15 8.86975167 27.4634178 8.86975167 18.5936661 -1.77635684e-15"></polyline></g></g></g></svg></button>',
        });

    }

    $(document).on('click', '.prevSlide', function () {
        $('.slider-bottom1, .slider-top1').slick('slickPrev');
    });
    $(document).on('click', '.nextSlide', function () {
        $('.slider-bottom1, .slider-top1').slick('slickNext');
    });

    $(".slider-top1").slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        asNavFor: '.slider-bottom1'
    });
    $(".slider-bottom1").slick({
        slidesToShow: 6,
        slidesToScroll: 1,
        arrows: false,
        asNavFor: '.slider-top1',
        dots: false,
        centerMode: false,
        focusOnSelect: true,
        responsive: [
            {
                breakpoint: 1200,
                settings: {
                    slidesToShow: 4,
                    slidesToScroll: 1,
                    arrows: false,
                }
            },
            {
                breakpoint: 767,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1,
                    arrows: false,
                    centerMode: true,
                    centerPadding: '75px'
                }
            },
            {
                breakpoint: 640,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1,
                    arrows: false,
                    centerMode: true,
                    centerPadding: '75px'

                }
            }

        ]
    });
    // setTimeout(function(){
    $("h4.txt-rotate").typed({
        strings: ["THE CHOICE IS YOURS"],
        typeSpeed: 100,
        startDelay: 10,
        backSpeed: 10,
        backDelay: 8500,
        loop: true,
        cursorChar: "|",
        contentType: 'html'

    });

    $('.first-popup-link').magnificPopup({
        closeBtnInside: true
    });
    $('.video-popup-link').magnificPopup({
        closeBtnInside: true
    });
    $(document).on("click", ".play-btn", function (i) {
        i.preventDefault();
        var e, t, s, o = $(this).closest(".videoCov");
        t = (e = o).find("#video"),
            s = t.data("src"),
            e.addClass("videopart--active"),
            t.attr("src", s);
        $(".play-btn").fadeOut();
    });

    $('img.svg').each(function () {
        var $img = jQuery(this);
        var imgID = $img.attr('id');
        var imgClass = $img.attr('class');
        var imgURL = $img.attr('src');
        jQuery.get(imgURL, function (data) {
            var $svg = jQuery(data).find('svg');
            if (typeof imgID !== 'undefined') {
                $svg = $svg.attr('id', imgID);
            }
            if (typeof imgClass !== 'undefined') {
                $svg = $svg.attr('class', imgClass + ' replaced-svg');
            }
            $svg = $svg.removeAttr('xmlns:a');
            $img.replaceWith($svg);
        }, 'xml');
    });

    $(".catlist").selectbox();
    $(".department_select").selectbox();



    $(".blue-menu.menu-item-has-children a").on("click", function () {
        $(this).next(".sub-menu").slideToggle();
        $(this).toggleClass("open-sub");
    });

    // svg
    $(function () {
        jQuery('img.svg').each(function () {
            var $img = jQuery(this);
            var imgID = $img.attr('id');
            var imgClass = $img.attr('class');
            var imgURL = $img.attr('src');
            jQuery.get(imgURL, function (data) {
                var $svg = jQuery(data).find('svg');
                if (typeof imgID !== 'undefined') {
                    $svg = $svg.attr('id', imgID);
                }
                if (typeof imgClass !== 'undefined') {
                    $svg = $svg.attr('class', imgClass + ' replaced-svg');
                }
                $svg = $svg.removeAttr('xmlns:a');
                $img.replaceWith($svg);
            }, 'xml');
        });
    });

    //    menu start


    var menu_cont = $(".cover-icon").html();
    $(".cover-icon").on("click", function () {
        $("body").toggleClass("open-main-menu");
        $(this).next().toggleClass("open-menu-main");
        $(this).toggleClass("menu-close");
        if ($(this).hasClass("menu-close")) {
            $(this).html("close<img src='/wp-content/themes/camp_lindenmere/images/close.svg' width='30' height='30' alt='Close'>");
        } else {
            $(this).html(menu_cont);
        }

    })
    var $default_a = $(".cover-main-menu .current_page_parent a");
    if ($default_a.length) {
        $(".menu-wrap .sub-menu").addClass('active');
    }
    var bg_img = $default_a.find(".menu-image-wrapper").html();
    $(".cover-sub-menu-default-overlay").html(bg_img);
    setTimeout(function () {
        $(".cover-sub-menu-default-overlay img").addClass('opacity-10 z-3').removeClass('opacity-0 z-1');
    }, 10);

    $(".menu-item-has-children.current-menu-ancestor").addClass("active");
    $(".menu-item-has-children.current-menu-ancestor > a").addClass("open");

    var subMenu = $(".cover-main-menu .menu-item-has-children.current-menu-ancestor .sub-menu");
    var totalHeight = 0;
    $(subMenu).find('li:even').each(function () {
        totalHeight += $(this).outerHeight(true);
    });
    subMenu.css("max-height", totalHeight + "px");

    $(".cover-main-menu .menu-item-has-children > a").on("click", function () {
        console.log($(this).attr("class"));
        var thisParent = $(this).parent("li.menu-item-has-children");
        if (thisParent.hasClass('open-su')) {
            $(this).removeClass("active open");
            thisParent.removeClass("open-su");
            $(".menu-wrap .sub-menu").css("max-height", "0");
            return;
        }
        $(".menu-wrap .sub-menu").css("max-height", '0');
        $(".menu-item-has-children > a").removeClass('active open');
        $(this).addClass('active open');
        var subMenu = $(this).next(".sub-menu");
        var totalHeight = 0;
        $(subMenu).find('li:even').each(function () {
            totalHeight += $(this).outerHeight(true);
        });
        subMenu.css("max-height", totalHeight + "px");

        $(".menu-item-has-children").removeClass("open-su current-page-parent current-menu-parent current-menu-item");
        thisParent.addClass("open-su");

        var bg_img = $(this).find(".menu-image-wrapper").html();
        $(".cover-sub-menu-default-overlay").append(bg_img);
        setTimeout(function () {
            $(".cover-sub-menu-default-overlay img:not(:last)").addClass('z-1').removeClass('z-3 z-2');
            $(".cover-sub-menu-default-overlay img:last").prev().addClass('z-2').removeClass('z-3');
            $(".cover-sub-menu-default-overlay img:last").addClass('opacity-10 z-3').removeClass('opacity-0 z-1');
        }, 10);
        setTimeout(function () {
            $(".cover-sub-menu-default-overlay img:not(:last)").remove();
        }, 1000);
    });

    $(".cover-main-menu .menu-item-has-children").on("mouseenter", function () {
        $(".menu-wrap .sub-menu").addClass('active');
        var thisAnchor = $(this).find("> a");
        if (thisAnchor.hasClass('active')) {
            return;
        }
        $(".menu-item-has-children > a").removeClass('active');
        thisAnchor.addClass("active");

        var bg_img = thisAnchor.find(".menu-image-wrapper").html();
        $(".cover-sub-menu-overlay").append(bg_img);
        setTimeout(function () {
            $(".cover-sub-menu-overlay img:not(:last)").addClass('z-1').removeClass('z-3 z-2');
            $(".cover-sub-menu-overlay img:last").prev().addClass('z-2').removeClass('z-3');
            $(".cover-sub-menu-overlay img:last").addClass('opacity-10 z-3').removeClass('opacity-0 z-1');
        }, 10);
        setTimeout(function () {
            $(".cover-sub-menu-overlay img:not(.z-3):not(.z-2)").remove();
        }, 1000);
    });



    $(".cover-icon").on("click", function () {
        if (window.innerWidth < 1200) {
            $(".btn-hamburger").trigger("click");
        }
    });

    //    menu end


    headerOuterHeight_ = $(".main-header").outerHeight();
    var Obj_ = $("<div>", {
        class: "blankDiv"
    }).height(headerOuterHeight_).hide().insertAfter($(".wrap-header"));
    stickyHeader();
    $(".main-header__nav-mobile--wrapper").append("<div class='close-btn'><img src='/wp-content/themes/camp_lindenmere/images/close.svg' width='40' height='40' alt='Close' /></div>")
    $(".close-btn").on("click", function () {
        $(".main-header__nav-mobile--wrapper").removeClass("active");
        $("body").removeClass("overlayed");
        if ($(".cover-icon").hasClass("menu-close")) {
            $(".cover-icon").trigger("click")
        }
    });
    setTimeout(function () {
        fadeInout = {
            init: function () {
                v = $(".loading-txt > li").css('visibility', 'hidden'),
                    cur = 0,
                    rem = 0;
                for (var j, x, i = v.length; i; j = parseInt(Math.random() * i), x = v[--i], v[i] = v[j], v[j] = x);
                return this;
            },
            fades: function () {
                this.fadein();
            },
            fadein: function () {
                v.eq(cur++).css('visibility', 'visible').hide().fadeIn();
                if (cur != v.length) setTimeout(fadeInout.fadein, 500);
                else setTimeout(fadeInout.fadeout, 500);
            },
            fadeout: function () {
                v.eq(rem++).css('visibility', 'none').fadeOut().show();
                if (rem != v.length) setTimeout(fadeInout.fadeout, 500);
                setTimeout(function () {
                    if ($(".loading-txt > li:visible").length == 0) {
                        $(".wrap-loader").fadeOut();
                    }
                }, 4998)
            }
        }
        fadeInout.init().fades();
    }, 3500);
    var tl = new TimelineMax({
        repeat: -1,
        repeatDelay: .01,
        yoyo: true
    })
    tl.staggerTo(".loader-text span", .5, {
        color: "rgb(0, 162, 199)",
        scale: 1.05
    }, 0.2);
    $(".play-btn-video").on("click", function () {
        $(".play-btn").trigger("click")
    })
    if ($('.page-content > *:last-child').css('background-image') == 'none') {
        if (window.innerWidth < 992) {
            $('.page-content > *:last-child').css("margin-bottom", "30px");
        } else {
            $('.page-content > *:last-child').css("margin-bottom", "60px");
        }
    }
})
$(window).resize(function () {
    headerOuterHeight_ = $(".main-header").outerHeight();
    $(".blankDiv").height(headerOuterHeight_);
    stickyHeader();
    if ($('.page-content > *:last-child').css('background-image') == 'none') {
        if (window.innerWidth < 1200) {
            $('.page-content > *:last-child').css("margin-bottom", "30px");
        } else {
            $('.page-content > *:last-child').css("margin-bottom", "60px");
        }
    }
});
$(window).scroll(function () {
    stickyHeader();
});
function stickyHeader() {
    if ($(window).scrollTop() > 0) {
        $("body").addClass("stickyHeader");
        $(".blankDiv").show();
    } else {
        $("body").removeClass("stickyHeader");
        $(".blankDiv").hide();
    }
}
$(window).on('load', function () {
    $('.banner-sec').slick({
        //autoplay: true,
        autoplaySpeed: 5000,
        loop: true,
        infinite: true,
        slidesToScroll: 1,
        slidesToShow: 1,
        fade: true,
        nav: false,
        arrows: false,
        dots: false,
    });





    var TxtRotate = function (el, toRotate, period) {
        this.toRotate = toRotate;
        this.el = el;
        this.loopNum = 0;
        this.period = parseInt(period, 10) || 2000;
        this.txt = '';
        this.tick();
        this.isDeleting = false;
    };

    TxtRotate.prototype.tick = function () {
        var i = this.loopNum % this.toRotate.length;
        var fullTxt = this.toRotate[i];

        if (this.isDeleting) {
            this.txt = fullTxt.substring(0, this.txt.length - 1);
        } else {
            this.txt = fullTxt.substring(0, this.txt.length + 1);
        }

        this.el.innerHTML = '<span class="wrap">' + this.txt + '</span>';

        var that = this;
        var delta = 300 - Math.random() * 100;

        if (this.isDeleting) { delta /= 2; }


        if (!this.isDeleting && this.txt === fullTxt) {
            delta = this.period;
            //this.isDeleting = true;
            setTimeout(function () {
                $('.banner-sec').slick('slickNext');
            }, 2000);
            return;
        } else if (this.isDeleting && this.txt === '') {
            //this.isDeleting = false;
            this.loopNum++;
            delta = 500;
        }

        setTimeout(function () {
            that.tick();
        }, delta);
    };


    // INJECT CSS
    var css = document.createElement("style");
    css.type = "text/css";
    css.innerHTML = ".banner-sec .txt-rotate > .wrap { border-right: 2px solid transparent; }";
    document.body.appendChild(css);


    initiate_txt_rotate($('.banner-sec'));

    $('.banner-sec').on('afterChange', function (event, slick, currentSlide, nextSlide) {
        $(this).find('.txt-rotate .wrap').remove();
        $(this).find('.txt-rotate').addClass('opacity-0');
        initiate_txt_rotate(this);
    });

    function initiate_txt_rotate(parent_slider) {
        var elements = $(parent_slider).find('.slick-active .txt-rotate');
        elements.removeClass('opacity-0');

        var toRotate = elements.attr('data-rotate');
        var period = elements.attr('data-period');
        if (toRotate) {
            new TxtRotate(elements[0], JSON.parse(toRotate), period);
        }
    }


    if ($('.insta_slider').hasClass('lf')) {

        $('.insta_slider #sbi_images').slick({
            slidesToShow: 3,
            slidesToScroll: 1,
            arrows: false,
            dots: false,
            centerMode: false,
            infinite: false,
            responsive: [
                {
                    breakpoint: 1200,
                    settings: {
                        slidesToShow: 2,
                    }
                },
                {
                    breakpoint: 767,
                    settings: {
                        slidesToShow: 1,
                    }
                },
                {
                    breakpoint: 640,
                    settings: {
                        slidesToShow: 1,

                    }
                }

            ]
        }).on('setPosition', function (event, slick) {
            slick.$slides.css('height', slick.$slides.width() + 'px');
        });

    } else {


        $('.insta_slider').slick({
            slidesToShow: 3,
            slidesToScroll: 1,
            arrows: false,
            dots: true,
            centerMode: false,
            infinite: false,
            responsive: [
                {
                    breakpoint: 1200,
                    settings: {
                        slidesToShow: 2,
                    }
                },
                {
                    breakpoint: 767,
                    settings: {
                        slidesToShow: 1,
                    }
                },
                {
                    breakpoint: 640,
                    settings: {
                        slidesToShow: 1,

                    }
                }

            ]
        }).on('setPosition', function (event, slick) {
            slick.$slides.css('height', slick.$slides.width() + 'px');
        });
    }

    $('.ginput_container_text, .ginput_container_textarea, .ginput_container_number, .ginput_container_email,.ginput_container_website, .ginput_complex').each(function () {
        $(this).parent().addClass('floating-label');
    });
});

window.onscroll = () => {scrollNavbar()}; 
scrollNavbar = () => {
    const navBar = document.getElementById("navBar"); 

    if(document.documentElement.scrollTop > 100) {
        navBar.classList.add("nav-white-bg")
    } else {
        navBar.classList.remove('nav-white-bg')
    }
}