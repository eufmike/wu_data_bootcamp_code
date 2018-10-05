function init() {
  var data = [{
    values: [19, 26, 55, 88],
    labels: ["Spotify", "Soundcloud", "Pandora", "Itunes"],
    type: "pie"
  }];

  var layout = {
    height: 600,
    width: 800
  };

  Plotly.plot("pie", data, layout);
}

function updatePlotly(newdata) {
  // YOUR CODE HERE
  // Use `Plotly.restyle` to update the pie chart with the newdata array
    var plotMe = document.getElementById("pie"); 
    Plotly.restyle(plotMe, "values", [newdata]);
}

function getData(dataset) {
  // YOUR CODE HERE
  // create a select statement to select different data arrays (YOUR CHOICE)
  // whenever the dataset parameter changes. This function will get called
  // from the dropdown event handler.
  console.log("dataset", dataset);
  var data = [];

  switch (dataset) {
    case "itunes":
      data = [10, 20, 39, 1];
      break;
    case "spotify":
      data = [1, 2, 50, 20];
      break;
    case "pandora":
      data = [100, 200, 39, 11];
      break;
    case "soundcloud":
      data = [ 20, 39, 15, 20]; 
      break;
    }
  updatePlotly(data);
}

init();
