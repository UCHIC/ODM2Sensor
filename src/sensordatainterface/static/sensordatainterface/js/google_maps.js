function initialize(lat, long) {
    var mapOptions = {
        center: new google.maps.LatLng(lat, long),
        zoom: 16,
        mapTypeId: google.maps.MapTypeId.SATELLITE,
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
};