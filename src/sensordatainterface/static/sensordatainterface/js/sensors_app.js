/**
 * Created by Juan on 6/28/2016.
 */

define(['forms', 'jquery', 'bootstrap'], function(forms) {
    var self = {};
    self.mainForm = '';

    self.initialize = function() {
        var formElement = $('form [data-main-form]');
        self.mainForm = forms.createForm(formElement);
    };

    return self;
});