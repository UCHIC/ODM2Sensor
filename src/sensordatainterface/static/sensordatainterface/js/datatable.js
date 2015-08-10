$(document).ready(function () {
    var dataTables = $('.data-table').DataTable({
        "iDisplayLength": 50,
        retrieve: true
    });

    if (dataTables.context.length && dataTables.column(0).header().textContent == "Date") {
        dataTables.order([0, 'desc']).draw();
    }

    if ($('.data-table').parents('.side-by-side-item')) {
        $('.data-table').parents('.side-dependent-table').hide();
    } /* After this add button in html template, and move related equipment inside 'side dependent table. 
         After that add functionality to show and hide the side dependent table. 
         A hide/show toggle could work nicely'*/

    preserveTableStatus();
});

// This function makes sure that when a change is made in a table (i. e. delete) the table
// is redisplayed where it left off.
function preserveTableStatus() {
     if (sessionStorage && sessionStorage.getItem('tableClicked')) {
        var selectedTable = $('#' + sessionStorage.getItem('tableClicked'));
        var tableNode = selectedTable.find('.dataTable').dataTable();

        if (sessionStorage.getItem('searchTerm')) {
            var searchTerm = sessionStorage.getItem('searchTerm');
            selectedTable.find('input[type="search"]').val(searchTerm).keyup();
            sessionStorage.removeItem('searchTerm');
        }

        if (sessionStorage.getItem('tablePage')) {
            tableNode.fnPageChange(parseInt(sessionStorage.getItem('tablePage')) - 1);
            sessionStorage.removeItem('tablePage');
        }
        sessionStorage.removeItem('tableClicked');
    }
}



