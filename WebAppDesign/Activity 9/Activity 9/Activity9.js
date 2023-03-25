$(document).ready(function () {



    // get the <a> elements in the unordered list
    // var listItems = $("ul#image_list a");
    var listItems = $("ul#image_list button");

    // use the each() method to get the URL and id for each image
    listItems.each(function () {
        var imageURL = $(this).attr("href");
        var imageCaption = $(this).attr("id");
        var image = new Image();
        image.src = imageURL;
        image.alt = imageCaption;

        // get the image URL and id for each image


        // preload the image for each link

        // set up the event handlers for each link
        $(this).click(function (evt) {
            // load the image and caption
            $("#image").attr("src", imageURL);
            $("#title").text(imageCaption);
            // cancel the default action of the link
            evt.preventDefault();
        }); // end click

    });
   
    // $("ul#image_list a:last").focus();
    // $("ul#image_list a:last").click();
    $("ul#image_list button:last").focus();
    $("ul#image_list button:last").click();


}); // end ready


