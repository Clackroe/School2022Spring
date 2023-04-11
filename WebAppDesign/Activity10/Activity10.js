$(document).ready(function() {


        // preload the image for each link
        var listItems = $("ul#image_list a");

        listItems.each(function () {
                var imageURL = $(this).attr("href");
                var imageCaption = $(this).attr("title");
                var image = new Image();
                image.src = imageURL;
                image.alt = imageCaption;
                

        

        // set up the event handlers for each link
        $(this).click(function (evt) {
		// get the image URL and caption for each image and animate the caption
                var imageURL = $(this).attr("href");
                var imageCaption = $(this).attr("title");

                $("#caption").fadeOut(3000);
                $("#image").fadeOut(3000, function() {
                        $("#image").attr("src", imageURL);
                        $("#caption").text(imageCaption);
                        $("#caption").fadeIn(3000);
                        $("#image").fadeIn(3000, function() {
                                $("#caption").animate({fontSize: "2em"}, 3000);
                        });
                });
                

                


            // cancel the default action of each link's child
                evt.preventDefault();

               
        });

}); // end each

    	


    // move the focus to the first link
        $("ul#image_list a:first img").focus();

}); // end ready