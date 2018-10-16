var mapper = L.map("map", {
    center: [45.52, -122.67],
    zoom: 13
}); 

L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  maxZoom: 18, 
  id: "mapbox.streets", 
  accessToken: API_KEY
}).addTo(mapper);