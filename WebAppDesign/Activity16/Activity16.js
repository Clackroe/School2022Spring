$(document).ready(function(){


    let key = "61e36e0d5f952a16fe1701492d2a2a74";

    let userID = "82407828@N07";


    let url = "https://www.flickr.com/services/rest/?method="

    let method = "flickr.people.getPublicPhotos"

    url += method + "&api_key=" + key + "&user_id=" + userID + "&format=json&nojsoncallback=1&tags=vectacorpbuilding";

    let mainHtml = "";

    let data = $.get(url, function(data){
    
        let photos = data.photos.photo;

        for(let i = 0; i < photos.length; i++){

            let html = "";
            let img = photos[i];

            let url = "https://live.staticflickr.com/" + img.server + "/" + img.id + "_" + 
            img.secret +".jpg"

            html += "<a href='" + url + "' data-title='" + img.title + "' data-lightbox='building'> " + "<img src=" + url + "/></a>";

            mainHtml += html;
        }

        $("#new_building").html(mainHtml);

    });

});