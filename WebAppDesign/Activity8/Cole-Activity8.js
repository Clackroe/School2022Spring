let names = ["Tom", "Lily", "Jose", "Sarah"];
let heights = [65, 60, 72, 68];

let $ = function (selector) { return document.querySelector(selector); };

document.addEventListener("DOMContentLoaded", function () {
    $("#show_results").addEventListener("click", showResults);
    $("#add").addEventListener("click", addHeight);
    $("#display_height").addEventListener("click", displayHeight);
});

function showResults() {
let avgHeight = 0;
for (let i = 0; i < heights.length; i++) {
    avgHeight += parseFloat(heights[i]);
}
avgHeight /= heights.length;

let tallest = 0;
let tallestIndex = 0;
for (let i = 0; i < heights.length; i++) {
    if (heights[i] > tallest) {
        tallest = heights[i];
        tallestIndex = i;
    }

    $("#average").innerHTML = "Average Height: " + avgHeight.toFixed(2);
    $("#highest").innerHTML = "Tallest: " + names[tallestIndex] + " (" + tallest + "ft)";

    }   
}

function addHeight() {
    let name = document.getElementById("name").value;
    let height = document.getElementById("height").value;
    names.push(String(name));
    heights.push(String(height));


}

function displayHeight() {
    let table = $("#height_table");

    table.innerHTML = " ";
    
    for (let i = 0; i < heights.length; i++) {
        let row = table.insertRow(i);
        let nameCell = row.insertCell(0);
        let heightCell = row.insertCell(1);
        nameCell.innerHTML = names[i];
        heightCell.innerHTML = heights[i];
    }
  
}

