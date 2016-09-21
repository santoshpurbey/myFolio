;(function (window, document, $) {
    'use strict';

    var BOUNDLY = window.BOUNDLY || {};
    var $body, $window, $html, $pageHeader, $pageHeader_height, $window_height, $pageWrapper, $sidebarWrapper, $sidebar, $localStorage, $window_width;

    BOUNDLY.variables = function () {
        $window            = $(window);
        $body              = $("body");
        $html              = $("html");
        $pageWrapper       = $("#page-wrapper");
        $sidebarWrapper    = $(".content-wrapper");
        $sidebar           = $(".bndl-sidebar");
        $pageHeader        = $(".page-header");
        $window_height     = $window.height();
        $window_width     = $window.width();
        $pageHeader_height = $pageHeader.outerHeight();
        $localStorage      = typeof(Storage) !== "undefined";
    };

    BOUNDLY.init = function () {

        $(".spinner").fadeOut(300, function () {

            // Show Blog Loop
            BOUNDLY.blogGrid();

            // Init Scroll Bar in hidden sidebar
            $sidebarWrapper.jScrollPane();
        });
    };

    BOUNDLY.subscribeBar = function () {

        var subscribeBar = $(".subscribe-bar"),
            closeIcon    = subscribeBar.find(".ei-close");

        // Check if user close subscribe bar previously
        if ($localStorage) {
            if (localStorage.getItem("subscribeBar") === "hidden") subscribeBar.remove()
        }

        // Close subscribebar after click
        closeIcon.on("click", function () {
            subscribeBar.slideUp(350);

            // Save hidden subscribe bar status to localstorage
            if ($localStorage) {
                localStorage.setItem("subscribeBar", "hidden");
            }
        });
    };

    BOUNDLY.popup = function () {

        var open_button    = $("[data-popup]"),
            textFeld       = $(".user-input"),
            popupContainer = $(".popup-content"),
            close_icon     = $(".destroy-popup");

        open_button.on("click", function (e) {

            e.preventDefault();

            var popup = $(this).data("popup");

            // Open Popup
            $body.addClass("white-filter");
            popupContainer.fadeIn(600);
            $("." + popup).fadeIn(600);

            textFeld.focus();

        });

        // Press esc to close popup
        $body.on("keyup", function (e) {
            if (e.keyCode === 27) close_icon.click();
        });

        // Icon click to close popup
        close_icon.on("click touchstart", function () {
            popupContainer.children().fadeOut(250).end().fadeOut(250);
            $body.removeClass("white-filter");
        });
    };

    BOUNDLY.blogGrid = function () {

        var gridContainer    = $(".blog-loop"),
            posts            = $(".loop"),
            gridItems        = '[class*="masonry-col-"] .post';

        if ( gridContainer.length ) {

            // Lazy Images Init
            var masonry = gridContainer.imagesLoaded(function () {

                // Init Grid layout
                var grid = new Minigrid({
                    container: '.blog-loop',
                    item: gridItems,
                    gutter: 0
                });

                // Fire Grid Layout
                grid.mount();

                // Show blog post after image load
                posts.addClass("bndl-show");
            });
        }
    };

    BOUNDLY.stickyHeader = function () {

        if ($pageHeader.is(".sticky") && $window_width >= 1024) {

            var sticky       = $('.sticky'),
                imageHeader  = $('.image-header'),
                subscribeBar = $('.subscribe-bar'),
                scroll       = $window.scrollTop();

            if ( scroll > $pageHeader_height ) {

                sticky.addClass('fixed');

                if (imageHeader.length) {
                    imageHeader.css("padding-top", $pageHeader_height);

                } else if (subscribeBar.length) {
                    subscribeBar.css("margin-bottom", $pageHeader_height);

                } else {
                    $pageWrapper.css("margin-top", $pageHeader_height);
                }

            } else {
                sticky.removeClass('fixed');
                $pageWrapper.removeAttr("style");
                imageHeader.css("padding-top", 0);
                subscribeBar.removeAttr("style");
            }
        }
    };

    BOUNDLY.toggle = function () {

        $body.on("click", ".bndl-toggle h4", function () {

            var el = $(this);

            // Controlls
            el.parent().parent().parent().find("h4").removeClass("active");
            el.addClass("active");

            // Content container
            el.parent().parent().parent().find(".collapse-content").slideUp(250);
            el.parent().parent().find(".collapse-content").slideDown(250);
        });
    };

    BOUNDLY.tabs = function () {

        $(".bndl-tabs").each(function () {

            var tab = $(this);

            tab.on("click", ".nav-tabs li", function () {

                var el      = $(this),
                    tabItem = tab.find(".tabs-content");

                // Tab panel
                el.parent().find("li").removeClass("active");
                el.addClass("active");

                // Tab Content
                tabItem.find(".tab").removeClass("active");
                tabItem.find(".tab").eq(el.index()).addClass("active");
            });
        });
    };

    BOUNDLY.instagramWidget = function () {

        $(".bndl-widget-carousel").each(function () {

            var carousel = $(this);

            carousel.on("click", ".controller span", function (e) {

                var el = $(this);

                // Controlls
                el.parent().find("span").removeClass();
                el.addClass("active");

                // Image container
                carousel.find("li").hide();
                carousel.find("li").eq(el.index()).fadeIn(350);
            });
        })
    };

    BOUNDLY.countdown = function () {

        var countdown = $(".bndl-countdown");

        countdown.each(function () {

            var el = $(this),
                date          = el.data("date"),
                dateFormat    = el.data("format"),
                countdownType = el.data("type");

            if (countdownType == "until") {
                el.countdown({until: new Date(date), format: dateFormat});

            } else {
                el.countdown({since: new Date(date), format: dateFormat});
            }
        });
    };

    BOUNDLY.progressBar = function () {

        var progressBar = $(".bndl-progress-bar");

        progressBar.each(function () {

            var el         = $(this),
                percentage = el.data("anim-to");

            // Start progressbar after scroll to visible area
            el.waypoint(function () {

                // Progress Line
                el.find(".progress-graph").css("width", percentage + "%");

                // Percentage Counter
                var value = 0,
                    interval = setInterval(function () {

                        ++value;

                        // Clear Interval
                        if (value == percentage) clearInterval(interval);

                        // Animate Percentage
                        el.find(".progress-amount").html(value + "%");
                }, 10);

            }, {
                offset: '100%',
                triggerOnce: false
            });
        });
    };

    BOUNDLY.navigation = function () {

        var menu     = $(".bndl-menu.horizontal"),
            menuIcon = $(".bndl-burger-icon"),
            link     = $(".bndl-menu a");

        if ( $window_width > 960 ) {

            $(".page-header.big .bndl-menu li").hover(function () {
                $(this).children(".sub-menu").stop().fadeIn(200);
                $body.on('scroll touchmove mousewheel', stopScrolling);

            }, function () {
                $(this).children(".sub-menu").stop().fadeOut(100);
                $body.off('scroll touchmove mousewheel', stopScrolling);
            });

        }

        // Change Icon and open menu in Big header type
        $('.page-header.big .bndl-burger').on("click", function (e) {

            menuIcon.toggleClass("active");
            menu.stop().slideToggle(350);
        });

        link.on("click", function (e) {

            var el = $(this);

            // Prevend Default Action
            if (el.attr('href') === '#') e.preventDefault();

            // Rotate Arrow Icon
            if (el.is(".sublink")) el.toggleClass("active");

            // Open & Close Submenu
            el.parent().children(".sub-menu").stop().slideToggle(300, function () {

                // Refresh Scroll Bar Area
                $sidebarWrapper.jScrollPane();
            });
        });


        // Stop Scrolling body when sidebar is open
        function stopScrolling(e) {
            e.preventDefault();
            e.stopPropagation();
            return false;
        }
    };

    BOUNDLY.scrollTop = function () {

        var scroll     = $window.scrollTop(),
            startPoint = $window_height / 2,
            icon       = $(".scroll-top");

        if ( scroll >= startPoint ) {
            icon.fadeIn(300);

        } else {
            icon.fadeOut(300);
        }

        icon.click(function () {
            $("html, body").stop().animate({scrollTop: 0}, 600);
        });
    };

    BOUNDLY.imageHeader = function () {

        var imageHeader = $(".image-header");

        if (imageHeader.length  && imageHeader.is(".full-height") ) {
            imageHeader.height($window_height);
        }
    };

    BOUNDLY.aboutAuthorWidget = function () {

        var authorWidget = $(".about-author");

        if (authorWidget.length && $window_width <= 1024) {

            authorWidget.removeClass("sticky");
        }
    };

    BOUNDLY.sidebar = function () {

        // Open Icons
        var bndl_burger = $(".bndl-burger"),
            bndl_widget = $(".bndl-widget-icon"),
            sidebar     = $(".bndl-sidebar");

        // Open Left sidebar
        bndl_burger.on("mouseenter touchstart", function () {

            if (!$pageHeader.is('.big')) openSidebar("left")
        });

        // Open Right Sidebar
        bndl_widget.on("mouseenter", function () {

            openSidebar("right");
        });

        // Close Sidebar
        $body.on("mouseenter touchstart click", ".toucharea, .close-sidebar-mobile", function () {
            closeSidebar();
        });

        // Stop Scrolling body when sidebar is open
        function stopScrolling(e) {
            e.preventDefault();
            e.stopPropagation();
            return false;
        }

        // Open sidebar after icon hover
        function openSidebar(side) {
            $("<div>").addClass("toucharea " + side).prependTo("body");
            $(".bndl-sidebar." + side).css(side, 0);
            $body.addClass("white-filter");

            // Close Button
            if( $window_width < 1024 ) $(".close-sidebar-mobile").fadeIn(300);

            // Stop Scrolling
            $body.on('scroll touchmove mousewheel', stopScrolling);
        }

        // Close sidebar after mouse leave sidebar
        function closeSidebar() {
            sidebar.removeAttr("style");
            $body.removeClass("white-filter");
            $(".toucharea").remove();


            // Close Button
            if( $window_width < 1024 ) $(".close-sidebar-mobile").fadeOut(150);

            // Stop Scrolling
            $body.off('scroll touchmove mousewheel', stopScrolling);
        }
    };

    $(document).ready(function () {
        BOUNDLY.variables();
        BOUNDLY.imageHeader();
        BOUNDLY.sidebar();
        BOUNDLY.popup();
        BOUNDLY.instagramWidget();
        BOUNDLY.countdown();
        BOUNDLY.tabs();
        BOUNDLY.toggle();
        BOUNDLY.progressBar();
        BOUNDLY.subscribeBar();
        BOUNDLY.navigation();
        BOUNDLY.aboutAuthorWidget();
        BOUNDLY.init();
    });

    $(window).load(function () {
    });

    $(document).scroll(function () {
        BOUNDLY.stickyHeader();
        BOUNDLY.scrollTop();
    });

    $(window).resize(function () {
        BOUNDLY.aboutAuthorWidget();
        BOUNDLY.blogGrid();
    });
})(window, document, jQuery);
