// Create a map object
var myMap = L.map("map", {
  center: [15.5994, -28.6731],
  zoom: 3
});

// Adding tile layer
L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/outdoors-v10/tiles/256/{z}/{x}/{y}?access_token=accessToken", {
    maxZoom: 18, 
    id: "mapbox.streets", 
    accessToken: API_KEY
  }).addTo(myMap);

// Country data
var countries = [
  {
    name: "Brazil",
    location: [-14.2350, -51.9253],
    points: 227
  },
  {
    name: "Germany",
    location: [51.1657, 10.4515],
    points: 218
  },
  {
    name: "Italy",
    location: [41.8719, 12.5675],
    points: 156
  },
  {
    name: "Argentina",
    location: [-38.4161, -63.6167],
    points: 140
  },
  {
    name: "Spain",
    location: [40.4637, -3.7492],
    points: 99
  },
  {
    name: "England",
    location: [52.355, 1.1743],
    points: 98
  },
  {
    name: "France",
    location: [46.2276, 2.2137],
    points: 96
  },
  {
    name: "Netherlands",
    location: [52.1326, 5.2913],
    points: 93
  },
  {
    name: "Uruguay",
    location: [-32.4228, -55.7658],
    points: 72
  },
  {
    name: "Sweden",
    location: [60.1282, 18.6435],
    points: 61
  }
];

function colorMarkers(dataset){
  
  dataset.map(country => {
    // clear the color each time so I can get the updates for the country 
    color = " ";

    // for each country pick a color 

    
    if (country.points > 200){
        color = "Yellow"
    } else if (country.points > 100){
          color = "red"
    }else {
       color = "brown"
    }
     
    L.circles(country.location, {
      color: color, 
      radius: dataset.points * 20.00
    }).addTo(myMap)
  }); 


}
// Loop through the countries array
// for each country if points < 200 color = red 
//     else if point > 200 color is blue 
  // Conditionals for countries points


  // Adjust radius
