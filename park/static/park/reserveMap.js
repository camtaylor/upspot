/*
 * Click the map to set a new location for the Street View camera.
 */

function initMap(lat, lng){
  var mapLocation = new google.maps.LatLng(lat, lng);
  streetViewMap(mapLocation, 'pano', function(result){
      placeMarker(result, mapLocation, false);
  });

  // Set up the map.
  var map = new google.maps.Map(document.getElementById('map'), {
    center: mapLocation,
    zoom: 20,
    mapTypeId: google.maps.MapTypeId.HYBRID,
    scrollwheel: false,
    streetViewControl: false
  });

  placeMarker(map, mapLocation, false);

}