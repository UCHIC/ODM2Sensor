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
        if(!($.find('[name="actionid"]').length)) {
            actionTypeElem.children('[value="Equipment retrieval"]').remove();
            actionTypeElem.children('[value="Instrument retrieval"]').remove();
        }
    } else if (mainForm.hasClass('InstrumentCalibration') || mainForm.hasClass('Instrumentcalibration')) {
        /* Careful when deleting parents of calibration etc tr */
        $('.InstrumentCalibration .maintenance').not('option').parents('tr').remove();
        actionTypeElem = $('.InstrumentCalibration [name="actiontypecv"]');
        actionTypeElem.select2('val', 'Instrument calibration');
        $('.InstrumentCalibration [name="equipmentused"]').removeAttr('multiple');
        $('.InstrumentCalibration [name="equipmentused"]').select2();
        actionTypeElem.parents('tr').hide();
    } else if (mainForm.hasClass('EquipmentDeployment')) {
        var site = $('.EquipmentDeployment').find('[name="site_id"]').val();
        if (site !== 'None') {
            filterVisitsBySite(site, $('.EquipmentDeployment').find('[name="actionid"]'));
        }
        $('.EquipmentDeployment').find('#id_equipment_by_site').prop('checked', false).parents('tr').hide();
        $('.EquipmentDeployment .calibration').not('option').parents('tr').hide();
        $('.EquipmentDeployment .maintenance').not('option').parents('tr').hide();
        actionTypeElem = $('.EquipmentDeployment [name="actiontypecv"]');
        actionTypeElem.children(':not([value="Instrument deployment"]):not([value="Equipment deployment"]):not([value=""])').remove();
        $('.EquipmentDeployment').find('[name="enddatetime"]').parents('tr').hide();
        $('.EquipmentDeployment').find('[name="enddatetimeutcoffset"]').parents('tr').hide();
        $('.EquipmentDeployment [name="equipmentused"]').removeAttr('multiple');
        $('.EquipmentDeployment [name="equipmentused"]').select2();
    } else if (mainForm.hasClass('Retrieval')) {
        var deployment = $('.Retrieval').find('[name="deployment_id"]').val();
        if (deployment !== 'None') {
            $('.Retrieval').find('[name="deploymentaction"]').prop('disabled', true);
            $('.Retrieval').find('[name="samplingfeatureid"]').prop('disabled', true);
        }

        $('.Retrieval').find('[name="actiontypecv"]').parents('tr').hide();
        $('.Retrieval').find('[name="deploymentaction"]').parents('tr').addClass('form-required').show();
        filterNonRetrievalFields($('.Retrieval'));
    }
    if (mainForm.hasClass('Instrument Deployment')) {
        if ($('form').find('[name="action"]').val() !== 'update') {
            var addResultButton = $("<tbody class='add-result-btn'><tr><td></td><td><a class='add-result-btn btn btn-default col-xs-12 col-sm-12' onclick='javascript:addResultForm(this)'>+ Add Result</a></td></tr></tbody>");
            addResultButton.insertAfter(currentForm);
            addResultForm(addResultButton, true);
        }
    }

    $('form').find('[name="actionid"]').trigger('change');
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
    dateElements.push($("[name='annotationdatetime']"));

    dateElements.forEach(function (element) {
        element.wrap("<div class='datetimepicker input-group date'></div>");
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
        var currentForm = $(this).parents('tbody');
        var beginDTObj = $(this).data('DateTimePicker');
        var actionType = currentForm.find('[name="actiontypecv"]').val();
        var isDeployment = $('form').hasClass('EquipmentDeployment') || actionType == 'Equipment deployment' || actionType == 'Instrument deployment';


        if (beginDTObj.collapse) {
            beginDTObj.hide();
            var endDTObj = currentForm.find('[name="enddatetime"]').parents('.datetimepicker').data('DateTimePicker');
            if (!isDeployment) {
                endDTObj.show();
                endDTObj.date(beginDTObj.date());
                endDTObj.date(beginDTObj.date());
            }
        }
    });
}

function setFormFields(currentForm) {
    currentForm.find('input').addClass('form-control');
    currentForm.find("[type='checkbox']").removeClass('form-control');
    currentForm.find('textarea').addClass('form-control');
    currentForm.find('select').addClass('select-two');

    currentForm.find(".select-two").select2();
    currentForm.find('.select2-container').css('width', '100%');
}

function handleActionTypeChange(formType, currentForm, form_prefix) {
    var actionId = $(currentForm).find('[name=' + form_prefix + "actionid" + ']').val()
    var requiredEquipmentClasses = ['Equipment maintenance', 'Equipment programming', 'Instrument retrieval',
        'Instrument calibration', 'Equipment deployment', 'Instrument deployment', 'Equipment retrieval'];
    var formClasses = $.map($(currentForm).find('.select-two[name=' + form_prefix + "actiontypecv" + ']').children(), function (option) {
        return option.value;
    }).reduce(function (map, actiontype) {
        map[actiontype] = actiontype.replace(' ', '');
        return map;
    }, {});
    formClasses[""] = "Notype";

    var formClass = formClasses[formType];
    for (var key in formClasses) {
        if (formClasses.hasOwnProperty(key) && key !== formType) {
            $(currentForm).find('.' + formClasses[key]).not('option').parents('tr').hide();
            $(currentForm).find('option.' + formClasses[key]).attr('disabled', 'disabled');
        }
    }

    $(currentForm).find('.' + formClass).not('option').parents('tr:hidden').show();
    $(currentForm).find('option.' + formClass).removeAttr('disabled');

    var methodSelect = $(currentForm).find('[name="methodid"]');
    methodSelect.siblings('.errorlist.no-methods').remove();

    // don't leave this here. or maybe do...
    var methodOptions = methodSelect.find('option:not([disabled])');
    var methods = $.map(methodOptions, function (option) {
        return option.value
    });


    if (methods.indexOf(methodSelect.val()) === -1) {
        methodSelect.val('');
    }


    if (formClass !== 'Notype' && $(currentForm).find('option.' + formClass).length === 0) {
        $('<ul class="errorlist no-methods"><li>No Methods exist for the selected Action Type.</li></ul>').insertBefore($(currentForm).find('#id_methodid'));
    }

    //reset select2 to hide disabled options
    methodSelect.select2();
    $('.select2-container').css('width', '100%');

    var equipmentUsedElem = $(currentForm).find('[name=' + form_prefix +"equipmentused" + ']');

    //Set EquipmentUsed required
    if (requiredEquipmentClasses.indexOf(formType) > -1) {
        equipmentUsedElem.parents('tr').addClass('form-required');
    } else {
        equipmentUsedElem.parents('tr').removeClass('form-required');
    }

    var isSiteVisit = $('form').hasClass('SiteVisit');
    var siteSelect = $('form').find('[name="samplingfeatureid"]');
    var isDeployment = formType == 'Instrument deployment' || formType == 'Equipment deployment';
    var isRetrieval = formType === 'Instrument retrieval' || formType === 'Equipment retrieval';
    var equipmentSelect = $(currentForm).find('[name=' + form_prefix + "equipmentused" + ']');


    if (isSiteVisit) {
        filterDeploymentsByType(formType, $(currentForm).find('[name=' + form_prefix + "deploymentaction" + ']'), form_prefix); //Filter deployments by action type
    }

    if (isDeployment) {
        filterEquipmentUsed(filterEquipmentByDate, $(currentForm).find('[name=' + form_prefix + "begindatetime" + ']').val(), $(currentForm), form_prefix);
        $(currentForm).find('[name=' + form_prefix + "enddatetime" + ']').parents('tr').hide();
        $(currentForm).find('[name=' + form_prefix + "enddatetimeutcoffset" + ']').parents('tr').hide();
        equipmentSelect.parents('tr').show();
        equipmentSelect.removeAttr('multiple');
        equipmentSelect.select2();
    } else if (isRetrieval) {
        $(currentForm).find('[name=' + form_prefix + "deploymentaction" + ']').parents('tr').addClass('form-required');
        filterNonRetrievalFields($(currentForm), form_prefix);
    } else if (!isDeployment && !isRetrieval) {
        filterEquipmentUsed(filterEquipmentBySite, siteSelect.val(), $(currentForm), form_prefix);
        $(currentForm).find('[name=' + form_prefix + "deploymentaction" + ']').parents('tr').removeClass('form-required');
        equipmentSelect.attr('multiple', 'multiple');
        showNonRetrievalFields($(currentForm), form_prefix);
        equipmentSelect.select2();
    }


    if (formType !== 'Instrument deployment') {
        $(currentForm).nextUntil('tbody.add-result-btn', '.results-set').remove();
        $(currentForm).next('tbody.add-result-btn').remove();
    }
    if (formType === 'Instrument deployment') {
        $(currentForm).find('[name=' + form_prefix + "equipmentused" + ']').trigger('change');
        if ($(currentForm).find('tr.form-required').first().html() !== $('form').find('tbody.action-fields tr.form-required').first().html()) {
            var addResultButton = $("<tbody class='add-result-btn'><tr><td></td><td><a class='add-result-btn btn btn-default col-xs-12 col-sm-12' onclick='javascript:addResultForm(this, null, " + actionId + ")'>+ Add Result</a></td></tr></tbody>");
            addResultButton.insertAfter(currentForm);
            addResultForm(addResultButton, true, actionId);
        }
        if ($('form').find('[name="action"]').val() !== 'update' && $('form').find('tbody.results-set').length === 0) {
            var addResultButton = $("<tbody class='add-result-btn'><tr><td></td><td><a class='add-result-btn btn btn-default col-xs-12 col-sm-12' onclick='javascript:addResultForm(this, null, " + actionId + ")'>+ Add Result</a></td></tr></tbody>");
            addResultButton.insertAfter(currentForm);
            addResultForm(addResultButton, true, actionId);
        }
        if ($(currentForm).next().attr('class') !== "results-set"){
            var addResultButton = $("<tbody class='add-result-btn'><tr><td></td><td><a class='add-result-btn btn btn-default col-xs-12 col-sm-12' onclick='javascript:addResultForm(this, null, " + actionId + ")'>+ Add Result</a></td></tr></tbody>");
            addResultButton.insertAfter(currentForm);
            addResultForm(addResultButton, true, actionId);
        }
    }
    if (formType === 'Instrument calibration') {
        $(currentForm).find('[name=' + form_prefix + "instrumentoutputvariable" + ']').parents('tr').addClass('form-required');
        $(currentForm).find('[name=' + form_prefix + "equipmentused" + ']').removeAttr('multiple');
    } else {
        $(currentForm).find('[name=' + form_prefix + "instrumentoutputvariable" + ']').parents('tr').removeClass('form-required');
    }
}

function addResultForm(that, firstResult, actionId) {
    // var actionId = $(that).parents('tbody.add-result-btn').prevUntil('.action-fields').prev('.action-fields').find('[name=' + form_prefix + "actionid" + ']').val()
    var removeButton = $('<tr><th></th><td><a class="btn btn-remove-result btn-danger col-xs-2 col-sm-2" onclick="javascript:removeResultForm(this, ' + actionId + ')">- Remove Result</a></td></tr>');
    var fields = $('#results-form').children().clone();
    var total = $('#id_' + 'resultform-' + actionId  + '-TOTAL_FORMS').val();
    total++;
    $('#id_' + 'resultform' + '-TOTAL_FORMS').val(total);
    var form_prefix = 'resultform-' + actionId + '-' + (total-1).toString() + '-'
    var btnForm;
    fields.find(':input').each(function() {
        if ($(this).attr('name') !== undefined) {
            var name = form_prefix.concat($(this).attr('name'))
            var id = 'id_' + name;
            $(this).attr('name', name)
            $(this).attr('id', id)
        }

    });
    fields.find('label').each(function() {
        var newFor = form_prefix.concat($(this).attr('for'))
        $(this).attr('for', newFor);
    });

    if (firstResult) {
        var resultsRow = $('<tr class="results-row"><td colspan="2" class="results-label"><label>Results</label></td></tr>');
        btnForm = $(that);
        fields.prepend(resultsRow);

    } else {
        btnForm = $(that).parents('tbody.add-result-btn');
        fields.prepend(removeButton);
    }

    fields.find(".select-two").select2();
    fields.insertBefore(btnForm);
    form_prefix = 'actionform-' + (total-1) +'-'
    btnForm.prevUntil('.action-fields').prev('.action-fields').find('[name=' + form_prefix + "equipmentused" + ']').trigger('change');
}

function removeResultForm(that, actionId) {
    // var actionId = btnForm.prevUntil('.action-fields').prev('.action-fields').find('[name=' + form_prefix + "actionid" + ']').val()
    var type = 'resultform-'
    var total = $('#id_' + type + actionId + '-TOTAL_FORMS').val();
    $('#id_' + type + actionId + '-TOTAL_FORMS').val(total-1);
    $('#id_' + type + actionId + '-' +  (total-1) + '-DELETE');
    $(that).parents('tbody').remove();
}


function filterVariablesByEquipment(equipmentElement, form_prefix) {
    var siblingForms = equipmentElement.parents('tbody').nextUntil('.action-fields', '.results-set').andSelf();
    if (siblingForms.last('.result-set').length) {
        form_prefix = form_prefix.replace('actionform', 'resultform')
    }
    var outputVariablesSelects = siblingForms.find('select[name=' + form_prefix + "instrumentoutputvariable" + ']');
    var unitsSelects = siblingForms.find('select[name=' + form_prefix + "unitsid" + ']');
    var selectedEquipment = equipmentElement.val();
    if (!selectedEquipment) {
        outputVariablesSelects.children('option').removeAttr('disabled');
        unitsSelects.children('option').removeAttr('disabled');
        outputVariablesSelects.select2();
        unitsSelects.select2();
        return;
    }

    var variablesByEquipment = $('#output-variables-by-equipment').val();

    $.ajax({
        url: variablesByEquipment,
        type: "POST",
        data :{
            equipment: selectedEquipment,
            csrfmiddlewaretoken: $('form').find('[name="csrfmiddlewaretoken"]').val()
        },

        success: function (json) {
            var variables = JSON.parse(json).map(function(variable) {return variable.pk + ""});
            var units = JSON.parse(json).map(function(variable) {return variable.fields['instrumentrawoutputunitsid'] + ""});

            outputVariablesSelects.children('option').each(function(index, element) {
                if (variables.indexOf(element.value) === -1 && element.value !== '') {
                    $(element).attr('disabled', 'disabled');
                } else {
                    $(element).removeAttr('disabled');
                }
            });
            unitsSelects.children('option').each(function(index, element) {
                if (units.indexOf(element.value) === -1 && element.value !== '') {
                    $(element).attr('disabled', 'disabled');
                } else {
                    $(element).removeAttr('disabled');
                }
            });

            outputVariablesSelects.each(function(index, element) {
                if (variables.indexOf($(element).val()) === -1) {
                    $(element).val('');
                }
            });

            unitsSelects.each(function(index, element) {
                if (units.indexOf($(element).val()) === -1) {
                    $(element).val('');
                }
            });

            outputVariablesSelects.select2();
            unitsSelects.select2();
        },

        error: function (xhr, errmsg, err) {
            console.log(errmsg);
            console.log(xhr.status + ": " + xhr.responseText);
        }
    });
}

function filterEquipmentBySite(selected, equipmentUsedSelectElems, formType) {
    if (!selected) {
        return;
    }

    var equipmentBySiteUrl = $('#equipment-by-site-api').val();

    $.ajax({
        url: equipmentBySiteUrl,
        type: "POST",
        data: {
            formType: formType,
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

function filterEquipmentByInstrument(selected, equipmentUsedSelectElems){
    if(selected == ""){
        return;
    }

    var equipmentByInstrumentUrl = $('#equipment-by-instrument-api').val();

    $.ajax({
        url: equipmentByInstrumentUrl,
        type: "POST",
        data:{
            action: selected,
            csrfmiddlewaretoken: $('form').find('[name="csrfmiddlewaretoken"]').val()
        },
        success: function(json) {
            handle_equ_used_filter_response(json, equipmentUsedSelectElems)

        },

        error: function(xhr, errmsg, err){
            console.log(errmsg)
            console.log(xhr.status+": "+xhr.responseText)
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

function filterEquipmentByDate(date, equipmentUsedSelectElems, formType) {
    if(date == "") {
        return;
    }

    var equipmentByDateUrl = $('#equipment-available-by-date-api').val();

    $.ajax({
        url: equipmentByDateUrl,
        type: "POST",
        data :{
            action_type: formType,
            date: date,
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

function filterDeploymentsByType(formType, deploymentsSelect, form_prefix) {
    if (formType !== 'Instrument retrieval' && formType !== 'Equipment retrieval') {
        return;
    }

    var selectedSite = $('form').find('[name="samplingfeatureid"]').val();
    var visitForm = deploymentsSelect.parents('tbody.action-fields').siblings('tbody.visit-fields');
    var beginDate =  visitForm.find('[name="begindatetime"]').val();
    var endDate =  visitForm.find('[name="enddatetime"]').val();

    if(formType == "" && selectedSite == "") {
        deploymentsSelect.children('option').removeAttr('disabled');
        deploymentsSelect.select2();
        return;
    } else if (formType == "" && selectedSite !== "") {
        filterDeployments(selectedSite, deploymentsSelect);
        return;
    }

    var deploymentsUrl = $('#deployments-by-type-api').val();

    $.ajax({
        url: deploymentsUrl,
        type: "POST",
        data :{
            type: formType,
            site: selectedSite,
            is_update: $('form [name="action"]').val() === "update",
            begindate: beginDate,
            enddate: endDate,
            csrfmiddlewaretoken: $('form').find('[name="csrfmiddlewaretoken"]').val()
        },

        success: function (json) {
            var deployments = JSON.parse(json).map(function(deployment) {return deployment.pk + ""});

            deploymentsSelect.children('option').each(function(index, element) {
                if (deployments.indexOf(element.value) === -1 && element.value !== '') {
                    $(element).attr('disabled', 'disabled');
                } else {
                    $(element).removeAttr('disabled');
                }
            });

            if (deployments.indexOf(deploymentsSelect.val()) === -1) {
                deploymentsSelect.val('');
            }
            deploymentsSelect.select2();
        },

        error: function (xhr, errmsg, err) {
            console.log(errmsg);
            console.log(xhr.status+": "+xhr.responseText)
        }
    });
}

function filterDeployments(selectedId, deploymentsSelect) {
    if(selectedId == "") {
        deploymentsSelect.children('option').removeAttr('disabled');
        deploymentsSelect.select2();
        return;
    }

    var deploymentsUrl = $('#deployments-by-site-api').val();

    $.ajax({
        url: deploymentsUrl,
        type: "POST",
        data :{
            id: selectedId,
            date: deploymentsSelect.parents('tbody').find('[name="begindatetime"]').val(),
            is_update: $('form [name="action"]').val() === "update",
            csrfmiddlewaretoken: $('form').find('[name="csrfmiddlewaretoken"]').val()
        },

        success: function (json) {
            var deployments = JSON.parse(json).map(function(deployment) {return deployment.pk + ""});

            if (deployments.indexOf(deploymentsSelect.val()) === -1) {
                deploymentsSelect.val('');
            }

            deploymentsSelect.children('option').each(function(index, element) {
                if (deployments.indexOf(element.value) === -1 && element.value !== '') {
                    $(element).attr('disabled', 'disabled');
                } else {
                    $(element).removeAttr('disabled');
                }
            });

            deploymentsSelect.select2();
        },

        error: function (xhr, errmsg, err) {
            console.log(errmsg);
            console.log(xhr.status+": "+xhr.responseText)
        }
    });
}

function filterDeploymentsByVisitSite(selectedId, deploymentsSelect) {
    if(selectedId == "") {
        deploymentsSelect.children('option').removeAttr('disabled');
        deploymentsSelect.select2();
        return;
    }

    var deploymentsUrl = $('#deployments-by-visit-site-api').val();

    $.ajax({
        url: deploymentsUrl,
        type: "POST",
        data :{
            id: selectedId,
            is_update: $('form [name="action"]').val() === "update",
            csrfmiddlewaretoken: $('form').find('[name="csrfmiddlewaretoken"]').val()
        },

        success: function (json) {
            var deployments = JSON.parse(json).map(function(deployment) {return deployment.pk + ""});

            if (deployments.indexOf(deploymentsSelect.val()) === -1) {
                deploymentsSelect.val('');
            }

            deploymentsSelect.children('option').each(function(index, element) {
                if (deployments.indexOf(element.value) === -1 && element.value !== '') {
                    $(element).attr('disabled', 'disabled');
                } else {
                    $(element).removeAttr('disabled');
                }
            });

            deploymentsSelect.select2();
        },

        error: function (xhr, errmsg, err) {
            console.log(errmsg);
            console.log(xhr.status+": "+xhr.responseText)
        }
    });
}


function filterVisitsByDeploymentSite(selectedId, visitsSelect) {
    if (selectedId == "") {
        visitsSelect.children('option').removeAttr('disabled');
        visitsSelect.select2();
        return;
    }

    var url = $('#visits-by-deployment-site-api').val();

    $.ajax({
        url: url,
        type: "POST",
        data :{
            id: selectedId,
            csrfmiddlewaretoken: $('form').find('[name="csrfmiddlewaretoken"]').val()
        },

        success: function (json) {
            var visits = JSON.parse(json).map(function(visit) {return visit.pk + ""});

            visitsSelect.children('option').each(function(index, element) {
                if (visits.indexOf(element.value) === -1 && element.value !== '') {
                    $(element).attr('disabled', 'disabled');
                } else {
                    $(element).removeAttr('disabled');
                }
            });

            if (visits.indexOf(visitsSelect.val()) === -1) {
                visitsSelect.val('');
            }

            visitsSelect.select2();
        },

        error: function (xhr, errmsg, err) {
            console.log(errmsg);
            console.log(xhr.status+": "+xhr.responseText)
        }
    });
}


function filterVisitsBySite(selectedId, visitsSelect) {
    if (selectedId == "") {
        visitsSelect.children('option').removeAttr('disabled');
        visitsSelect.select2();
        return;
    }

    var url = $('#visits-by-site-api').val();

    $.ajax({
        url: url,
        type: "POST",
        data :{
            id: selectedId,
            csrfmiddlewaretoken: $('form').find('[name="csrfmiddlewaretoken"]').val()
        },

        success: function (json) {
            var visits = JSON.parse(json).map(function(visit) {return visit.pk + ""});

            visitsSelect.children('option').each(function(index, element) {
                if (visits.indexOf(element.value) === -1 && element.value !== '') {
                    $(element).attr('disabled', 'disabled');
                } else {
                    $(element).removeAttr('disabled');
                }
            });

            if (visits.indexOf(visitsSelect.val()) === -1) {
                visitsSelect.val('');
            }

            visitsSelect.select2();
        },

        error: function (xhr, errmsg, err) {
            console.log(errmsg);
            console.log(xhr.status+": "+xhr.responseText)
        }
    });
}


function setDeploymentEquipment(deploymentId, equipmentUsedSelect) {
    if(deploymentId == "") {
        return;
    }

    var equipmentByActionUrl = $('#equipment-by-deployment-api').val();

    $.ajax({
        url: equipmentByActionUrl,
        type: "POST",
        data :{
            action_id: deploymentId,
            csrfmiddlewaretoken: $('form').find('[name="csrfmiddlewaretoken"]').val()
        },

        success: function (equipmentId) {
            equipmentUsedSelect.children('option').removeAttr('disabled');
            equipmentUsedSelect.val(equipmentId);
            equipmentUsedSelect.select2();
        },

        error: function (xhr, errmsg, err) {
            console.log(errmsg);
            console.log(xhr.status+": "+xhr.responseText)
        }
    });
}

// get site visit dates from get_site_visit_dates, and restrict begindate and enddate
function filterActionDatesByVisit(siteVisitId, form_prefix) {
    if (siteVisitId == '') {
        return;
    }

    var apiUrl = $('#site-visit-dates').val();
    var form = $('form');
    var actionType = form.find('[name=' + form_prefix + "actiontypecv" + ']').val();
    var token = form.find('[name="csrfmiddlewaretoken"]').val();
    var isDeployment = form.hasClass('EquipmentDeployment') || actionType == 'Equipment deployment' || actionType == 'Instrument deployment';

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
            beginDateTimeObj.date(minDatetime);

            if (!isDeployment) {
                endDateTimeObj.maxDate(maxDatetime);
                endDateTimeObj.minDate(minDatetime);
                endDateTimeObj.date(maxDatetime);
            }
        },
        error: function(xhr, errmsg) {
            console.log(errmsg);
            console.log(xhr.status+": "+xhr.responseText)
        }
    });
}


function handle_equ_used_filter_response(objects, equipmentUsedSelectElems) {
    objects = JSON.parse(objects);

    equipmentUsedSelectElems.each(function () {
        var currentEquipmentSelect = $(this);
        var selectedEquipment = $.makeArray(currentEquipmentSelect.val());

        var equipments = objects.map(function(equipment) {
            return equipment.pk + "";
        });

        // if (selectedEquipment.length) {
        //      currentEquipmentSelect.val($.grep(selectedEquipment, function (element) {
        //          return $.inArray(element, equipments) !== -1;
        //      }));
        //   }

        currentEquipmentSelect.children('option').each(function(index, element) {
            if (equipments.indexOf(element.value) === -1) {

                $(element).attr('disabled', 'disabled');
                $(element).attr('hidden', true);
            } else {
                $(element).removeAttr('disabled');
            }
        });

        currentEquipmentSelect.select2();
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

function bindEquipmentUsedFiltering(selectElement, form_prefix) {
    selectElement.change(function(eventData, handler) {
        filterVariablesByEquipment(selectElement, form_prefix);
    });
}

function cleanFields(fields) {
    fields.find('textarea, input').val('');
    fields.find('input[type="checkbox"]').prop('checked', false);
    fields.find('select').val(undefined).trigger('change');
    fields.find('select').prop('checked', false);
}

function cacheUnfilteredSelects() {
    $('#all-equipment-select').append($('#id_equipmentused').children().clone());
}

$(document).ready(function () {
    setDateTimePicker();
    setDTPickerClose($('[name="begindatetime"]'));
    setFormFields($('tbody'));
    cacheUnfilteredSelects();
    var currentForm = $('form');
    var allForms = currentForm.find('tbody.action-fields');
    for (i = 0 ; i < allForms.length ; i++){
        var form_prefix = "actionform-" + i + '-'
        bindEquipmentUsedFiltering($(allForms[i]).find('.select-two[name=' + form_prefix + "equipmentused" + ']'), form_prefix);
    }


    var resultSelects = $('#results-form').find('.select-two');
    if (resultSelects.length !== 0) {
        $('#results-form').find('.select-two').select2('destroy');
        $('#results-form').find(".select2-container").remove();
    }


    var filterEquipmentCheck = $('#id_equipment_by_site');
    var siteVisitSelect = currentForm.find('[name="actionid"]');
    console.log(allForms.length)
    if (currentForm.attr('action').indexOf('create-equipment') > -1) { // if current form is the create new equipment form
        var modelSelect = $('#id_equipmentmodelid');
        $('<option value="new">New Equipment Model</option>').insertAfter(modelSelect.children().first());
        modelSelect.on('change', onEquipmentModelChange);
    }

    allForms.each(function(index, actionForm) {
        var form_prefix = "actionform-" + index + '-'
        var actionType = $(actionForm).find('.select-two[name=' + form_prefix + "actiontypecv" + ']')

        handleActionTypeChange(actionType.val(), actionForm, form_prefix);
        bindDeploymentField($(actionForm));

        actionType.change(function(event) {
            var field = $(event.target);
            var selected = field.val();

            var currentActionForm = field.parents('tbody');
            handleActionTypeChange(selected, currentActionForm, form_prefix);
        });
    });

    if (siteVisitSelect.length !== 0) {
        var actionType = currentForm.find('[name=' + form_prefix + "actiontypecv" + ']').val();
        siteVisitSelect.change(function (eventData, handler) {
            var selectedVisit = siteVisitSelect.val();
            var isRetrieval = actionType == 'Instrument retrieval' || actionType == 'Equipment retrieval';
            var isDeployment = $('form').hasClass('EquipmentDeployment');
            if (!isRetrieval && !isDeployment) {
                filterEquipmentUsed(filterEquipmentByAction, $(this).val(), currentForm);
            } else if (isDeployment) {
                filterEquipmentUsed(filterEquipmentByDate, currentForm.find('[name=' + form_prefix + "begindatetime" + ']').val(), currentForm, actionType);
            }


            var deploymentField = currentForm.find('[name=' + form_prefix + "deploymentaction" + ']');
            filterActionDatesByVisit(selectedVisit, form_prefix);
            if (!deploymentField.prop('disabled') && siteVisitSelect.children('option[disabled]').length === 0) {
                filterDeploymentsByVisitSite(selectedVisit, deploymentField);
            }
        });

        filterEquipmentCheck.change(function(eventData) {
            siteVisitSelect.trigger('change');
        });
    }


    if (currentForm.find('[name=' + form_prefix + "deploymentaction" + ']').val() !== '') {
        currentForm.find('[name=' + form_prefix + "deploymentaction" + ']').trigger('change');
    }
    setOtherActions();
});


function bindDeploymentField(form, form_prefix) {
    var deploymentSelect = form.find('[name=' + form_prefix + "deploymentaction" + ']');
    deploymentSelect.change(function() {
        var deploymentId = deploymentSelect.val();
        var siteVisitSelect = form.find('[name="actionid"]');
        getDeploymentType(deploymentId, form);
        setDeploymentEquipment(deploymentId, form.find('[name=' + form_prefix + "equipmentused" + ']'));

        if (siteVisitSelect.length > 0 && deploymentSelect.children('option[disabled]').length === 0) {
            filterVisitsByDeploymentSite(deploymentId, siteVisitSelect);
        }
    });
}


function getDeploymentType(deploymentId, form) {
    if(deploymentId == "") {
        return;
    }

    var deploymentTypeApi = $('#deployment-type-api').val();

    $.ajax({
        url: deploymentTypeApi,
        type: "POST",
        data :{
            deployment_id: deploymentId,
            csrfmiddlewaretoken: $('form').find('[name="csrfmiddlewaretoken"]').val()
        },

        success: function (deploymentType) {
            var methodSelect = form.find('[name="methodid"]');
            var actiontypeSelect = form.find('[name="actiontypecv"]');
            var methodOptions = methodSelect.find('option:not([disabled])');
            var methods = $.map(methodOptions, function(option) { return option.value });

            if (methods.indexOf(methodSelect.val()) === -1) {
                methodSelect.val('');
            }

            actiontypeSelect.val(deploymentType);
            actiontypeSelect.trigger('change');
        },

        error: function (xhr, errmsg, err) {
            console.log(errmsg);
            console.log(xhr.status+": "+xhr.responseText)
        }
    });
}


function filterNonRetrievalFields(form, form_prefix) {
    form.find('[name=' + form_prefix + "equipmentused" + ']').parents('tr').hide();
    form.find('[name=' + form_prefix + "enddatetime" + ']').parents('tr').hide();
    form.find('[name=' + form_prefix + "enddatetimeutcoffset" + ']').parents('tr').hide();
    form.find('[name=' + form_prefix + "actionfilelink" + ']').parents('tr').hide()
}

function showNonRetrievalFields(form, form_prefix) {
    form.find('[name=' + form_prefix + "equipmentused" + ']').parents('tr').show();
    form.find('[name=' + form_prefix + "enddatetime" + ']').parents('tr').show();
    form.find('[name=' + form_prefix + "enddatetimeutcoffset" + ']').parents('tr').show();
    form.find('[name=' + form_prefix + "actionfilelink" + ']').parents('tr').show()
}


function filterEquipmentUsed(filter, filteringValue, currentForm, form_prefix) {
    var filterEquipmentCheck = currentForm.find('#id_equipment_by_site');
    var formActionType = currentForm.find('[name=' + form_prefix + "actiontypecv" + ']').val();
    var equipmentUsedSelect = currentForm.find('[name=' + form_prefix + "equipmentused" + ']');

    if (formActionType == 'Equipment retrieval' || formActionType == 'Instrument retrieval') {
        equipmentUsedSelect.children('option').removeAttr('disabled');
    } else if (!filterEquipmentCheck.prop('checked')) { // formActionType != "Equipment deployment" && formActionType != "Instrument deployment" &&
        // why was this excluding equipment and instrument deployments? left rest of condition as comment just in case.
        filter(filteringValue, equipmentUsedSelect, formActionType);
    } else {
        equipmentUsedSelect.children('option').removeAttr('disabled');
    }
}