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
    var stateObj = {tab: tab};
    history.replaceState(stateObj, tab, '?tab=' + tab);
}

function initVocabulariesTabs($) {
    var currentTab = getUrlParameters('tab');
    if (currentTab) {
        $("[aria-controls=" + currentTab + "]").parent().addClass('active');
        $('#' + currentTab).addClass('active in');
    } else {
        $('#site').addClass("active in");
        $('#initial_tab').addClass('active');
    }
}

$(document).ready(function () {

});