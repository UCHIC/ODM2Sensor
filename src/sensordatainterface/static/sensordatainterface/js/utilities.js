function removeCommas(table) {
    var lastColumn = table.rows[0].cells.length - 1;

    for (var i = 1; i < table.rows.length; i++) {
        data = table.rows[i].cells[lastColumn].innerHTML.trim();

        table.rows[i].cells[lastColumn].innerHTML = data.substr(0, data.length - 1);
        console.log(data);
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
    }
}

$(document).ready(function () {
    /*http://ethaizone.github.io/Bootstrap-Confirmation/*/
    $('#danger-button').confirmation({
        placement: 'bottom',
        title: 'Are you sure you want to delete?',
        popout: true,
        btnCancelClass: 'btn-default',
        onCancel: function (){
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
});

setNavActive();