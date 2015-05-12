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
    }else if (currentPath.indexOf("control-vocabularies") > 0) {
        $("#vocabulary-nav").addClass("active");
    }
}

// Function by Sameer Kazi
function getUrlParameters(param) {
    var pageURL = window.location.search.substring(1);
    var URLVariables = pageURL.split('&');
    for (var i = 0; i < URLVariables.length; i++) {
        var parameterName = URLVariables[i].split('=');
        if (parameterName[0] == param) {
            return parameterName[1];
        }
    }
}

function setInitialTab($) {
    var currentTab = getUrlParameters('tab');
    if (currentTab) {
        $("[aria-controls=" + currentTab + "]").parent().addClass('active');
        $('#' + currentTab).addClass('active in');
    } else {
        $('#site').addClass("active in");
        $('#initial_tab').addClass('active');
    }
}

function initVocabulariesTabs($) {
    $('#site').find('a').click(function (e) {
        $(this).tab('show')
    });

    $('#equipment').click(function (e) {
        $(this).tab('show')
    });

    $('#activity').find('a').click(function (e) {
        $(this).tab('show')
    });

    $('#deployment').find('a').click(function (e) {
        $(this).tab('show')
    });

    $('#calibration').find('a').click(function (e) {
        $(this).tab('show')
    });

    $('#vendor').find('a').click(function (e) {
        $(this).tab('show')
    });

    setInitialTab($);
}

$(document).ready(function () {
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

    /* http://xdsoft.net/jqplugins/datetimepicker/ */
    $('#id_equipmentpurchasedate').datetimepicker({
        format: 'm/d/Y H:i'
    });

    $("[name='begindatetime']").datetimepicker({
        format: 'm/d/Y H:i'
    });

    $("[name='enddatetime']").datetimepicker({
        format: 'm/d/Y H:i'
    });

    $('input').addClass('form-control');
    $("[type='checkbox']").removeClass('form-control');
    $('select').addClass('select-two');
    $('textarea').addClass('form-control');
    $(".select-two").select2();

    initVocabulariesTabs($);
});

setNavActive();