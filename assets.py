from django_assets import Bundle, register

AVALAIBLE_BUNDLES = {
    'main_css': Bundle(
        'css/main.css',
        filters='yui_css',
        output='css/main.min.css'
    ),
    'modernizr_js': Bundle(
        "js/foundation/modernizr.foundation.src.js",
        filters='yui_js',
        output='js/modernizr.min.js'
    ),
    'main_js': Bundle(
        "js/foundation/jquery.js",
        "js/jquery/equalize.js",
         "js/foundation/jquery.foundation.forms.js",
        #"js/foundation/jquery.foundation.magellan.js",
        "js/foundation/jquery.foundation.navigation.js",
        "js/foundation/jquery.foundation.accordion.js",
        "js/foundation/jquery.foundation.topbar.js",
        "js/foundation/jquery.cookie.js",
        "js/foundation/jquery.foundation.tabs.js",
        "js/foundation/jquery.foundation.buttons.js",
        "js/foundation/jquery.event.swipe.js",
        "js/foundation/jquery.foundation.alerts.js",
        "js/foundation/jquery.placeholder.js",
        "js/foundation/jquery.foundation.tooltips.js",
        "js/foundation/jquery.event.move.js",
        "js/foundation/app.js",
        filters='yui_js',
        output='js/main.min.js'
    ),
}

ENABLED_BUNDLES = [
    'modernizr_js',
    'main_css',
    'main_js',
]

for item in ENABLED_BUNDLES:
    register(item, AVALAIBLE_BUNDLES[item])
