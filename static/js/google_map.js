function init() {
    var myLatLng = {lat: 12.9083032, lng: 77.5644103};
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 16,
          center: myLatLng
        });
        var marker = new google.maps.Marker({
          position: myLatLng,
          map: map,
          title: 'Hackathon at DSCE!'
        });
}
google.maps.event.addDomListener(window, 'load', init);