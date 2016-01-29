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
        actionTypeElem.children('[value="Instrument deployment"]').remove();
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
        // TODO: ASK AMBER IS IT EQUIPMENT OR INSTRUMENT DEPLOYMENT?
        actionTypeElem.select2('val', 'Instrument deployment');
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
        format: 'YYYY-MM-DD HH:mm',
        sideBySide: true
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
    beginDTElem.parent('.datetimepicker').on('dp.hide', function () {
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
        'Instrument deployment': 'deployment',
        'Instrument calibration': 'calibration',
        'Equipment maintenance': 'maintenance'
    };


    var formClass = formClasses[formType] || 'notypeclass';

    for (var key in formClasses) {
        if (formClasses.hasOwnProperty(key) && key !== formType) {
            $(currentForm).find('.' + formClasses[key]).not('option').parents('tr').hide();
            $(currentForm).find('option.' + formClasses[key]).attr('disabled', 'disabled');
        }
    }

    $(currentForm).find('.' + formClass).not('option').parents('tr:hidden').show();
    $(currentForm).find('option.' + formClass).removeAttr('disabled');

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

    if (formType == 'Instrument deployment') {
        var addResultButton = $("<tbody class='add-result-btn'><tr><td></td><td><a class='add-result-btn btn btn-default col-xs-12 col-sm-12' onclick='javascript:addResultForm(this)'>+ Add Result</a></td></tr></tbody>");
        addResultButton.insertAfter(currentForm);
        addResultForm(addResultButton, true);
    } else {
        $(currentForm).nextUntil('tbody.add-result-btn', '.results-set').remove();
        $(currentForm).next('tbody.add-result-btn').remove();
    }
}

function addResultForm(that, firstResult) {
    var removeButton = $('<tr><th></th><td><a class="btn btn-remove-result btn-danger col-xs-2 col-sm-2" onclick="javascript:removeResultForm(this)">- Remove Result</a></td></tr>');
    var fields = $('#results-form').children().clone();

    if (firstResult) {
        var resultsRow = $('<tr class="results-row"><td colspan="2" class="results-label"><label>Results</label></td></tr>');
        var btnForm = $(that);
        fields.prepend(resultsRow);

    } else {
        var btnForm = $(that).parents('tbody.add-result-btn');
        fields.prepend(removeButton);
    }

    fields.find(".select-two").select2();
    fields.insertBefore(btnForm);
}

function removeResultForm(that) {
    $(that).parents('tbody').remove();
}

function filterVariablesByEquipment(equipmentElement) {
    var outputVariablesSelect = equipmentElement.parents('tbody')
        .nextUntil('.action-fields', '.results-set')
        .find('select[name="instrumentoutputvariable"]');

    var equipmentList = equipmentElement.val();

    if (!equipmentList) {
        outputVariablesSelect.empty();
        outputVariablesSelect.append($('#all-variables-select').children().clone());
        return;
    }

    var variablesByEquipment = $('#output-variables-by-equipment').val();

    $.ajax({
        url: variablesByEquipment,
        type: "POST",
        data :{
            equipment: equipmentList,
            csrfmiddlewaretoken: $('form').find('[name="csrfmiddlewaretoken"]').val()
        },

        success: function (json) {
            var optionElements = [];
            var variables = JSON.parse(json);

            outputVariablesSelect.empty();
            variables.forEach(function(variable) {
                optionElements.push('<option value="', variable.pk, '">',
                    variable.fields['modelid'], ': ', variable.fields['variableid'], '</option>'
                );
            });
            outputVariablesSelect.append(optionElements.join(''));
        },

        error: function (xhr, errmsg, err) {
            console.log(errmsg);
            console.log(xhr.status+": "+xhr.responseText)
        }
    });
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
    if(selected == "") {
        return;
    }

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

function showAllEquipment(equipmentUsedSelectElems) {
    equipmentUsedSelectElems.empty();
    equipmentUsedSelectElems.append($('#all-equipment-select').children().clone());
}

// get site visit dates from get_site_visit_dates, and restrict begindate and enddate
function filterActionDatesByVisit(siteVisitId) {
    if (siteVisitId == '') {
        return;
    }

    var apiUrl = $('#site-visit-dates').val();
    var form = $('form');
    var token = form.find('[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        url: apiUrl,
        type: 'POST',
        data: { site_visit: siteVisitId, csrfmiddlewaretoken: token },
        success: function(data) {

            // get datetimepicker stuff and restrict by the dates received.
            var minDatetime = moment(data.begin_date);
            var maxDatetime = moment(data.end_date);

            var beginDateTimeObj = form.find('[name="begindatetime"]').parents('.datetimepicker').data('DateTimePicker');
            var endDateTimeObj = form.find('[name="enddatetime"]').parents('.datetimepicker').data('DateTimePicker');

            beginDateTimeObj.maxDate(false);
            beginDateTimeObj.minDate(false);
            endDateTimeObj.maxDate(false);
            endDateTimeObj.minDate(false);

            beginDateTimeObj.maxDate(maxDatetime);
            beginDateTimeObj.minDate(minDatetime);
            endDateTimeObj.maxDate(maxDatetime);
            endDateTimeObj.minDate(minDatetime);

            beginDateTimeObj.date(minDatetime);
            endDateTimeObj.date(maxDatetime);

            beginDateTimeObj.date(minDatetime);
            endDateTimeObj.date(maxDatetime);
        },
        error: function(xhr, errmsg) {
            console.log(errmsg);
            console.log(xhr.status+": "+xhr.responseText)
        }
    });
}



function handle_equ_used_filter_response(json, equipmentUsedSelectElems) {
    var currentValue;
    json = JSON.parse(json);
    equipmentUsedSelectElems.each(function () {
        currentValue = $(this).parents('tbody').find('[name="actiontypecv"]').val();
        var currentEquipmentSelect = $(this);
        if (currentValue !== "Equipment deployment" && currentValue !== "Instrument deployment") {
            var options = [];
            currentEquipmentSelect.empty();
            json.forEach(function(object) {
                var equipment = object.fields;
                var equipmentElement = ['<option value=', object.pk, '>',
                    equipment.equipmentcode, ': ', equipment.equipmentserialnumber,
                    ' (', equipment.equipmenttypecv, ', ', equipment.equipmentmodelid, ')',
                    '</option>'
                ];
                options.push(equipmentElement.join(''));
            });
            currentEquipmentSelect.append(options.join(''));
        } else {
            var defaultElements = $('#action-form').find('[name="equipmentused"]').children();
            if (defaultElements.length > 0) {
                currentEquipmentSelect.empty();
                currentEquipmentSelect.append($(defaultElements).clone());
            }
        }

        // Clear value of equipment selected. An equipment can't be deployed at two locations.
        //$(currentEquipmentSelect).select2("val", "");
    });
}

function onEquipmentModelChange(event) {
    var modelForm = $('#model-form');
    var modelFields = $('tbody.model-fields');
    var modelSelect = $('#id_equipmentmodelid');

    if (modelSelect.find(':selected').val() == 'new') {
        cleanFields(modelFields);
        modelFields.insertAfter(modelSelect.parents('tbody'));
    } else {
        modelForm.append(modelFields);
    }
}


function bindEquipmentUsedFiltering(selectElement) {
    selectElement.change(function(eventData, handler) {
        filterVariablesByEquipment(selectElement);
    });
}

function cleanFields(fields) {
    fields.find('textarea, input').val('');
    fields.find('input[type="checkbox"]').prop('checked', false);
    fields.find('select').val(undefined).trigger('change');
    fields.find('select').prop('checked', false);
}


$(document).ready(function () {
    setDateTimePicker();
    setDTPickerClose($('[name="begindatetime"]'));
    setFormFields($('tbody'));
    setOtherActions();

    $('#results-form').find('.select-two').select2('destroy');
    $('#results-form').find(".select2-container").remove();

    var currentForm = $('form');
    var allForms = $('tbody').has('[name="actiontypecv"]');
    var filterEquipmentCheck = $('#id_equipment_by_site');
    var siteVisitSelect = currentForm.find('[name="actionid"]');
    var equipmentUsedSelect = $('#id_equipmentused');

    // Cache instrument output variables and equipments
    var variableSelect = $('#all-variables-select');
    var equipmentSelect = $('#all-equipment-select');
    equipmentSelect.append(equipmentUsedSelect.children().clone());
    variableSelect.append($('#id_instrumentoutputvariable').children().clone());

    if (currentForm.attr('action').indexOf('create-equipment') > -1) { // if current form is the create new equipment form
        var modelSelect = $('#id_equipmentmodelid');
        $('<option value="new">New Equipment Model</option>').insertAfter(modelSelect.children().first());
        modelSelect.on('change', onEquipmentModelChange);
    }

    allForms.each(function (index) {
        var actionType = $(this).find('.select-two[name="actiontypecv"]');
        handleActionTypeChange(actionType.val(), this);
        actionType.change(function () {
            var selected = $(this).val();
            var currentActionForm = $(this).parents('tbody');
            handleActionTypeChange(selected, currentActionForm);
        });
    });

    bindEquipmentUsedFiltering(equipmentUsedSelect);

    siteVisitSelect.change(function (eventData, handler) {
        var formActionType = currentForm.find('[name="actiontypecv"]').val();

        if (formActionType != "Equipment deployment" && formActionType != "Instrument deployment" && !filterEquipmentCheck.prop('checked')) {
            filterEquipmentByAction($(this).val(), currentForm.find('[name="equipmentused"]'));
        } else {
            showAllEquipment(currentForm.find('[name="equipmentused"]'));
        }

        if (currentForm.hasClass('EquipmentDeployment') || currentForm.hasClass('InstrumentCalibration') || currentForm.hasClass('Generic')) {
            var siteVisit = eventData.target.options[eventData.target.selectedIndex].value;
            filterActionDatesByVisit(siteVisit);
        }
    });

    filterEquipmentCheck.change(function(eventData) {
        siteVisitSelect.trigger('change');
    });
});

