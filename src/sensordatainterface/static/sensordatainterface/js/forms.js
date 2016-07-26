/**
 * Created by Juan on 6/28/2016.
 */


define(['jquery', 'bootstrap_datetimepicker', 'select2'], function() {
    'use strict';
    
    var self = {};

    var form = {
        formType: '',
        formElement: {},
        csrfmiddlewaretoken: '',
        initialize: function initialize(formElement) {
            this.formElement = formElement;
            this.formType = this.formElement.data('form-type');
            this.csrfmiddlewaretoken = $('form [name="csrfmiddlewaretoken"]').val();

            this.setFormClasses();
            this.initializeDatePickers();
            this.initializeSelectFields();

            return this;
        },
        setFormClasses: function setFormClasses() {
            this.formElement.find('input').addClass('form-control');
            this.formElement.find("[type='checkbox']").removeClass('form-control');
            this.formElement.find('textarea').addClass('form-control');
            this.formElement.find('select').addClass('select-two');
        },
        initializeDatePickers: function initializeDatePickers() {
            var dateElements = this.formElement.find('[name*="date"]:not([name*="utcoffset"])')

            dateElements.wrap("<div class='datetimepicker input-group date'></div>");
            dateElements.after(
                $("<span class='input-group-addon'><span class='glyphicon glyphicon-calendar'></span></span>")
            );

            dateElements.parents('.datetimepicker').datetimepicker({
                format: 'YYYY-MM-DD HH:mm',
                sideBySide: true
            });
        },
        initializeSelectFields: function initializeSelectFields() {
            this.formElement.find('.select-two').select2();
        },
        getFieldByName: function getFieldByName(fieldName) {
            var selector = '[name="' + fieldName + '"]';
            return this.formElement.find(selector);
        },
        clearFields: function clearFields(fields) {
            fields.find('textarea, input').val('');
            fields.find('input[type="checkbox"]').prop('checked', false);
            fields.find('select').val(undefined).trigger('change');
            fields.find('select').prop('checked', false);
        }
    };

    var actionForm = {
        initialize: function initializeActionForm(formElement) {
            Object.getPrototypeOf(this).initialize.call(this, formElement);
        }
    };

    var equipmentForm = {
        initialize: function initializeEquipmentForm(formElement) {
            Object.getPrototypeOf(this).initialize.call(this, formElement);
        }
    };

    var factoryServiceForm = {
        initialize: function initializeFactoryServiceForm(formElement) {
            Object.getPrototypeOf(this).initialize.call(this, formElement);
            this.bindDatePickerEvents();
            this.checkDateIntegrity();
            return this;
        },
        bindDatePickerEvents: function bindDatePickerEvents() {
            var thisForm = this;
            var endDatetime = this.getDateRangeObjects().endDatetime;
            this.getFieldByName('begindatetime').parents('.datetimepicker').on('dp.hide', function() {
                thisForm.checkDateIntegrity(); // make sure begin and end datetimes are consistent with each other.
                endDatetime.show();
            });
        },
        checkDateIntegrity: function checkDateIntegrity() {
            var dateObjects = this.getDateRangeObjects();
                // if the new beginDatetime is greater than the current endDatetime, set end time to begin time
                if (dateObjects.endDatetime.date() < dateObjects.beginDatetime.date()) {
                    dateObjects.endDatetime.date(dateObjects.beginDatetime.date());
                }
                // update endDatetime min date according to the new beginDatetime
                dateObjects.endDatetime.minDate(dateObjects.beginDatetime.date());
        },
        getDateRangeObjects: function getDateRangeObjects() {
            return {
                beginDatetime: this.getFieldByName('begindatetime').parents('.datetimepicker').data('DateTimePicker'),
                endDatetime: this.getFieldByName('enddatetime').parents('.datetimepicker').data('DateTimePicker')
            }
        }
    };

    var visitForm = {
        childActions: []
    };

    var formMap = {
        'action': actionForm,
        'visit': visitForm,
        'equipment': equipmentForm,
        'factory_service': factoryServiceForm
    };

    self.createForm = function createForm(formElement) {
        var formType = formElement.data('form-type');
        var formObject = Object.assign(Object.create(form), formMap[formType]).initialize(formElement);
        return formObject;
    };

    return self;
});