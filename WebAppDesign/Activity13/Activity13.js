$(document).ready(function() {
    $.ajax({
        type: "get",
        url: "team.json",
        beforeSend: function() {
            $("#team").html("Loading...");
        },
        timeout: 10000,
        dataType: "json"
    })

    .done(function(data) {
        $("#team").html("");
        let members = data.teammembers
        
        for (let i = 0; i < members.length; i++) {
            $("#team").append
                ("<h3>" + members[i].name + "</h3>" +
                            members[i].title + "<br>" +
                            members[i].bio + "<br>");
        }

    })
    .fail(function(xr, stat, error){
        alert("Error" + xr.status + " " + error)
    });

});
