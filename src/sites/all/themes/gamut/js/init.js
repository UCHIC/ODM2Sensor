var activeMenu;
var map;

function fixTables($) {
    var widths = new Array();
    var i = 0;
    // This is a problem if there are 2 filters in the same page
    $('tbody tr:visible:first td').each(function () {
        widths[i] = $(this).width();
        i++;
    });

    i = 0;
    $('thead tr:visible th').each(function () {
        $(this).width(widths[i] + 1);
        i++;
    });
}


jQuery(document).ready(function ($) {

    /* Replace all drupal default filters for tables */
    {
        var filtersContainers = $(".view-filters");
        filtersContainers.each(function(){
            var container = $(this);
            var filterTextbox = $("<input type='text' class='filter-textbox'>");
            
            container.empty();
            container.append("<label class='filter-label'>Keyword</label>");
            container.append(filterTextbox);

            var table = container.siblings(".view-content").find("table");
            filterTextbox.table_filter({
                'table': table,
                'filter_inverse': false,
                'enable_space': false,
            });

        });
    }


    // Display sorting arrow at first td of table
    i = 0;
    $('thead tr:nth-child(1) th:nth-child(1)').each(function () {
        $(this).addClass('headerSortDown');
    });
    
    /* Make all tables sortable */
    $("table").tablesorter();

    /* Correct Deployments and Calibrations links in Site Visit Detail */
    if (Drupal.settings["activity-id"]) {
        $(".views-field-fieldactivitytype:contains('Deployment') a").attr("href", Drupal.settings["basePath"] + "deployment-details/" + Drupal.settings["activity-id"]);
        $(".views-field-fieldactivitytype:contains('Calibration') a").attr("href", Drupal.settings["basePath"] + "calibration-details/" + Drupal.settings["activity-id"]);
    }

    /* Hide Deployment measured variables */
    {
        var equipmentType = $(".views-field-equipmenttype .field-content").text();
        if (equipmentType !== "Sensor" && equipmentType !== "Datalogger") {
            $(".views-field-view-1").hide();
        }
    }
    
    /* Set previous and next visit onclick event */
    $("#previous-visit").click(function(){
        $.ajax({
            type: "GET",
            dataType: "json",
            url: Drupal.settings.basePath + "entities_service/previous-site-visit/" + Drupal.settings.site_visit_id,
            complete: function(data) {
                visitId = JSON.parse(data.responseText).value.SiteVisitID;
                if (visitId) {
                    window.location.href = Drupal.settings.basePath + "visit-details/" + visitId;
                }
                else {
                    alert("There is not a previous site visit.");
                }
            },
        });
    });

    $("#next-visit").click(function(){
        $.ajax({
            type: "GET",
            dataType: "json",
            url: Drupal.settings.basePath + "entities_service/next-site-visit/" + Drupal.settings.site_visit_id,
            complete: function(data) {
                visitId = JSON.parse(data.responseText).value.SiteVisitID;
                if (visitId) {
                    window.location.href = Drupal.settings.basePath + "visit-details/" + visitId;
                }
                else {
                    alert("There is not a next site visit.");
                }
            },
        });
    });

    // Set autofocus to the first input element of the form
    $('form:first *:input[type!=hidden]:first').focus();
    

    /* ### Sticky Headers BEGIN ### */

    /* Put tables inside a div for styling purposes, and because drupal's structuring sucks big time. */
    var tables = $("table");
    tables.each(function(){
        var parent = $(this).parent();
        var container = $("<div class='table-container'></div>");
        container.append($(this));
        parent.append(container);
    });


    /* ------------- Reposition the thead so it won't overlap -----------------*/
    i = 0;
    // Move the thead up. 
    var heights = Array();
    $('thead').each(function(){
        // save the heights
        heights[i] = $(this).height();
        i++;
        $(this).css('top', -$(this).height() + 1)
    })

    //Now move the whole table down same distance
    i = 0;
    $('.outer').each(function(){
        $(this).css('top', heights[i]);
        $(this).css('padding-bottom', heights[i]);
        i++;
    })

    /* ### Sticky Headers END ### */




    
    /*create tabs for the vocabularies page */
    $("#tabs").tabs();
    $("#tabs").removeClass("ui-widget").removeClass("ui-widget-content");
    $("#tabs .ui-tabs-nav a").focus(function() {$(this).blur()});
    $(".fht-tbody").removeAttr('style');
    
    /* Change color of all date rows containing the "Present" value */
    $(".views-field-begindate a:not(:contains('Present'))").parent().css("background-color", "#EDEDED").siblings().css("background-color", "#EDEDED");

    /* Bind click event to in-table entity operations */
    var entities = ['vendortype', 'sitegroup', 'sitetype', 'people', 'deploymenttypes', 'calibrationmethod', 'calibrationstandard', 'calibrationstandardtype', 'fieldactivitytype', 'equipmenttypes', 'deploymentmeasuredvariable'];

    for (index in entities) {
        if ($(".delete-" + entities[index]).length == 0) {
            continue;
        }

        var entity = entities[index];
        $(".delete-" + entity).click(function(data) {
            var resourceName = this.className.replace("delete-icon delete-", "");
            deleteEntity(resourceName, $(this).attr("itemid"), function(data) {
                response = JSON.parse(data.responseText);
                var messageDiv = $("<div class='messages' style='display:none'><span></span></div>");
                var message = "";
                if (response.value !== 0) {
                    $("span[itemid='"+response.id+"'].delete-icon").parent().parent().slideUp();
                    messageDiv.addClass("status");
                    message = "The item was successfully deleted.";
                }
                else {
                    messageDiv.addClass("error");
                    message = "The item could not be deleted. It is probably in use.";
                }

                messageDiv.append($("<span>" + message + "</span>"));
                $("div.messages").slideUp(200, function(){
                    $(this).remove();
                });
                $(".tabs:first").append(messageDiv);
                messageDiv.slideDown();
                $('body').scrollTop(0);
            });
        });
    }
    /* Put asterisk on every required field*/
    $(".required.form-select, input.required, .required input").after("<span title='This is a required field.' class='required-asterisk'> *</span>");
    $('textarea.required').parent().after("<span title='This is a required field.' class='required-asterisk'> *</span>");

    // Allows red asterik to appear inline in date fields
    $(".required input").removeClass('date-clear');

    /* Setup Mouse cursor animation when in ajax call */
    $("html").bind("ajaxStart", function(){
        $(this).addClass('busy');
    }).bind("ajaxStop", function() {
        $(this).removeClass('busy');
    });

    /* Setup chosen plugin */
    $("select").chosen();

    /* Setup behaviors to fix the dropdowns after ajax call */
    Drupal.behaviors.db_connect = {
        attach: function (context, settings) {
            if (context.attr("id") === "equipment-site_visits-div") {
                $('[id^=edit-field-site-visit-und', context).chosen();
                var chosenSelect = $('#edit_field_site_visit_und_chzn', context);
                $('#edit_field_site_visit_und_chzn').after("<span title='This is a required field.' class='required-asterisk'> *</span>");
            }
            if (context.attr("id") === "equipment-div") {
                $('[id^=edit-field-equipment-serial-number-und', context).chosen();
                var chosenSelect = $('#edit_field_equipment_serial_number_und_chzn', context);
                $('#edit_field_equipment_serial_number_und_chzn').after("<span title='This is a required field.' class='required-asterisk'> *</span>");
            }
            if (context.attr("id") === "measured-variable-div") {
                $('[id^=edit-field-measured-variable-und', context).chosen();
                var chosenSelect = $('#edit-field-measured-variable-und_chzn', context);
                $('#edit-field-measured-variable-und_chzn').after("<span title='This is a required field.' class='required-asterisk'> *</span>");
            }
        }
    };

    /* Build Sub-menus */
    $("#visits-menu").hover(function () {
        $("#floating-submenu").empty();

        $("#floating-submenu").append("<li id='deployments-menu'><a href='"+Drupal.settings.basePath+"deployments-view'>Deployments<span class='link_description'>View Deployments</span></a></li>");
        $("#floating-submenu").append("<li id='calibrations-menu'><a href='"+Drupal.settings.basePath+"calibrations-view'>Calibrations<span class='link_description'>View Calibrations</span></a></li>");
        $("#floating-submenu").append("<li id='activities-menu'><a href='"+Drupal.settings.basePath+"activities-view'>Other Activities <span class='link_description'>View Other Activities</span></a></li>");
        

        $("#floating-submenu").css("visibility", "visible");
        $("#floating-submenu").css("display", "block");
        activeMenu = $(this);
    });
    $("#equipment-menu").hover(function () {
        $("#floating-submenu").empty();

        $("#floating-submenu").append("<li id='factory-service-menu'><a href='"+Drupal.settings.basePath+"service-events-view'>Factory Service History<span class='link_description'>View Factory Service Events</span></a></li>");
        $("#floating-submenu").append("<li id='sensor-output-variable-menu'><a href='"+Drupal.settings.basePath+"view-sensor-output-variables'>Sensor Output Variables<span class='link_description'>View Sensor Output Variables</span></a></li>");
        $("#floating-submenu").append("<li id='equipment-models-menu'><a href='"+Drupal.settings.basePath+"view-equipment-models'>Equipment Models<span class='link_description'>View Equipment Models</span></a></li>");

        $("#floating-submenu").css("visibility", "visible");
        $("#floating-submenu").css("display", "block");
        activeMenu = $(this);
    });

    /* Bind dropdown menu events */
    $("#floating-submenu, .has-menu").mouseenter(function () {
        $("#floating-submenu").css("visibility", "visible");
        $("#floating-submenu").css("display", "block");
        activeMenu.addClass("hover");
    });
    $("#floating-submenu, .has-menu").mouseleave(function () {
        $("#floating-submenu").css("visibility", "invisible");
        $("#floating-submenu").css("display", "none");
        activeMenu.removeClass("hover");
    });

    /* Setup Google Map */
    if (Drupal.settings["site_name"] && Drupal.settings["map_latitude"] && Drupal.settings["map_longitude"]){
        map_latitude = Drupal.settings["map_latitude"];
        map_longitude = Drupal.settings["map_longitude"];
        site_name = Drupal.settings["site_name"];
        page = Drupal.settings["page"];
        

        centerPoint = new google.maps.LatLng(map_latitude, map_longitude);
        var mapOptions = {
            zoom: 12,
            panControl: false,
            center: centerPoint,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        };
        map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
        var marker = new google.maps.Marker({
            position: centerPoint,
            map: map,
            title: site_name,
            animation: google.maps.Animation.DROP
        });

        if (page == "site") {
            var overlayContent;
            var openOverlay = false;
            var siteImage = Drupal.settings["site_image"];

            if (siteImage != "") {
                overlayContent = "<div id='overlayContent'>" +
                "<h4>" + site_name + " Photo</h4>" +
                "<a href=" + siteImage + " rel='lightbox'><img src=" + siteImage + " alt='" + site_name + "' class='thumbnail'></a>" +
                "</div>";
                openOverlay = true;
            }
            else {
                overlayContent = "<p>This site has no images.</p>";
            }

            MapContentHandler = (typeof InfoBox === 'undefined')? google.maps.InfoWindow: InfoBox;
            var infowindow = new MapContentHandler({
                content: overlayContent,
                pane: "floatPane",
                infoBoxClearance: new google.maps.Size(25, 25),
                pixelOffset: new google.maps.Size(-85, 17),
                boxClass: "infoBox siteBox",
            });

            google.maps.event.addListener(infowindow, "domready", function() {
                Lightbox.initList();
            });
            google.maps.event.addListener(marker, "click", function(event) {
                infowindow.open(map, marker);
            });

            if (openOverlay) {setTimeout(function() { infowindow.open(map, marker);  }, 0)};
        }

        else if (page == "site-visit") {
            var visitId = Drupal.settings["site_visit_id"];
            var imagesDirectory = Drupal.settings["images_directory"];

            jQuery.ajax({
                type: 'get',
                dataType: "json",
                url: Drupal.settings.basePath + "entities_service/site-visit-image/" + visitId,
                success: function(data) {
                    var overlayContent;
                    var openOverlay = false;
                    var images = data.value;

                    if (images.length > 0) {
                        overlayContent = "<div id='overlayContent'> <h4>" + site_name + " Images</h4>";
                        for (var index = 0; index < images.length; index++) {
                            image = images[index];
                            overlayContent += "<a href='../" + imagesDirectory + "/" + image.PhotoFilePath + "' rel='lightbox[\"visit-images\"]'>" +
                                "<img src='../" + imagesDirectory + "/" + image.PhotoFilePath + "' class='thumbnail'>" +
                            "</a>";
                        }
                        overlayContent += "</div>";
                        openOverlay = true;
                    }

                    else {
                        overlayContent = "<p>This site visit has no images.</p>";
                    }

                    MapContentHandler = (typeof InfoBox === 'undefined')? google.maps.InfoWindow: InfoBox;
                    var infowindow = new MapContentHandler({
                        content: overlayContent,
                        pane: "floatPane",
                        infoBoxClearance: new google.maps.Size(25, 25),
                        pixelOffset: new google.maps.Size(-171, 17),

                    });
                
                    google.maps.event.addListener(infowindow, "domready", function() {
                        Lightbox.initList();
                    });
                    google.maps.event.addListener(marker, "click", function(event) {
                        infowindow.open(map, marker);
                    });
                    if (openOverlay) {setTimeout(function() { infowindow.open(map, marker);  }, 0)};
                }
            });
        }
    }
});