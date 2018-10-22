//==================================================================
bubble_factor = 10000;

//Create function for color selection
function getColor(d){
  return d > 5 ? '#bd0026' :
        d > 4  ? '#f03b20' :
        d > 3  ? '#fd8d3c' :
        d > 2  ? '#feb24c' :
        d > 1  ? '#fed976' :
                  '#ffffb2';
};

//Create function for add earthquake bubbles
var earthquakes = new L.LayerGroup();

//load data
var url_earthquakes = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson';
//var url_earthquakes = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson';
d3.json(url_earthquakes, function(data){
  L.geoJSON(data, {
    pointToLayer: function(feature, latlng) {

      //Create marker options
      var geojsonCircleOptions = {
        radius: feature.properties.mag*bubble_factor,
        fillColor: getColor(feature.properties.mag),
        color: "#000",
        weight: 0.5,
        opacity: 1,
        fillOpacity: 0.8
      }   
      return L.circle(latlng, geojsonCircleOptions);
    }, 

    onEachFeature: function (feature, layer) {
      layer.bindPopup(
          "<h4 style='text-align:center;'>" + new Date(feature.properties.time) +
          "</h4> <hr> <h5 style='text-align:center;'>" + feature.properties.title + "</h5>");
    }
    
  }).addTo(earthquakes);
});

console.log(earthquakes)

//==================================================================

//Create plate boundary
var url_plates = "https://raw.githubusercontent.com/fraxen/tectonicplates/master/GeoJSON/PB2002_boundaries.json";

var plateBoundary = new L.LayerGroup();

d3.json(url_plates, function (data) {
    L.geoJSON(data.features, {
        style: function (geoJsonFeature) {
            return {
                weight: 2,
                color: '#ce2204'
            }
        },
    }).addTo(plateBoundary);
})


//==================================================================
function createMap() {
  //Create a map and fill in the container
  var satellitemap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.satellite",
    accessToken: API_KEY
  });

  var lightmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.light",
    accessToken: API_KEY
  });

  var darkmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.dark",
    accessToken: API_KEY
  });

  // Define a baseMaps object to hold our base layers
  var baseMaps = {
    "Satellite Map": satellitemap,
    "Light Map": lightmap,
    "Dark Map": darkmap,
  };

  // Create overlay object to hold our overlay layer
  var overlayMaps = {
    Earthquakes: earthquakes,
    Boundaries: plateBoundary
  };

  // Create our map, giving it the streetmap and earthquakes layers to display on load
  var myMap = L.map("map", {
    center: [39.50, -98.35],
    zoom: 4,
    layers: [satellitemap, plateBoundary, earthquakes]
  });

  //Use the addTo method to add objects to our map
  L.control.layers(baseMaps, overlayMaps).addTo(myMap);


  //==================================================================
  // Create legend
  var legend = L.control({position: 'bottomright'});

  legend.onAdd = function (myMap) {

      var div = L.DomUtil.create('div', 'info legend'),
      grades = [0, 1, 2, 3, 4, 5],
      labels = [];

      // loop through our density intervals and generate a label with a colored square for each interval
      for (var i = 0; i < grades.length; i++) {
          div.innerHTML +=
              '<i style="background:' + getColor(grades[i] + 1) + '"></i> ' +
              grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
      }

      return div;
  };

  legend.addTo(myMap);

};

createMap();