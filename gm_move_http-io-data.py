<!DOCTYPE html>
<!-- moving marker with js & Google Map API -->
<!-- GPS data -(Lat, Lon is provided through a local http server
    (realized using Python http.server: http_server.py, server_io.py)
    js Ajax send http request and get the data, then move
    marker to the place -->
<html>
  <head>
    <title>Simple Click Events</title>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta charset="utf-8">
    <style>
      /* Always set the map height explicitly to define the size of the div
       * element that contains the map. */
      #map {
        height: 70%;
      }
      /* Optional: Makes the sample page fill the window. */
      html, body {
        height: 100%;
        margin: 0;
        padding: 0;
      }
    </style>
  </head>
  <body>
    <div id="map"></div>
    <script>
      // global variables in <script> range
      var x0=-25.363;
      var y0=131.044;
      var step=9;
      var delay=300;
      var i=1;
      var marker;
      var map;
      function initMap() {
        var myLatlng = {lat: x0, lng: y0};
        var myLatlng2 = {lat: -26.363, lng: 132.044};
        map = new google.maps.Map(document.getElementById('map'), {
          zoom: 4,
          center: myLatlng
        });

        marker = new google.maps.Marker({
          position: myLatlng,
          map: map,
          title: 'Click to zoom'
        });

        setTimeout(function() {get_data();}, 3000);

        marker.addListener('click', function() {
          i=1;
          //move(marker);
        });
      }

      function move() {
        var xd=x0+i;
        marker.setPosition( new google.maps.LatLng( xd, y0 ) );
        var e=document.getElementById("index")
        e.innerHTML="i="+xd;
        var e1=document.getElementById("index1")

        if (i!=step) {
            e1.innerHTML="inner="+i+"delay="+delay;
            console.log(i);
            i++;
            // Attention to the syntax of setTimeout (a windows method)
            setTimeout(function() {move();}, delay);
            }
      }

      function get_data() {
        document.getElementById("hresponse").innerHTML="start connection ... ...";
        var xhttp=new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            document.getElementById("hresponse").innerHTML="receiving ... ..."+this.readyState+" status="+this.status;
            if (this.readyState == 4 && this.status == 200) {
                var values=(this.responseText).split(",");
                var xt=parseFloat(values[0]);
                var yt=parseFloat(values[1]);
                document.getElementById("hresponse").innerHTML = xt+","+yt;
                marker.setPosition( new google.maps.LatLng( xt, yt ) );

            }
        };
        //ajax_info.txt is a txt file in the same folder as this html file
        xhttp.open("GET","http://localhost:8000", true);
        //xhttp.open("GET","https://www.google.com", true);
        xhttp.send();
      }
      function http_move() {
        get_data();
        setTimeout(function() {http_move();}, 300);

      }


    </script>
    <script async defer
        src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAiqVRCkhlHbUCuSlJ7kGNUfUo90mIxa0U&callback=initMap">
    </script>
    <script>
        var autoDriveSteps = new Array();
        var speedFactor = 10; // 10x faster animated drive

        function setAnimatedRoute(origin, destination, map) {
            // init routing services
            var directionsService = new google.maps.DirectionsService;
            var directionsRenderer = new google.maps.DirectionsRenderer({
                map: map
            });

            //calculate route
            directionsService.route({
                    origin: origin,
                    destination: destination,
                    travelMode: google.maps.TravelMode.DRIVING
                },
                function(response, status) {
                    if (status == google.maps.DirectionsStatus.OK) {
                        // display the route
                        directionsRenderer.setDirections(response);

                        // calculate positions for the animation steps
                        // the result is an array of LatLng, stored in autoDriveSteps
                        autoDriveSteps = new Array();
                        var remainingSeconds = 0;
                        var leg = response.routes[0].legs[0]; // supporting single route, single legs currently
                        leg.steps.forEach(function(step) {
                            var stepSeconds = step.duration.value;
                            var nextStopSeconds = speedFactor - remainingSeconds;
                            while (nextStopSeconds <= stepSeconds) {
                                var nextStopLatLng = getPointBetween(step.start_location, step.end_location, nextStopSeconds / stepSeconds);
                                autoDriveSteps.push(nextStopLatLng);
                                nextStopSeconds += speedFactor;
                            }
                            remainingSeconds = stepSeconds + speedFactor - nextStopSeconds;
                        });
                        if (remainingSeconds > 0) {
                            autoDriveSteps.push(leg.end_location);
                        }
                    } else {
                        window.alert('Directions request failed due to ' + status);
                    }
                });
        }

        // helper method to calculate a point between A and B at some ratio
        function getPointBetween(a, b, ratio) {
            return new google.maps.LatLng(a.lat() + (b.lat() - a.lat()) * ratio, a.lng() + (b.lng() - a.lng()) * ratio);
        }

        // start the route simulation
        function startRouteAnimation(marker) {
            var autoDriveTimer = setInterval(function () {
                    // stop the timer if the route is finished
                    if (autoDriveSteps.length === 0) {
                        clearInterval(autoDriveTimer);
                    } else {
                        // move marker to the next position (always the first in the array)
                        marker.setPosition(autoDriveSteps[0]);
                        // remove the processed position
                        autoDriveSteps.shift();
                    }
                },
                1000);
        }
    </script>
  <p id="index">Index</p>
  <p id="index1">Index1</p>
  <p id="hresponse">http response</p>
  <button type="button" onclick="http_move()">Change States</button>
  </body>
</html>
