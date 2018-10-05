// show me the data 
console.log(data);

var trace1 = {
    x: data.map(row => row.pair),
    y: data.map(row => row.greekSearchResults),
    type: "bar"
};

var data = [trace1];

var layout = {
    title: "Greek vs Roman"
}; 

Plotly.newPlot("plot", data, layout); 