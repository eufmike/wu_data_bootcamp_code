// Get a reference to the table body
var tbody = d3.select("tbody");

// Console.log the weather data from data.js
console.log(data);

// from data.js
var tableData = data;
/*
tableData.forEach(function(UFOReport) {
    var row = tbody.append("tr");
    Object.entries(UFOReport).forEach(([key, value]) => {
        var cell = tbody.append("td");
        cell.text(value);
    });
});
*/
console.log("test01");
// Select the submit button
var submit = d3.select("#filter-btn");
submit.on("click", function() {
    
    console.log("click start");

    // Prevent the page from refreshing
    d3.event.preventDefault();

    // Select the input element and get the raw HTML node
    var inputElement = d3.select("#datetime");

    // Get the value property of the input element
    var inputValue = inputElement.property("value");

    console.log(inputValue);
    console.log(tableData);
    
    var filteredData = tableData.filter(tableData => tableData.datetime === inputValue);
    
    console.log("filtered data start");
    filteredData.forEach(function(UFOReport) {
        var row = tbody.append("tr");
        Object.entries(UFOReport).forEach(([key, value]) => {
            var cell = tbody.append("td");
            cell.text(value);
        });
    });
    

});
