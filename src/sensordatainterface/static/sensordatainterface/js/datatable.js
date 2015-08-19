$(document).ready(function () {
    var dataTables = $('.data-table').DataTable({
        "iDisplayLength": 50,
        retrieve: true
    });

    if (dataTables.context.length && dataTables.column(0).header().textContent == "Date") {
        dataTables.order([0, 'desc']).draw();
    }

    var side_item_tables = $('.side-by-side-item .data-table');
    var vocabularies_page = $('[role="tabpanel"]');

    if (side_item_tables.length > 0 || vocabularies_page.length > 0)
        dataTables.page.len(10).draw();

    var measuredVarsButton = $('.add-inst-meas-variables-button');
    var relatedEquButton = $('.add-related-equ-button');

    if (measuredVarsButton && relatedEquButton) {
        //measuredVarsButton.click(function () {
        //    $(this).parents('.side-by-side-item').find('.side-dependent-table').toggle("slow");
        //    var text = $(this).text();
        //    $(this).text(
        //        text == "Show Measured Variables"? "Hide Measured Variables" : "Show Measured Variables"
        //    );
        //
        //});
        //relatedEquButton.click(function () {
        //    $(this).parents('.side-by-side-item').find('.related-equipment-table').toggle("slow");
        //    var text = $(this).text();
        //    $(this).text(
        //        text == "Show Related Equipment"? "Hide Related Equipment" : "Show Related Equipment"
        //    );
        //});
    }
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



