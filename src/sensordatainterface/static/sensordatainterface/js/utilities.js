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

function beginDateTimeChanged(thisTBody, trigger) {
    var endDTElem = $(thisTBody).find('[name="enddatetime"]').parent('.datetimepicker');
    var actionType = $(thisTBody).find('[name="actiontypecv"]').val();
    var isDeployment = $('form').hasClass('EquipmentDeployment') || actionType == 'Equipment deployment' || actionType == 'Instrument deployment';

    var event = $(thisTBody).find('[name="begindatetime"]')
        .parent('.datetimepicker')
        .on('dp.change', function (ev) {
            var date = moment($(ev.currentTarget).data().date);
            if (!isDeployment) {
                setEndMinDate(thisTBody, date);
            }
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

function setIndividualBounds(actionTBody) {
    var siteVisit = $('.form-table').children('tbody').first();
    var beginSVDate = moment($(siteVisit).find('[name="begindatetime"]').val());
    var endSVDate = moment($(siteVisit).find('[name="enddatetime"]').val());

    var beginDateTimeObj = actionTBody.find('[name="begindatetime"]').parents('.datetimepicker').data('DateTimePicker');
    var endDateTimeObj = actionTBody.find('[name="enddatetime"]').parents('.datetimepicker').data('DateTimePicker');

    var actionType = actionTBody.find('[name="actiontypecv"]').val();
    var isDeployment = $('form').hasClass('EquipmentDeployment') || actionType == 'Equipment deployment' || actionType == 'Instrument deployment';

    // This fixes problem of beginDateTime being after maxDate. Boundaries are reset and set again.
    beginDateTimeObj.maxDate(false);
    beginDateTimeObj.minDate(false);
    endDateTimeObj.maxDate(false);
    endDateTimeObj.minDate(false);

    beginDateTimeObj.maxDate(endSVDate);
    beginDateTimeObj.minDate(beginSVDate);

    if (!isDeployment) {
        endDateTimeObj.maxDate(endSVDate);
        endDateTimeObj.minDate(beginSVDate);
    }

    beginDateTimeObj.hide();
    endDateTimeObj.hide();

}

function  setLoginForm(loginForm) {
    loginForm.find('input').addClass('form-control');
}



$(document).ready(function () {
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

    var loginForm = $('#login_form');
    if (loginForm.length > 0) {
        setLoginForm(loginForm);
    }
});


