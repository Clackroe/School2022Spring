$(function() {

    updateInfo();
   

    $("#tabs").accordion({collapsible: true, heightStyle: "content", });
    
});


function updateInfo() {

    let forPurchaseList = [];
    let noPurchaseList = [];

    let apikey = "61e36e0d5f952a16fe1701492d2a2a74";
    let uid = "52664347@N06";
    let url = "https://www.flickr.com/services/rest/?method=";
    let method = "flickr.people.getPublicPhotos";

    let forPurchUrl = url +  method + "&api_key=" + apikey + "&user_id=" + uid + "&format=json&nojsoncallback=1";

    uid = "98504010@N08";
    let noPurchUrl = url +  method + "&api_key=" + apikey + "&user_id=" + uid + "&format=json&nojsoncallback=1";

    $.when(
        $.get(forPurchUrl, function(data) {


            let photos = data.photos.photo;

            for(let i = 0; i < photos.length; i++) {

                let element = "";
                let img = photos[i];


                let imgUrl = "https://live.staticflickr.com/" + img.server + "/" + img.id + "_" + 
                img.secret +".jpg"

                element += '<li id="item">' +
                '<h3>'+ img.title +'</h3>' +
                '<p class="price">$' + Math.floor(Math.random() * 20) + '.99</p>' +
                '<img src="'+ imgUrl +'" alt="'+ img.title +'_alt">' + 
                '<input type="button" value="Buy Now" class="btn_buy">'

                forPurchaseList.push(element);

            }

            
        }),
        
        $.get(noPurchUrl, function(data) {

            
            let photos = data.photos.photo;

            for(let i = 0; i < photos.length; i++) {

                let element = "";
                let img = photos[i];


                let imgUrl = "https://live.staticflickr.com/" + img.server + "/" + img.id + "_" + 
                img.secret +".jpg"

                element += '<li id="item">' +
                '<h3>'+ img.title +'</h3>' +
                '<img src="'+ imgUrl +'" alt="'+ img.title +'_alt">' + 
                '<input type="button" value="Not Available" class="btn_buy" disabled>'

                noPurchaseList.push(element);

            }



        })
    ).then(function() {
        displayInfo(forPurchaseList, noPurchaseList);
    });

    
    


}

function displayInfo(forPurchaseList, noPurchaseList) {


    let allHTML = "";

    let html = "";

    for (let i = 0; i < forPurchaseList.length; i++) {
        html += forPurchaseList[i];
        console.log(forPurchaseList[i]);
        allHTML += forPurchaseList[i];
    }
    console.log(html);
    $("#forPurchase").html(html);

    html = "";
    for (let i = 0; i < noPurchaseList.length; i++) {
        html += noPurchaseList[i];
        allHTML += noPurchaseList[i];

    }
   
    console.log(html);
    $("#noPurchase").html(html);

    $("#allPurchase").html(allHTML);


}