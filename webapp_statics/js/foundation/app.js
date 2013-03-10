;(function ($, window, undefined) {
    'use strict';

    var $doc = $(document),
        Modernizr = window.Modernizr;

    function column_equalizer(){
        $('.equal-columns').equalize({equalize: 'outerHeight', children: '.equal-item', reset: true, breakpoint: 767});
        return;
    }

    $(document).ready(function() {
        $.fn.foundationAlerts           ? $doc.foundationAlerts() : null;
        $.fn.foundationButtons          ? $doc.foundationButtons() : null;
        $.fn.foundationAccordion        ? $doc.foundationAccordion() : null;
        $.fn.foundationNavigation       ? $doc.foundationNavigation() : null;
        $.fn.foundationTopBar           ? $doc.foundationTopBar() : null;
        $.fn.foundationMediaQueryViewer ? $doc.foundationMediaQueryViewer() : null;
        $.fn.foundationTooltips         ? $doc.foundationTooltips() : null;
        
    });

    $(window).load(function () {
        // Equalize some columns after full page loading
        // NOTE: Needed to be in the $.load(), because webkit raise ready() even if it have 
        //       not download all ressources, this cause false dimensions because all images 
        //       have not yet be downloaded, so they doesn't set true dimensions on their 
        //       parent and etc..
        column_equalizer();
    });
    
    // Bind equalizer action on window resize
    $(window).resize(function() {
        column_equalizer();
    });

    // Hide address bar on mobile devices (except if #hash present, so we don't mess up deep linking).
    if (Modernizr.touch && !window.location.hash) {
        $(window).load(function () {
            setTimeout(function () {
                // At load, if user hasn't scrolled more than 20px or so...
                if( $(window).scrollTop() < 20 ) window.scrollTo(0, 1);
            }, 0);
        });
    }

})(jQuery, this);
