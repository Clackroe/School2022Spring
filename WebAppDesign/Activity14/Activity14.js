$(document).ready(function() {
	

    /* In the Activity14.js file, add code for this application. Within the click
event handlers for the <a> elements in the sidebar, use the title attribute
for each link to build the name of the JSON file that needs to be retrieved.
Then, use that file name to get the data for the speaker, enclose that data in
HTML elements that are just like the ones that are used in the starting
HTML for the first speaker, and put those elements in the main element in
the HTML. That way, the CSS will work the same for the Ajax data as it
did for the starting HTML.

*/

    $("#nav_list ul li a").click(function(e) {

        e.preventDefault();

        
        title= this.title;

        var url = this.title + ".json";

        $.getJSON("json_files/" + url, function(data) {

           let speakerData = data.speakers[0];

            var html = "";
            html += "<h1>" + speakerData.title + "</h1>";
            html += "<h2>" + speakerData.month + "</h2>";
            html += "<h3>" + speakerData.speaker + "</h3>";
            html += "<img src='" + speakerData.image + "' alt='" + title + "_picture' />";
            html += "<p>" + speakerData.text + "</p>";
            $("main").html(html);
        }); // end getJSON

    });







}); // end ready