//var actionNumber = 1;

function addActionForm(that) {
    var button = $(that).parents('tbody');
    var form = $('#action-form').children();
    var thisForm = form.clone();
    //thisForm.data('action-number', actionNumber++);


    //Move add button and insert delete button
    thisForm.insertBefore(button);
    button.prev().prepend(
        '<tr><th></th><td><a class="btn btn-remove-action btn-danger col-xs-2 col-sm-2" onclick="javascript:deleteActionForm(this)">- Remove Action</a></td></tr>'
    );

    setChildActionDateTimePicker(thisForm);

    //add handler for when the actiontypecv is changed
    $(thisForm).find('.select-two[name="actiontypecv"]').change(function() {
        var selected = $(this).val();
        var currentActionForm = $(this).parents('tbody');
        handleActionTypeChange(selected, currentActionForm);
    });

    bindEquipmentUsedFiltering($(thisForm).find('.select-two[name="equipmentused"]'));
    $(thisForm).find('[name="equipment_by_site"]').change(function() {
        filterEquipmentUsed(filterEquipmentBySite, $('form').find('[name="samplingfeatureid"]').val(), $(thisForm)); // what is this?
    });

    bindDeploymentField($(thisForm));
    filterDeployments($('form').find('[name="samplingfeatureid"]').val(), false, $(thisForm).find('[name="deploymentaction"]'));

    //Fix error with select2
    $(thisForm).find(".select2-container").remove();
    $(thisForm).find(".select-two").select2();

    // This bit of code solves the problem of the checkbox not sending status when is unchecked.
    // ie. it will not send False to the server
    $(thisForm).find('.maintenance[type="checkbox"]').change(setIsFactoryServiceFlag);

    handleActionTypeChange('Field activity', thisForm);

    setFormFields($(thisForm));

    //hide custom fields for all action form types
    $(thisForm).find(".calibration").not('option').parents('tr').hide();
    $(thisForm).find(".maintenance").not('option').parents('tr').hide();
}


function addAnnotationForm(that) {
    var removeButton = $('<tr class="remove-button"><th></th><td><a class="btn btn-remove-annotation btn-danger col-xs-2 col-sm-2" onclick="javascript:removeAnnotation(this)">- Remove Annotation</a></td></tr>');
    var fields = $('#annotation-form').children().clone();
    var btnForm = $(that).parents('tbody');

    setAnnotationDateTimePicker(fields);

    fields.prepend(removeButton);

    var annotationSelect = fields.find('[name="annotationid"]');
    fields.find('tr:not(.remove-button)').not(annotationSelect.parents('tr')).hide();
    fields.find(".select-two").select2();

    $('<option value="new">New Annotation</option>').insertAfter(annotationSelect.children().first());
    annotationSelect.on('change', { form: fields }, onAnnotationChange);

    fields.insertBefore(btnForm);
}

function removeAnnotation(that) {
    $(that).parents('tbody').remove();
}

function onAnnotationChange(event) {
    var annotationForm = event.data['form'];
    var annotationSelect = annotationForm.find('[name="annotationid"]');
    var newAnnotationFields = annotationForm.find('tr:not(.remove-button)').not(annotationSelect.parents('tr'));

    if (annotationSelect.find(':selected').val() == 'new') {
        newAnnotationFields.show();
        annotationSelect.parents('tr').removeClass('form-required').hide();
    } else {
        newAnnotationFields.hide();
        annotationSelect.parents('tr').addClass('form-required');
    }
}

function setAnnotationDateTimePicker(annotationForm) {
    var siteVisitForm = $('.form-table').children('tbody').first();
    var beginDTInitialValue = moment(siteVisitForm.find("[name='begindatetime']").val());
    var endDTInitialValue = moment(siteVisitForm.find("[name='enddatetime']").val());

    //restart datetimepicker
    $(annotationForm).find('.datetimepicker').datetimepicker({
        format: 'YYYY-MM-DD HH:mm',
        sideBySide: true
    });

    //Initialize data and UTCOffset for children action forms
    //set the value of the begin time in the action form to the site visit form begin time
    annotationForm.find("[name='annotationdatetime']").parent('.datetimepicker').data('DateTimePicker').date(beginDTInitialValue);
    annotationForm.find("[name='annotationutcoffset']").val(siteVisitForm.find("[name='begindatetimeutcoffset']").val());
}

function setChildActionDateTimePicker(childForm) {
    var siteVisitForm = $('.form-table').children().first();
    var beginDTInitialValue = moment(siteVisitForm.find("[name='begindatetime']").val());
    var endDTInitialValue = moment(siteVisitForm.find("[name='enddatetime']").val());

    //restart datetimepicker
    $(childForm).find('.datetimepicker').datetimepicker(
        {
            format: 'YYYY-MM-DD HH:mm',
            sideBySide: true
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
    var form = $(that).parents('tbody');
    if (form.next('tbody').hasClass('results-set')) {
        form.nextUntil('tbody.add-result-btn', '.results-set').remove();
        form.next('tbody.add-result-btn').remove();
    }

    form.remove();
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

function setMultipleFieldsNumber(event) {
    var object = event.data.object;
    var multipleObjElems = $('.input-group tbody').find('[name="' + object + '"]');

    for (var i = 0; i < multipleObjElems.length; i++) {
        var multipleObjElem = $(multipleObjElems[i]);
        var selectedValue = multipleObjElem.val();
        var count = 0;
        if (typeof selectedValue == 'string') {
            count = (selectedValue.length != 0)? 1: 0; // cause why not. who cares?
        } else count = !selectedValue? 0 : selectedValue.length;
        multipleObjElem.parents('tbody').find('[name="' + object + 'number"]').val(count);
    }

}

function setEquipmentUsedFilter() {
    $('form').find('.select-two[name="samplingfeatureid"]').change(function(event) {
        var actionTypeSelects = $('form').find('[name="actiontypecv"]');
        actionTypeSelects.each(function(index, select) {
            var actionType = $(select).val();
            var currentForm = $(select).parents('tbody');
            filterEquipmentUsed(filterEquipmentBySite, $(event.target).val(), currentForm);
            filterDeploymentsByType(actionType, currentForm.find('[name="deploymentaction"]'));
        });
    });
}

function setChildBoundsListener() {
    // Set boundaries of child form datetime fields according to datetime fields of parent site visit
    var siteVisitForm = $('form').find('tbody')[0];
    $(siteVisitForm).find('.datetimepicker').on('dp.change', setChildActionFormBounds);
}

function setChildActionFormBounds(ev) {
    var childForms = $('.form-table').children('tbody').has('[name="enddatetime"]');
    for (var i = 1; i < childForms.length; i++)
        setIndividualBounds($(childForms[i]))
}

$(document).ready(function () {
    var formItems = $('form.input-group');
    formItems.submit({object: 'equipmentused'}, setMultipleFieldsNumber);
    formItems.submit({object: 'calibrationstandard'}, setMultipleFieldsNumber);
    formItems.submit({object: 'calibrationreferenceequipment'}, setMultipleFieldsNumber);

    setChildBoundsListener();
    setEquipmentUsedFilter();

    $('tbody').has('[name="actiontypecv"]').find('.maintenance[type="checkbox"]').change(setIsFactoryServiceFlag);

    var annotationSelects = $('#annotation-form').find('.select-two');
    if (annotationSelects.length !== 0) {
        annotationSelects.select2('destroy');
        $('#annotation-form').find(".select2-container").remove();
    }

    $('.annotation-fields').each(function(index, annotationForm) {
        annotationForm = $(annotationForm);

        if (annotationForm.parent().attr('id') === 'annotation-form') {
            return;
        }

        setAnnotationDateTimePicker(annotationForm);
        var annotationSelect = annotationForm.find('[name="annotationid"]');
        annotationForm.find('tr:not(.remove-button)').not(annotationSelect.parents('tr')).hide();
        annotationForm.find(".select-two").select2();

        $('<option value="new">New Annotation</option>').insertAfter(annotationSelect.children().first());
        annotationSelect.on('change', { form: annotationForm }, onAnnotationChange);
    });

});
