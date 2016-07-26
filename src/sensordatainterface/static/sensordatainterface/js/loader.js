/**
 * Created by Juan on 6/28/2016.
 */

requirejs.config({
    paths: {
        'jquery': [
            '//cdnjs.cloudflare.com/ajax/libs/jquery/2.2.4/jquery.min',
            'vendor/jquery/jquery-2.2.4.min'
        ],
        'jquery_template': [
            'vendor/jquery/jquery.loadTemplate-1.5.7.min'
        ],
        'datatables': [
            '//cdn.datatables.net/v/dt/jq-2.2.3/dt-1.10.12/datatables.min.js',
            'vendor/datatables/datatables.min.js'
        ],
        'bootstrap': [
            '//maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min',
            'vendor/bootstrap/bootstrap.min'
        ],
        'bootstrap_datetimepicker': [
            'vendor/bootstrap/bootstrap-datetimepicker'
        ],
        'bootstrap_tooltip': [
            'vendor/bootstrap/bootstrap-tooltip'
        ],
        'bootstrap_confirmation': [
            'vendor/bootstrap/bootstrap-confirmation'
        ],
        'moment': [
            '//cdnjs.cloudflare.com/ajax/libs/moment.js/2.13.0/moment.min',
            'vendor/moment/momentjs'
        ],
        'select2': [
            '//cdnjs.cloudflare.com/ajax/libs/select2/4.0.3/js/select2.min',
            'vendor/jquery/select2.min'
        ]
    },
    shim: {
        bootstrap: { deps: ['jquery'] },
        bootstrap_datetimepicker: { deps: ['jquery', 'bootstrap'] },
        datatables_bootstrap: { deps: ['datatables', 'bootstrap'] }
    }
});
//
// define('generalLibraries', ['jquery', 'jquery_browser', 'underscore', 'bootstrap', 'bootstrap_datepicker']);

// define('d3_global', ['d3'], function(d3Module) {
//     window.d3 = d3Module;
// });

requirejs(['sensors_app'], function(sensors_app) {
    $(document).ready(sensors_app.initialize);
});