$(document).ready(function () {
    var dataTables = $('.data-table').dataTable({
        "iDisplayLength": 50,
        retrieve: true
    });

    if (sessionStorage && sessionStorage.getItem('tableClicked')) {
        var selectedTable = $('#' + sessionStorage.getItem('tableClicked'))
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
});



