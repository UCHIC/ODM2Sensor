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


    endDTPickerObj.setStartDate(newDate);

    if (!endLessThanBegin) {
        endDTPickerObj.setDate(newDate);
    }

    if (elemInitiallyEmpty) {
        endTimeElem.val("");
    }

}

function addActionForm(that) {
    var button = $(that).parents('tbody');
    var form = $('#action-form').children();

    //Move add button and insert delete button
    var thisForm = form.clone();
    thisForm.insertBefore(button);
    button.prev().prepend('<tr><th></th><td><a class="btn btn-danger col-xs-2 col-sm-2" onclick="javascript:deleteActionForm(this)">- Remove Action</a></td></tr>');

    //restart datetimepicker
    //format: 'm/d/Y H:i'
    $('.datetimepicker').datetimepicker({
        format: 'yyyy-MM-dd hh:mm:ss'
    })
    .on('changeDate', beginDTChanged);

    //Initialize data and UTCOffset for children action forms
    var siteVisitForm = $('.form-table').children().first();

    //set the value of the begin time in the action form to the site visit form begin time
    thisForm.find("[name='begindatetime']").val(siteVisitForm.find("[name='begindatetime']").val());

    //same as above, but with end time
    thisForm.find("[name='enddatetime']").val(siteVisitForm.find("[name='enddatetime']").val());

    setFormEndTime(thisForm.find("[name='enddatetime']"), new Date(siteVisitForm.find("[name='begindatetime']").val()));

    thisForm.find("[name='begindatetimeutcoffset']").val(siteVisitForm.find("[name='begindatetimeutcoffset']").val());
    thisForm.find("[name='enddatetimeutcoffset']").val(siteVisitForm.find("[name='enddatetimeutcoffset']").val());

    //Fix error with select2
    $(".select2-container").remove();
    $(".select-two").select2();
    $(".select2-container").attr('style', 'width:85%');

    //add handler for when the actiontypecv is changed
    $(thisForm).find('.select-two[name="actiontypecv"]').change(function () {
        var selected = $(this).val();
        var currentActionForm = $(this).parents('tbody');
        formSelected(selected, currentActionForm);
    });

    // This bit of code solves the problem of th checkbox not sending status when is unchecked.
    // ie. it will not send False to the server
    $(thisForm).find('.maintenance[type="checkbox"]').change(function () {
        var thisCheckBox = $(this);
        var hiddenCheckBox = thisCheckBox.parents('tbody').find('#id_isfactoryservicebool');
        if (thisCheckBox[0].checked) {
            hiddenCheckBox.attr('value', 'True');
        } else {
            hiddenCheckBox.attr('value', 'False');
        }
    });

    //hide custom fields for all action form types
    $(thisForm).find(".calibration").parents('tr').hide();
    $(thisForm).find(".maintenance").parents('tr').hide();
}

function deleteActionForm(that) {
    $(that).parents('tbody').remove();
}

function formSelected(formType, currentForm) {
    var formClasses = {
        'EquipmentDeployment': 'deployment',
        'InstrumentCalibration': 'calibration',
        'EquipmentMaintenance': 'maintenance'
    };

    for (var key in formClasses) {
        if (formClasses.hasOwnProperty(key) && key !== formType) {
            $(currentForm).find('.' + formClasses[key]).parents('tr').hide();
        }
    }

    if (formClasses.hasOwnProperty(formType)) {
        $(currentForm).find('.' + formClasses[formType]).parents('tr:hidden').show();
    }
}
