(function($) {
  "use strict";

//------------------------------------- Waiting for the entire site to load ------------------------------------------------//

jQuery(window).load(function() {
		jQuery("#loaderInner").fadeOut();
		jQuery("#loader").delay(200).fadeOut("slow");
});

$(document).ready(function(){
//------------------------------------- Portfolio setup------------------------------------------------//

$('.box').magnificPopup({
					  type: 'image',
					fixedContentPos: false,
					fixedBgPos: false,
					mainClass: 'mfp-no-margins mfp-with-zoom',
					image: {
						verticalFit: true
					},
					zoom: {
						enabled: true,
						duration: 300
					}
				});


$('.popup-youtube, .popup-vimeo').magnificPopup({
	disableOn: 700,
	type: 'iframe',
	mainClass: 'mfp-fade',
	removalDelay: 160,
	preloader: false,

	fixedContentPos: false
});

/*Filtred portfolio*/
$('.filter a').on("click", function(e){

		e.preventDefault();
		$(this).addClass('active');
		$(this).parent().siblings().find('a').removeClass('active');



        var filters = $(this).attr('data-filter');
        $(this).closest('.works').find('.item').removeClass('disable');

        if (filters !== 'all') {




        var selected =  $(this).closest('.works').find('.item');

        for(var i = 0; i < selected.length; i++){

        if (!selected.eq(i).hasClass(filters)) {
                    selected.eq(i).addClass('disable');
				}

        }

   }


});



//------------------------------------- End portfolio setup------------------------------------------------//

});


})(jQuery);
