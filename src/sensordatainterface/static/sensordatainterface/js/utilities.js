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
    //$('[data-toggle="confirmation"]').confirmation({
    //    placement: 'bottom',
    //    title: 'Are you sure you want to delete?',
    //    popout: true
    //})
    $('input').addClass('form-control');
    $('select').addClass('form-control');
});

setNavActive();