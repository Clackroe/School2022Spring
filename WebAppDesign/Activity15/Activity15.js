$(document).ready(function(){


    let data = $.getJSON("facultyList.json", function(data){

        let facultyData = data.facultymembers;

        let mainHtml = "";
        for (let i = 0; i < facultyData.length; i++){

            let member = facultyData[i];

            let html = "";
            html += "<img src='" + member.image + "' alt='" + member.first_name + "_picture' />";
            html += "<h2> " + member.full_name + "</h2>";
            html += "<h3>  " + member.department + "</h3>";
            html += "<p> " + member.bio + "</p>";

            mainHtml += html;
        }

        $("main").html(mainHtml);
    });


});
