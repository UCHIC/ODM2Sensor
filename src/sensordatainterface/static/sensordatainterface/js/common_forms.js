//This file is intended to be used only on forms pages with forms

// this action works for the create forms in Action, Deployment and Calibration pages.
// It hides fields from the action forms depending on the type of action being created.
function setOtherActions() {
    var mainForm = $('form');
    var actionTypeElem;

    if (mainForm.hasClass('Generic')) {
        $('.Generic .calibration').not('option').parents('tr').hide();
        $('.Generic .maintenance').not('option').parents('tr').hide();
        actionTypeElem = $('.Generic [name="actiontypecv"]');
        actionTypeElem.children('[value="Equipment deployment"]').remove();
        actionTypeElem.children('[value="Instrument calibration"]').remove();

    } else if (mainForm.hasClass('InstrumentCalibration')) {
        /* Careful when deleting parents of calibration etc tr */
        $('.InstrumentCalibration .maintenance').not('option').parents('tr').remove();
        actionTypeElem = $('.InstrumentCalibration [name="actiontypecv"]');
        actionTypeElem.select2('val', 'Instrument calibration');
        actionTypeElem.parents('tr').hide();

    } else if (mainForm.hasClass('EquipmentDeployment')) {
        $('.EquipmentDeployment .calibration').not('option').parents('tr').hide();
        $('.EquipmentDeployment .maintenance').not('option').parents('tr').hide();
        actionTypeElem = $('.EquipmentDeployment [name="actiontypecv"]');
        actionTypeElem.select2('val', 'Equipment deployment');
        actionTypeElem.parents('tr').hide();
    }
}

function initDTPicker() {
    /* http://tarruda.github.io/bootstrap-datetimepicker/ */
    var dateElements = [];
    // Push elements to get calendar widget
    dateElements.push($('#id_equipmentpurchasedate'));
    dateElements.push($("[name='begindatetime']"));
    dateElements.push($("[name='enddatetime']"));
    dateElements.push($("[name='referencematerialpurchasedate']"));
    dateElements.push($("[name='referencematerialexpirationdate']"));

    dateElements.forEach(function (element) {
        element.wrap("<div class='datetimepicker input-group date'></div");
        element.after(
            $("<span class='input-group-addon'><span class='glyphicon glyphicon-calendar'></span></span>")
        );

    });

    var currentDateTimePicker = $('.datetimepicker');
    currentDateTimePicker.datetimepicker({
        format: 'YYYY-MM-DD HH:mm'
    });
}

function setDateTimePicker() {
    initDTPicker();

    //When begindatetime changes, set maxDate on enddatetime
    var tBodies = $('tbody');
    tBodies.each(function () {
        beginDateTimeChanged(this, true);
    });

}

function setDTPickerClose(beginDTElem) {
    //Function to set up begindatetime fields to close automatically when date is picked and open next enddatetime field.
    beginDTElem.parent('.datetimepicker').on('dp.change', function () {
        var beginDTObj = $(this).data('DateTimePicker');
        if (beginDTObj.collapse) {
            beginDTObj.hide();
            var endDTObj = $(this).parents('tbody').find('[name="enddatetime"]').parents('.datetimepicker').data('DateTimePicker');
            endDTObj.show();
            endDTObj.date(beginDTObj.date())
        }
    })
}

function setFormFields(currentForm) {
    currentForm.find('input').addClass('form-control');
    currentForm.find("[type='checkbox']").removeClass('form-control');
    currentForm.find('textarea').addClass('form-control');
    currentForm.find('select').addClass('select-two');

    currentForm.find(".select-two").select2();
    currentForm.find('.select2-container').css('width', '100%');
}

function handleActionTypeChange(formType, currentForm) {
    var formClasses = {
        'Field activity': 'notypeclass',
        'Equipment deployment': 'deployment',
        'Instrument calibration': 'calibration',
        'Equipment maintenance': 'maintenance'
    };

    for (var key in formClasses) {
        if (formClasses.hasOwnProperty(key) && key !== formType) {
            $(currentForm).find('.' + formClasses[key]).not('option').parents('tr').hide();
            $(currentForm).find('option.' + formClasses[key]).attr('disabled', 'disabled');
        }
    }

    if (formClasses.hasOwnProperty(formType)) {
        $(currentForm).find('.' + formClasses[formType]).not('option').parents('tr:hidden').show();
        $(currentForm).find('option.' + formClasses[formType]).removeAttr('disabled');
    }

    //reset select2 to hide disabled options
    var methodSelect = $(currentForm).find('[name="methodid"]');
    methodSelect.select2();
    $('.select2-container').css('width', '100%');

    var equipmentUsedElem = $(currentForm).find('[name="equipmentused"]');

    //Set EquipmentUsed required
    if (formType !== 'Generic')
        equipmentUsedElem.parents('tr').addClass('form-required');
    else
        equipmentUsedElem.parents('tr').removeClass('form-required');

    //Filter equipmentUsed
    filterEquipmentBySite($('form').find('.select-two[name="samplingfeatureid"]').val(), equipmentUsedElem);
}

function filterEquipmentBySite(selected, equipmentUsedSelectElems) {
    if (selected == "")
        return;

    var equipmentBySiteUrl = $('#equipment-by-site-api').val();

    $.ajax({
        url: equipmentBySiteUrl, /*needs to be changed depending on application name. ie in development it's ODM2Sensor, in sandbox it's equipment*/
        type: "POST",
        data: {
            site_selected: selected,
            csrfmiddlewaretoken: $('form').find('[name="csrfmiddlewaretoken"]').val()
        },

        success: function (json) {
            handle_equ_used_filter_response(json, equipmentUsedSelectElems)
        },

        error: function (xhr, errmsg, err) {
            console.log(errmsg);
            console.log(xhr.status + ": " + xhr.responseText)
        }
    });
}

function filterEquipmentByAction(selected, equipmentUsedSelectElems) {
    if(selected == "")
        return;

    var equipmentByActionUrl = $('#equipment-by-action-api').val();

    $.ajax({
        url: equipmentByActionUrl,
        type: "POST",
        data :{
            action_id: selected,
            csrfmiddlewaretoken: $('form').find('[name="csrfmiddlewaretoken"]').val()
        },

        success: function (json) {
            handle_equ_used_filter_response(json, equipmentUsedSelectElems)
        },

        error: function (xhr, errmsg, err) {
            console.log(errmsg);
            console.log(xhr.status+": "+xhr.responseText)
        }
    });
}

function handle_equ_used_filter_response(json, equipmentUsedSelectElems) {
            var currentValue;
            equipmentUsedSelectElems.each(function () {
                currentValue = $(this).parents('tbody').find('[name="actiontypecv"]').val();
                var currentEquipmentSelect = this;
                if (currentValue !== "Equipment deployment") {
                    $(currentEquipmentSelect).empty();
                    $.each(json, function (key, value) {
                        $(currentEquipmentSelect).append('<option value=' + key + '>' + value + '</option>');
                    });
                } else {
                    var defaultElements = $('#action-form').find('[name="equipmentused"]').children();
                    if (defaultElements.length > 0) {
                        $(currentEquipmentSelect).empty();
                        $(currentEquipmentSelect).append($(defaultElements).clone());
                    }
                }

                // Clear value of equipment selected. An equipment can't be deployed at two locations.
                //$(currentEquipmentSelect).select2("val", "");
            });
        }

$(document).ready(function () {
    setDateTimePicker();
    setDTPickerClose($('[name="begindatetime"]'));
    setFormFields($('tbody'));
    setOtherActions();

    var allForms = $('tbody').has('[name="actiontypecv"]');

    allForms.each(function (index) {
        var actionType = $(this).find('.select-two[name="actiontypecv"]');
        handleActionTypeChange(actionType.val(), this);
        actionType.change(function () {
            var selected = $(this).val();
            var currentActionForm = $(this).parents('tbody');
            handleActionTypeChange(selected, currentActionForm);
        });
    });

    $('form').find('[name="actionid"]').change(function () {
        var form = $('form');
        var formActionType = form.find('[name="actiontypecv"]').val();
        if (formActionType != "Equipment deployment" && formActionType != "Instrument deployment")
            filterEquipmentByAction($(this).val(), form.find('[name="equipmentused"]'));
    })
});

