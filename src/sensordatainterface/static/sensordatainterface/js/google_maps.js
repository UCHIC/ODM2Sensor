function initialize(lat, long) {
    var mapOptions = {
        center: new google.maps.LatLng(lat, long),
        zoom: 15,
        mapTypeId: google.maps.MapTypeId.TERRAIN,
        zoomControl: true,
        zoomControlOptions: {
            style: google.maps.ZoomControlStyle.SMALL
        },
        streetViewControl: false
    };
    var map = new google.maps.Map(document.getElementById("map-canvas"),
        mapOptions);

    var marker = new google.maps.Marker({
        position: map.getCenter(),
        map: map,
        title: 'Click to zoom',
        animation: google.maps.Animation.DROP
    });

    google.maps.event.addListener(marker, 'click', function () {
        map.setZoom(8);
        map.setCenter(marker.getPosition());
    });

    setCountyState(lat, long);
};

function setCountyState(lat, long) {
    var stateTD = document.getElementById('site-state');
    var countyTD = document.getElementById('site-county');
    var geocoder = new google.maps.Geocoder();
    if (countyTD && stateTD) {
        var latLng = new google.maps.LatLng(lat, long);
        geocoder.geocode({'latLng': latLng}, function (results, status) {
            if (status == google.maps.GeocoderStatus.OK) {
                var addressComponents = results[0].address_components;
                for (var i = 0; i < addressComponents.length; i++) {
                    if (addressComponents[i].types[0] == 'administrative_area_level_1') {
                        stateTD.innerHTML = addressComponents[i].long_name;
                    } else if (addressComponents[i].types[0] == 'administrative_area_level_2') {
                        countyTD.innerHTML = addressComponents[i].long_name;
                    }
                }
            } else {
                console.log("Geocode error: " + status);
            }
        })
    }
};

