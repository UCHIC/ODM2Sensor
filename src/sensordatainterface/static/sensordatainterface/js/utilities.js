function removeCommas(table) {
    var lastColumn = table.rows[0].cells.length - 1;

    for (var i = 1; i < table.rows.length; i++) {
        data = table.rows[i].cells[lastColumn].innerHTML.trim();

        table.rows[i].cells[lastColumn].innerHTML = data.substr(0, data.length - 1);
        console.log(data);
    }
}

window.addEventListener('load', function() {
    var table = document.getElementById('data-table');

    if (table) {
        removeCommas(table);
    }
});