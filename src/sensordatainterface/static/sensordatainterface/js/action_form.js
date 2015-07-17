function addActionForm(that) {
    var button = $(that).parents('tbody');
    var form = $('#action-form').children();
    var thisForm = form.clone();

    //Move add button and insert delete button
    thisForm.insertBefore(button);
    button.prev().prepend('<tr><th></th><td><a class="btn btn-danger col-xs-2 col-sm-2" onclick="javascript:deleteActionForm(this)">- Remove Action</a></td></tr>');

    setChildActionDateTimePicker(thisForm);

    //add handler for when the actiontypecv is changed
    $(thisForm).find('.select-two[name="actiontypecv"]').change(function () {
        var selected = $(this).val();
        var currentActionForm = $(this).parents('tbody');
        handleActionTypeChange(selected, currentActionForm);
    });

    //Fix error with select2
    $(thisForm).find(".select2-container").remove();
    $(thisForm).find(".select-two").select2();

    // This bit of code solves the problem of th checkbox not sending status when is unchecked.
    // ie. it will not send False to the server
    $(thisForm).find('.maintenance[type="checkbox"]').change(setIsFactoryServiceFlag);

    //add button for adding new equiment
    //var insertPosition = $(thisForm).find('[name="equipmentused"]', '[name="methodid"]').eq(0).parents('tr');
    //var addEquipmentButton = '<tr><th></th><td><a class="btn btn-default col-xs-2 col-sm-2" onclick="javascript:addEquipmentField(this)">- Add Equipment Used</a></td></tr>';
    //$(addEquipmentButton).insertAfter(insertPosition);

    handleActionTypeChange('Generic', thisForm);

   setFormFields($(thisForm));

    //hide custom fields for all action form types
    $(thisForm).find(".calibration").parents('tr').hide();
    $(thisForm).find(".maintenance").parents('tr').hide();
}

function setChildActionDateTimePicker(childForm) {
    var siteVisitForm = $('.form-table').children().first();
    var beginDTInitialValue = moment(siteVisitForm.find("[name='begindatetime']").val());
    var endDTInitialValue = moment(siteVisitForm.find("[name='enddatetime']").val());

    //restart datetimepicker
    $(childForm).find('.datetimepicker').datetimepicker(
        {
            format: 'YYYY-MM-DD HH:mm'
        }).on('changeDate', beginDateTimeChanged);

    //set initial bounds on dates depending on site visit dates
    setIndividualBounds(childForm);

    //Initialize data and UTCOffset for children action forms
    //set the value of the begin time in the action form to the site visit form begin time
    childForm.find("[name='begindatetime']").parent('.datetimepicker').data('DateTimePicker').date(beginDTInitialValue);
    childForm.find("[name='enddatetime']").parent('.datetimepicker').data('DateTimePicker').date(endDTInitialValue);

    beginDateTimeChanged(childForm, false);

    childForm.find("[name='begindatetimeutcoffset']").val(siteVisitForm.find("[name='begindatetimeutcoffset']").val());
    childForm.find("[name='enddatetimeutcoffset']").val(siteVisitForm.find("[name='enddatetimeutcoffset']").val());

    setDTPickerClose($(childForm).find('[name="begindatetime"]'));
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

function setMultipleFieldsNumber(event) {
    var object = event.data.object;
    var multipleObjElems = $('.input-group tbody').find('[name="' + object + '"]');

    for (var i = 0; i < multipleObjElems.length; i++) {
        var multipleObjElem = $(multipleObjElems[i]);
        var multipleObjCount = multipleObjElem.val().length;
        multipleObjElem.parents('tbody').find('[name="' + object + 'number"]').val(multipleObjCount);
    }

}

function setEquipmentUsedFilter() {
    //add handler for when the actiontypecv is changed
    $('form').find('.select-two[name="samplingfeatureid"]').change(function () {
        filterEquipmentBySite(this, $('form [name="equipmentused"]'));
    });
}

function filterEquipmentBySite(samplingFeatureSelectElement, equipmentUsedSelectElems) {
    var selected = $(samplingFeatureSelectElement).val();

    if (selected == "")
        return;

    $.ajax({
        url: "get-equipment-by-site/",
        type: "POST",
        data: {
            site_selected: selected,
            csrfmiddlewaretoken: $('form').find('[name="csrfmiddlewaretoken"]').val()
        },

        success: function (json) {
            var currentValue;
            equipmentUsedSelectElems.each(function () {
                currentValue = $(this).parents('tbody').find('[name="actiontypecv"]').val();
                var currentEquipmentSelect = this;
                $(currentEquipmentSelect).empty();
                if (currentValue !== "EquipmentDeployment") {
                    $.each(json, function (key, value) {
                        $(currentEquipmentSelect).append('<option value=' + key + '>' + value + '</option>');
                    });
                } else {
                    var defaultElements = $('#action-form').find('[name="equipmentused"]').children();
                    $(currentEquipmentSelect).append($(defaultElements).clone());
                }

                // Clear value of equipment selected. An equipment can't be deployed at two locations.
                $(currentEquipmentSelect).select2("val", "");
            });
            // When actiontype changes check if it is deployment, if it is then empty the select and add the ones on the hidden action form.
            // When an action form is added in the check the type (for thoroughness) and call this function with the site selected.

            //Suggestion: Maybe the equipment that are currently being deployed should be on the selection for other forms in a site visit being created.
        },

        error: function (xhr, errmsg, err) {
            console.log(errmsg);
            console.log(xhr.status + ": " + xhr.responseText)
        }
    });
}

$(document).ready(function () {
    var formItems = $('.input-group');
    formItems.submit({object: 'equipmentused'}, setMultipleFieldsNumber);
    formItems.submit({object: 'calibrationstandard'}, setMultipleFieldsNumber);
    formItems.submit({object: 'calibrationreferenceequipment'}, setMultipleFieldsNumber);

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

    setEquipmentUsedFilter();

});
