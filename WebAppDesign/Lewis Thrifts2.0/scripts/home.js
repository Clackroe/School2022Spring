



$(function() { 

    updateWeather();



    $('.recent_uploads').slick({
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 2000,
        dots: true,
        infinite: true,
        speed: 500,
        fade: true,
        cssEase: 'linear'
    });



    function updateWeather() {

        console.log("Update Weather");

       let temperature = 0;

        let apiKey = "d1344aade632445f8aa195718230905"

        let url = "https://api.weatherapi.com/v1/current.json?key=" + apiKey + "&";

        let location = "q=Charlotte";

        url += location + "&aqi=no";

        $.get(url, function(data) {

            temperature = data.current.temp_f;
            // console.log(temperature);

            html = "<h2>" + temperature + "°F</h2>";

            if (parseInt(temperature) >= 67){
                html += "<p>It's a great day to take a walk and go thrifting!</p>";
            }
            else if (parseInt(temperature) < 67 && parseInt(temperature) >= 50){
                html += "<p>It's a little chilly, but it's still a great day to go thrifting!</p>";
            }
            else if (parseInt(temperature) < 50 && parseInt(temperature) >= 32){
                html += "<p>It's a little cold, maybe stay inside and chill with your family!</p>";
            }

            $("#weather").html(html);


        });      



    }

 })
