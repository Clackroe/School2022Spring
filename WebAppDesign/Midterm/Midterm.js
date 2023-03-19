var days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
var duration = [5,6,7,8,4,5,5];

var username = "";




var $ = function(id) { return document.querySelector("#"+id); };



document.addEventListener("DOMContentLoaded", function() {
    //event handlers
    $("update").addEventListener("click", updateSleep);
    $("track").addEventListener("mouseover", displaySleepDuration);
    $("enter_details").addEventListener("click", setDetails);
    $("average_bttn").addEventListener("click", showAverageMinMaxSleep);
    
});

function showAverageMinMaxSleep() {


    var sum = 0;
    for (var i = 0; i < duration.length; i++) {
        sum += parseInt(duration[i]);
    }
    var avg = sum / duration.length;
    var min = Math.min(...duration);
    var max = Math.max(...duration);

    var avgSleep = $("average_box");
    avgSleep.value = "Average: " + avg + "hrs, Min: " + min + "hrs, Max: " + max + "hrs";
    avgSleep.style.color = "green";
    avgSleep.style.borderColor = "red";



    


}


function setDetails() {
    username = $("name").value;
   
    
}


function updateSleep() {
    if (!$("sleep_duration").value == "") {
        var day = document.querySelector('input[name="day"]:checked').value;
        var sleep = $("sleep_duration").value;
        var index = days.indexOf(day);
        duration[index] = sleep;
        alert("Your updated sleep duration is " + sleep + " hrs on " + day + " day");
        $("sleep_duration").value = "";
    }
    else {
        alert("Please enter a valid sleep duration");
    }
}

function displaySleepDuration(){

    if (username == "") {
        alert("Please enter your name");
        return;
    }

    var paragraph = $("sleep_paragraph");

    paragraph.innerHTML = "Hey " + username + ", you slept less than 6hrs on the following days:"; 


    var table = document.getElementById("sleep_table");
    table.innerHTML = "";

    var listDays = [];
    var listDur = [];
    

    for (var i = 0; i < duration.length; i++) {
        if (duration[i] < 6) {
            listDays.push(days[i]);
            listDur.push(duration[i]);
        }
    }   
    
    var header = table.createTHead();
    var row = header.insertRow(0);
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    cell1.innerHTML = "<b>Day</b>";
    cell2.innerHTML = "<b>Hours</b>";

    for (var i = 0; i < listDays.length; i++) {
        var row = table.insertRow(i+1);
        var day = row.insertCell(0);
        var dur = row.insertCell(1);
        day.innerHTML = listDays[i];
        dur.innerHTML = listDur[i];
    }

    

}
