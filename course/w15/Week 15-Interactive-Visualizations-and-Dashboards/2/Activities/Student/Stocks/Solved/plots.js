<<<<<<< HEAD
var apiKey = "ppvzoohSZsStRq8whQr9";
=======
var apiKey = "aqk9zPG2yAG4gM2zmRj9";
>>>>>>> 6c7c7b5c516adcdbd595a15bad389c135ef2dc58

/* global Plotly */
var url =
  `https://www.quandl.com/api/v3/datasets/WIKI/AMZN.json?start_date=2016-10-01&end_date=2017-10-01&api_key=${apiKey}`;

/**
 * Helper function to select stock data
 * Returns an array of values
 * @param {array} rows
 * @param {integer} index
 * index 0 - Date
 * index 1 - Open
 * index 2 - High
 * index 3 - Low
 * index 4 - Volume
 */
function unpack(rows, index) {
  return rows.map(function(row) {
<<<<<<< HEAD
    return row[index];
=======
       return row[index];
>>>>>>> 6c7c7b5c516adcdbd595a15bad389c135ef2dc58
  });
}

function buildPlot() {
  d3.json(url).then(function(data) {

    // Grab values from the data json object to build the plots
<<<<<<< HEAD
    var name = data.dataset.name;
=======
    console.log(data);
    var name = data.dataset.colum_names;
>>>>>>> 6c7c7b5c516adcdbd595a15bad389c135ef2dc58
    var stock = data.dataset.dataset_code;
    var startDate = data.dataset.start_date;
    var endDate = data.dataset.end_date;
    var dates = unpack(data.dataset.data, 0);
<<<<<<< HEAD
    var closingPrices = unpack(data.dataset.data, 1);
=======
    var closingPrices = unpack(data.dataset.data, 4);
>>>>>>> 6c7c7b5c516adcdbd595a15bad389c135ef2dc58

    var trace1 = {
      type: "scatter",
      mode: "lines",
      name: name,
      x: dates,
      y: closingPrices,
      line: {
        color: "#17BECF"
      }
    };

    var data = [trace1];

    var layout = {
      title: `${stock} closing prices`,
      xaxis: {
        range: [startDate, endDate],
        type: "date"
      },
      yaxis: {
        autorange: true,
        type: "linear"
      }
    };

    Plotly.newPlot("plot", data, layout);

  });
}

buildPlot();
