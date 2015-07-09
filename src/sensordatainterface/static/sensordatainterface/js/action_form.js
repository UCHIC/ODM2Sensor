function addActionForm(that) {
    var button = $(that).parents('tbody');
    var form = $('#action-form').children();
    var siteVisitForm = $('.form-table').children().first();
    var beginDTInitialValue = siteVisitForm.find("[name='begindatetime']").val();
    var endDTInitialValue = siteVisitForm.find("[name='enddatetime']").val();
    var thisForm = form.clone();

    //Move add button and insert delete button
    thisForm.insertBefore(button);
    button.prev().prepend('<tr><th></th><td><a class="btn btn-danger col-xs-2 col-sm-2" onclick="javascript:deleteActionForm(this)">- Remove Action</a></td></tr>');

    //restart datetimepicker
    //format: 'm/d/Y H:i'
    $(thisForm).find('.datetimepicker').datetimepicker(
    {
        format: 'YYYY-MM-DD HH:mm'
    })
        .on('changeDate', beginDTChanged);

    //Initialize data and UTCOffset for children action forms
    //set the value of the begin time in the action form to the site visit form begin time
    thisForm.find("[name='begindatetime']").val(beginDTInitialValue);
    thisForm.find("[name='enddatetime']").val(endDTInitialValue);

    setFormEndTime(thisForm.find("[name='enddatetime']"), new Date(beginDTInitialValue));

    thisForm.find("[name='begindatetimeutcoffset']").val(siteVisitForm.find("[name='begindatetimeutcoffset']").val());
    thisForm.find("[name='enddatetimeutcoffset']").val(siteVisitForm.find("[name='enddatetimeutcoffset']").val());

    //add handler for when the actiontypecv is changed
    $(thisForm).find('.select-two[name="actiontypecv"]').change(function () {
        var selected = $(this).val();
        var currentActionForm = $(this).parents('tbody');
        handleActionTypeChange(selected, currentActionForm);
    });

    //Fix error with select2
    $(thisForm).find(".select2-container").remove();
    $(thisForm).find(".select-two").select2();
    $(thisForm).find(".select2-container").attr('style', 'width:85%');

    // This bit of code solves the problem of th checkbox not sending status when is unchecked.
    // ie. it will not send False to the server
    $(thisForm).find('.maintenance[type="checkbox"]').change(setIsFactoryServiceFlag);

    setTimeBoundaries(thisForm, beginDTInitialValue, endDTInitialValue);

    //add button for adding new equiment
    //var insertPosition = $(thisForm).find('[name="equipmentused"]', '[name="methodid"]').eq(0).parents('tr');
    //var addEquipmentButton = '<tr><th></th><td><a class="btn btn-default col-xs-2 col-sm-2" onclick="javascript:addEquipmentField(this)">- Add Equipment Used</a></td></tr>';
    //$(addEquipmentButton).insertAfter(insertPosition);

    handleActionTypeChange('Generic', thisForm);

    setFormFields();

    //hide custom fields for all action form types
    $(thisForm).find(".calibration").parents('tr').hide();
    $(thisForm).find(".maintenance").parents('tr').hide();
}

function setIsFactoryServiceFlag() {
    var thisCheckBox = $(this);
    var hiddenCheckBox = thisCheckBox.parents('tbody').find('#id_isfactoryservicebool');
    if (thisCheckBox[0].checked) {
        hiddenCheckBox.attr('value', 'True');
    } else {
        hiddenCheckBox.attr('value', 'False');
    }
}

function deleteActionForm(that) {
    $(that).parents('tbody').remove();
}

function addEquipmentField(that) {
    // Change this function to add a nested form for equipment used...
    var newField = $($('#action-form').find('[name="equipmentused"]').parents('tr').clone());
    var select2Elem = newField.find('[name="equipmentused"]');
    newField.insertBefore($(that).parents('tr'));
    select2Elem.next('.select2-container').remove();
    select2Elem.select2();
    select2Elem.next('.select2-container').attr('style', 'width:85%');
}

function handleActionTypeChange(formType, currentForm) {
    var formClasses = {
        'Generic': 'notypeclass',
        'EquipmentDeployment': 'deployment',
        'InstrumentCalibration': 'calibration',
        'EquipmentMaintenance': 'maintenance'
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
    methodSelect.next('select2-container').remove();
    methodSelect.select2();
    methodSelect.next('select2-container').attr('style', 'width:85%');
}

function beginDTChanged(ev) {
    var changedInputName = $(ev.currentTarget).find('input').attr('name');
    if (changedInputName !== 'enddatetime') {
        var beginDate = new Date($(this).find('input').val());
        var endDTElem = $(ev.currentTarget).parents('tbody').find("[name='enddatetime']");
        setFormEndTime(endDTElem, beginDate)
    }
}

function setFormEndTime(endTimeElem, newDate) {
    var endDTPickerObj = $(endTimeElem.parents('.datetimepicker')).data('datetimepicker');
    var elemInitiallyEmpty = endTimeElem.val() === "";
    var endLessThanBegin = !elemInitiallyEmpty && newDate < new Date(endTimeElem.val());


    //endDTPickerObj.setStartDate(newDate);

    //if (!endLessThanBegin) {
    //    endDTPickerObj.setDate(newDate);
    //}
    //
    //if (elemInitiallyEmpty) {
    //    endTimeElem.val("");
    //}

}

function setTimeBoundaries(that, startDateTime, endDateTime) {
    var beginDTElem = $(that).find('[name="begindatetime"]');
    var endDTElem = $(that).find('[name="enddatetime"]');
    var beginDTObj = beginDTElem.parents('.datetimepicker').data('datetimepicker');
    var endDTObj = endDTElem.parents('.datetimepicker').data('datetimepicker');

    if (beginDTObj && endDTObj) {
        if (startDateTime) {
            var startDTObj = new Date(startDateTime);

            //beginDTObj.setStartDate(startDTObj);
            //endDTObj.setStartDate(startDTObj);

            //if (startDTObj > new Date(beginDTElem.val())) {
            //    beginDTObj.setDate(startDTObj);
            //}
            //
            //if (startDTObj > new Date(endDTElem.val())) {
            //    endDTObj.setDate(startDTObj);
            //}
        }

        if (endDateTime) {
            var finishDTObj = new Date(endDateTime);

            //beginDTObj.setEndDate(finishDTObj);
            //endDTObj.setEndDate(finishDTObj);
            //
            //if (finishDTObj < new Date(beginDTElem.val())) {
            //    beginDTObj.setDate(finishDTObj)
            //}
            //
            //if (finishDTObj < new Date(endDTElem.val())) {
            //    endDTObj.setDate(finishDTObj)
            //}
        }

    }
}

function changeDateTimeBoundaries() {
    var startDateTime = $(this).parents('tbody').find('[name="begindatetime"]').val();
    var endDateTime = $(this).parents('tbody').find('[name="enddatetime"]').val();

    $(this).parents('table').find('tbody').each(function (index) {
        if (index > 0)
            setTimeBoundaries(this, startDateTime, endDateTime)
    });
}

function setEquipmentUsedNumber(event) {
    var equipmentUsedElems = $('.input-group tbody').find('[name="equipmentused"]');

    for (var i = 0; i < equipmentUsedElems.length; i++) {
        var equipmentUsedElem = $(equipmentUsedElems[i]);
        var equipmentUsedCount = equipmentUsedElem.val().length;
        equipmentUsedElem.parents('tbody').find('[name="equipmentusednumber"]').val(equipmentUsedCount);
    }

}

$(document).ready(function () {
    $('.input-group').submit(setEquipmentUsedNumber);

    // Set boundaries of child form datetime fields according to datetime fields of parent site visit
    var siteVisitForm = $(this).find('tbody')[0];
    $(siteVisitForm).find('.datetimepicker').datetimepicker({
        format: 'yyyy-MM-dd hh:mm:ss'
    })
        .on('changeDate', changeDateTimeBoundaries);

    var allForms = $('tbody');

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
