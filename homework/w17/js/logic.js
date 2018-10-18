//Create initial map with id "map", defined in the index.html
var myMap = L.map("map", {
  center: [39.50, -98.35],
  zoom: 4
});

//Create a map and fill in the container
var lightmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.light",
  accessToken: API_KEY
});

// We use the addTo method to add objects to our map
lightmap.addTo(myMap); 

//create function for add earthquake bubbles
function createMarkers(earthquakes){
  var incidents = earthquakes.features.geometry;
  var bikeMarkers = [];
  for (var index = 0; index < incidents.length; index++) {
    var bikeMarker = L.marker([incidents.coordinates[0], incidents.coordinates[1]]);
    bikeMarkers.push(bikeMarker);
  };

};

//load data
var url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson';
d3.json(url, createMarkers);
