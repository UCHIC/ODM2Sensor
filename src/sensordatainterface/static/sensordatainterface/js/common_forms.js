//This file is intended to be used only on forms pages with forms

// this action works for the create forms in Action, Deployment and Calibration pages.
// It hides fields from the action forms depending on the type of action being created.
function setOtherActions() {
    var mainForm = $('form');
    var actionTypeElem;

    if (mainForm.hasClass('Generic')) {
        $('.Generic .calibration').parents('tr').hide();
        $('.Generic .maintenance').parents('tr').hide();
        actionTypeElem = $('.Generic [name="actiontypecv"]');
        actionTypeElem.children('[value="EquipmentDeployment"]').remove();
        actionTypeElem.children('[value="InstrumentCalibration"]').remove();

    } else if (mainForm.hasClass('InstrumentCalibration')) {
        $('.InstrumentCalibration .maintenance').parents('tr').remove();
        actionTypeElem = $('.InstrumentCalibration [name="actiontypecv"]');
        actionTypeElem.select2('val', 'Instrument calibration');
        actionTypeElem.parents('tr').hide();

    } else if (mainForm.hasClass('EquipmentDeployment')) {
        $('.EquipmentDeployment .calibration').parents('tr').hide();
        $('.EquipmentDeployment .maintenance').parents('tr').hide();
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
    currentForm.find('.select2-container').css('width', '85%');
}

function handleActionTypeChange(formType, currentForm) {
    var formClasses = {
        'Generic': 'notypeclass',
        'Equipment deployment': 'deployment',
        'Instrument calibration': 'calibration',
        'Equipment maintenance': 'maintenance'
    };

    for (var key in formClasses) {
        if (formClasses.hasOwnProperty(key) && key !== formType) {
            $(currentForm).find('.' + formClasses[key]).parents('tr').hide();
            $(currentForm).find('.' + key).attr('disabled', 'disabled');
        }
    }

    if (formClasses.hasOwnProperty(formType)) {
        $(currentForm).find('.' + formClasses[formType]).parents('tr:hidden').show();
        $(currentForm).find('.' + formType).removeAttr('disabled');
    }

    //reset select2 to hide disabled options
    var methodSelect = $(currentForm).find('[name="methodid"]');
    methodSelect.select2();
    $('.select2-container').css('width', '85%');

    var equipmentUsedElem = $(currentForm).find('[name="equipmentused"]');

    //Set EquipmentUsed required
    if (formType !== 'Generic')
        equipmentUsedElem.parents('tr').addClass('form-required');
    else
        equipmentUsedElem.parents('tr').removeClass('form-required');

    //Filter equipmentUsed
    filterEquipmentBySite($('form').find('.select-two[name="samplingfeatureid"]'), equipmentUsedElem);
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

    allForms.find('.maintenance[type="checkbox"]').change(setIsFactoryServiceFlag);
});

