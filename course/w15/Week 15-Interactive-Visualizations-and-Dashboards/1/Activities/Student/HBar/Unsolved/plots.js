// @TODO: Complete the following sections

console.log("data", data[0].greekSearchResults);
// Sort the data array using the greekSearchResults value
data.sort(function(a, b){
    return parseFloat(b.greekSearchResults) - parseFloat(a.greekSearchResults);
});
// Slice the first 10 objects for plotting
data = data.slice(0, 10);
console.log(data);
// Trace1 for the Greek Data
var trace1 = {
    
};
// set up the data variable
data = [trace1];
// set up the layout variable
// var layout = {};
// Render the plot to the div tag with id "plot"
Plotly.newPlot("plot", data);