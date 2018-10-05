var apiKey = "aqk9zPG2yAG4gM2zmRj9";

/* global Plotly */
var url =
  `https://www.quandl.com/api/v3/datasets/WIKI/AMZN.json?start_date=2016-10-01&end_date=2017-10-01&api_key=${apiKey}`;

/**
 * Helper function to select stock data
 * Returns an array of values
 * @param {array} data
 * @param {integer} index
 * index 0 - Date
 * index 1 - Open
 * index 2 - High
 * index 3 - Low
 * index 4 - Volume
 */
function unpack(rows, index) {
  return rows.map(function(row) {
    return row[index];
  });
}

/**
 * Fetch data and build the timeseries plot
 */
function buildPlot() {

  d3.json(url).then(function(data){
     console.log(data);
    //  select stuff 
    var name = data.dataset.column_names;
    var stock = data.dataset.dataset_code;
    var endData = data.dataset.end_date;
    var startDate = data.dataset.start_date;
    var dates = unpack(data.dataset.data, 0);
    var closingPrice = unpack(data.dataset.data, 4);
  }); 
 trace = {
   x: dates, 
   y: closingPrice, 
   type: "scatter"
 };
 data = [trace]; 

 Plotly.newplot("plot", data);
}

buildPlot();
