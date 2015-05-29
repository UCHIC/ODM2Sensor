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

function changeTab(tab) {
    var href = window.location.href;
    var getStart = href.indexOf('?');
    if (getStart !== -1) {
        href = href.substr(0, getStart);
    }
    //window.location.href = href + '?tab='+tab; causes reload :(
    var stateObj = { tab: tab };
    history.replaceState(stateObj, tab, '?tab='+tab);
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


    set_delete_icon();

    $('.dataTables_paginate').click(function(){
       set_delete_icon();
    });

    $('.dataTables_filter').find('input[type="search"]').change(function() {
       set_delete_icon();
    });

    function set_delete_icon() {
        $('.delete-icon').confirmation({
            placement: 'left',
            title: 'Are you sure?',
            btnCancelClass: 'btn-default',
            onCancel: function () {
                $('.delete-icon').confirmation('hide');
            },
            onConfirm: function() {
                var tableClicked = $(this).parents('.dataTables_wrapper').attr('id');
                var table = $('#'+tableClicked);
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




    /* http://tarruda.github.io/bootstrap-datetimepicker/ */
    var dateElements = [];
    dateElements.push($('#id_equipmentpurchasedate'));
    dateElements.push($("[name='begindatetime']"));
    dateElements.push($("[name='enddatetime']"));
    dateElements.push($("[name='referencematerialpurchasedate']"));
    dateElements.push($("[name='referencematerialexpirationdate']"));

    dateElements.forEach(function(element) {
        element.wrap("<div class='datetimepicker input-append date'></div");
        element.removeClass('form-control');
        element.after(
            $("<span class='add-on'><i data-time-icon='glyphicon glyphicon-time' data-date-icon='glyphicon glyphicon-calendar'></i></span>")
        );

    });

    //format: 'm/d/Y H:i'
    $('.datetimepicker').datetimepicker({
        format: 'MM/dd/yyyy hh:mm:ss'
    });

    var button = $(".timepicker-picker a");
    button.addClass('btn-default');
    button.find('.icon-chevron-up').addClass('glyphicon glyphicon-chevron-up');
    button.find('.icon-chevron-down').addClass('glyphicon glyphicon-chevron-down');

    $('input').addClass('form-control');
    $("[type='checkbox']").removeClass('form-control');
    $('select').addClass('select-two');
    $('textarea').addClass('form-control');
    $(".select-two").select2();

    initVocabulariesTabs($);


});

setNavActive();

