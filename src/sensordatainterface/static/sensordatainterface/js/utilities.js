function removeCommas(table) {
    var lastColumn = table.rows[0].cells.length - 1;

    for (var i = 1; i < table.rows.length; i++) {
        data = table.rows[i].cells[lastColumn].innerHTML.trim();
        table.rows[i].cells[lastColumn].innerHTML = data.substr(0, data.length - 1);
    }
}

function setNavActive() {
    $(".active").removeClass("active");

    var currentPath = window.location.pathname;

    if (currentPath.indexOf("inventory") > 0) {
        $("#inventory-nav").addClass("active");
    } else if (currentPath.indexOf("sites") > 0) {
        $("#sites-nav").addClass("active");
    } else if (currentPath.indexOf("site-visits") > 0) {
        $("#visits-nav").addClass("active");
    } else if (currentPath.indexOf("control-vocabularies") > 0) {
        $("#vocabulary-nav").addClass("active");
    }
}

function setDeleteConfirmation() {
    /*http://ethaizone.github.io/Bootstrap-Confirmation/*/
    $('#danger-button').confirmation({
        placement: 'bottom',
        title: 'Are you sure you want to delete?',
        popout: true,
        btnCancelClass: 'btn-default',
        onCancel: function () {
            $('#danger-button').confirmation('hide');
        }
    });
}

function set_delete_icon() {
    $('.delete-icon').confirmation({
        placement: 'left',
        title: 'Are you sure?',
        btnCancelClass: 'btn-default',
        onCancel: function () {
            $('.delete-icon').confirmation('hide');
        },
        onConfirm: function () {
            var tableClicked = $(this).parents('.dataTables_wrapper').attr('id');
            var table = $('#' + tableClicked);
            var searchText = table.find('input[type="search"]')[0].value;

            sessionStorage.setItem('tableClicked', tableClicked);
            var tablePage = table.find('.paginate_button.current')[0].getAttribute('data-dt-idx');

            if (searchText != "") {
                sessionStorage.setItem('searchTerm', searchText);
                if (tablePage > 0) {
                    sessionStorage.setItem('tablePage', tablePage);
                }
            } else {
                sessionStorage.setItem('tablePage', tablePage);
            }

        }
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

function beginDateTimeChanged(thisTBody, trigger) {
    var endDTElem = $(thisTBody).find('[name="enddatetime"]').parent('.datetimepicker');
    var event = $(thisTBody).find('[name="begindatetime"]')
        .parent('.datetimepicker')
        .on('dp.change', function (ev) {
            var date = moment($(ev.currentTarget).data().date);
            setEndMinDate(thisTBody, date);
        });

    if (trigger && endDTElem.length > 0) {
        event.trigger('dp.change');
        endDTElem.children('input').blur();
        endDTElem.data('DateTimePicker').hide();
    }
}

function setEndMinDate(thisTBody, newDate) {
    $(thisTBody).find('[name="enddatetime"]').parent('.datetimepicker').data('DateTimePicker').minDate(newDate);
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

function setIndividualBounds(actionTBody) {
    var siteVisit = $('.form-table').children('tbody').first();
    var beginSVDate = moment($(siteVisit).find('[name="begindatetime"]').val());
    var endSVDate = moment($(siteVisit).find('[name="enddatetime"]').val());

    var beginDateTimeObj = actionTBody.find('[name="begindatetime"]').parents('.datetimepicker').data('DateTimePicker');
    var endDateTimeObj = actionTBody.find('[name="enddatetime"]').parents('.datetimepicker').data('DateTimePicker');

    // This fixes problem of beginDateTime being after maxDate. Boundaries are reset and set again.
    beginDateTimeObj.maxDate(false);
    beginDateTimeObj.minDate(false);
    endDateTimeObj.maxDate(false);
    endDateTimeObj.minDate(false);

    beginDateTimeObj.maxDate(endSVDate);
    beginDateTimeObj.minDate(beginSVDate);
    endDateTimeObj.maxDate(endSVDate);
    endDateTimeObj.minDate(beginSVDate);

    beginDateTimeObj.hide();
    endDateTimeObj.hide();

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

 function setFormFields(currentForm) {
    currentForm.find('input').addClass('form-control');
    currentForm.find("[type='checkbox']").removeClass('form-control');
    currentForm.find('textarea').addClass('form-control');
    currentForm.find('select').addClass('select-two');

    currentForm.find(".select-two").select2();
    currentForm.find('.select2-container').css('width', '85%');
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

$(document).ready(function () {
    setDateTimePicker();

    setChildBoundsListener();

    setDTPickerClose($('[name="begindatetime"]'));

    setFormFields($('tbody'));

    setNavActive();

    setDeleteConfirmation();

    set_delete_icon();

    $('.dataTables_paginate').click(function () {
        set_delete_icon();
    });

    $('.dataTables_filter').find('input[type="search"]').change(function () {
        set_delete_icon();
    });

    if (typeof (initVocabulariesTabs) == "function") {
        initVocabulariesTabs($);
    }

});
