// YOUR CODE HERE
console.log(data);

var long_jump = {
   x: data.year,
   y: data.long_jump,
   type: "scatter",
   mode: "lines+markers",
   marker: { size: 12,
             symbol: "square",
             color: "purple",
             line: { width: 3,
                     color: "coral"}},
   line: { width: 6,
           color: "pink" }
};

var high_jump = {
   x: data.year,
   y: data.high_jump,
   type: "scatter",
   mode: "lines+markers",
   marker: { size: 12,
             symbol: "diamond",
             color: "pink",
             line: { width: 3,
                     color: "purple"}},
   line: { width: 6,
           color: "coral" }
};

var discus_throw = {
   x: data.year,
   y: data.discus_throw,
   type: "scatter",
   mode: "lines+markers",
   marker: { size: 12,
             symbol: "x",
             color: "coral",
             line: { width: 3,
                     color: "pink"}},
   line: { width: 6,
           color: "purple" }
};

var scatter = [long_jump, high_jump, discus_throw];

Plotly.newPlot("plot", scatter);