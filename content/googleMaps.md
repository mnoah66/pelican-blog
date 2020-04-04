Title: Customizing the Google Maps JavaScript API
slug: google-maps-county-border
date: 2018-11-16
category: Blog
Tags: googlemaps
share_post:true
og_image:images/googlemapsfinished.jpg
Summary: Adding county borders and multiple markers and InfoWindows for an interactive Google Map experience.

The inspiration for this tutorial was the difficulty I had in finding solutions to a few things related to Google Maps JavaScript API.  The first being how to add borders to geographical areas, like the outline of a county or state.  The second was how to add multiple markers to a map, each with their own unique InfoWindow.  And finally, how to use custom marker icons and not the standard red pin.

In this post we're going to tackle creating an interactive map with the Google Maps API.  We'll cover how to add multiple markers all with their own InfoWindow popup that includes a styled description and image.  We'll also only highlight a section of the map to focus the users attention on what we want them to interact with.  We'll pretend to be a craft beer brewery with multiple locations in Warren County, NJ, so only Warren County will be highlighted by including the boundary lines and shading the rest of the map.

Required:

1.  A Google account
2.  Google Maps API credentials

Login to your Google account, then head over to the Maps JavaScript API overview page (https://developers.google.com/maps/documentation/javascript/tutorial), grab an API key and pull the template HTML file.  Remember to stick your own API key in 

```<script async defer src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&callback=initMap"
     type="text/javascript"></script>
  ```

Save your file and open in a browser.  It should open a Google Map hovering near Sydney, Australia.  Let's change it to center on Warren County, NJ and then zoom in a little bit more.  In the `initMap()` function, change the lat and lng values and the zoom value:

```html
<script>
      var map;
      function initMap() {
        map = new google.maps.Map(document.getElementById('map'), {
          center: {lat: 40.869176, lng: -74.943978},
          zoom: 10
        });
      }
</script>
```

Save `index.html` and refresh the browser.  The map should be centered over Warren County, NJ.

## County Boundary

If you go to google.com and search for "Warren County, NJ" and then click the Maps tab, you'll see a pink/red outline of the county which is what we're going to recreate.  This is made up of hundreds of lat/lng coordinates, which would be nearly impossible to create manually.  Luckily, Google has already done this in a Fusion Table: (https://fusiontables.google.com/data?docid=1xdysxZ94uUFIit9eXmnw1fYc6VcQiXhceFd_CVKa#map:id=2)

1.  Click the rows tab
2.  Search for Warren
3.  Find the Warren County NJ row, double click it to view the data.
4.  In the popup window, locate the geometry section which includes all of the polygon coordinates for the outer boundary for Warren County.
<img style="max-width: 400px;width:100%; height:  auto;" src='/images/Coordinates_Warren_County.jpg'>
5.  Extract the data how you wish (I'll use Excel) so that you have an array of objects like this:

```javascript
var warrenCountyCoordinates = [
          {lat: 25.774, lng: -80.190},
          {lat: 18.466, lng: -66.118},
          {lat: 32.321, lng: -64.757},
          {lat: 25.774, lng: -80.190},
          // The rest of the coordinates
        ];
```

> When you paste the data in Excel, you'll have to do some funky data manipulation.  
> 1) Use the Text to Columns option, fixed width, to split all of the data where there is a space in the contents.
> 2) Copy the data, then paste and transpose so that the data fills columns and not rows.
> 3) Use the Text to Columns option again, this time with the delimited option, delimited by a comma, so that the `lng` values fill one column, and the `lat` values fill another column.
> 4) Concatenate the values together using a formula `="{lat: "&C4&", lng: "&B4&"},"` (assuming your data starts at B4).  For whatever reason the lat/lng
>coordinates from the fusion table are reversed, so keep that in mind when manipulating the data.

<img style="max-width: 400px;width:100%; height:  auto;" src='/images/latLng.jpg'>

Copy and paste the array into the same `initMap` function in a variable called 'warrenCountyCoordinates', just after the creation of the map.

```javascript
var map;
function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 40.869176, lng: -74.943978},
    zoom: 10
  });

  var warrenCountyCoordinates = [
    {lat: 40.92404, lng: -75.09537},
    // The rest of the coordinates
```

If you refresh your browser, nothing will change.  That's because we need to add a Polygon with those coordinates:

```javascript
  var warrenCountyBorder = new google.maps.Polygon({
            paths: warrenCountyCoordinates,
            strokeColor: '#000000',
            strokeOpacity: 0.8,
            strokeWeight: 2,
            fillColor: '#FF0000',
            fillOpacity: 0.35
          });
  warrenCountyBorder.setMap(map);
```
Save index.html and refresh your browser and Warren County, NJ should be highlighted.

So far, so good!  But I don't want to highlight Warren County.  Instead, I want to "un-highlight" it and shade the rest of the map.  Google calls this ["Polygon with Hole"](https://developers.google.com/maps/documentation/javascript/examples/polygon-hole)

Let's define our outer coordinates (the rest of the world, mostly):

```javascript
  var everythingElse = [
            {lat: 42.729886, lng: -71.420584},
            {lat: 42.568274, lng: -77.045584},
            {lat: 38.586262, lng:-76.769553},
            {lat: 38.500334, lng:-73.089133}
          ];
```

And now modify our `warrenCountyBorder` paths value to an array of `everythingElse` and `warrenCountyCoordinates`.  Experiment with the `stroke` and `fill` variables to your desired settings:

```javascript
  var warrenCountyBorder = new google.maps.Polygon({
            paths: [everythingElse, warrenCountyCoordinates],
            strokeColor: '#000000',
            strokeOpacity: 0.8,
            strokeWeight: 2,
            fillColor: '#000000',
            fillOpacity: 0.35
          });
```

Refresh your browser, and Warren County should be "highlighted."

<img style="max-width: 400px;width:100%; height:  auto;"src="/images/boundary_map.jpg">

## Markers and InfoWindows

I want to place markers on the map for each one of my brewery locations.  When the user clicks on the marker, I also want an InfoWindow to appear with a description of that brewery and an image.

Still in our `initMap()` function, let's first create an array of our brewery locations where the `desc` is the HTML description we want in the InfoWindow:

```javascript
  var breweries = [{
            position: new google.maps.LatLng(40.971508, -75.003786),
            desc: '<div id="content">' +
              '<div id="siteNotice">' +
              '</div>' +
              '<h1 id="firstHeading" class="firstHeading">Blairstown Brews</h1>' +
              '<div id="bodyContent">' +
              '<p><b>Blairstown Brews</b> is home to our Blairstown Blues; playing live Fri-Sun, 12-4pm.</p><br> ' +
              '<p><b>Fun Fact:</b> Fun fact goes here!</p><br>' +
              '<IMG style="max-width: 400px;width:100%; height:  auto; class="ImageBorder" SRC="https://i.imgur.com/9ByhOFK.jpg">' +
              '</div>' +
              '</div>'
          },{
            position: new google.maps.LatLng(40.910303, -74.887056),
            desc: '<div id="content">' +
              '<div id="siteNotice">' +
              '</div>' +
              '<h1 id="firstHeading" class="firstHeading">Jenny Jump Brews</h1>' +
              '<div id="bodyContent">' +
              '<p><b>Jenny Jump</b> location is home to our famous Jenny Jump IPA.</p><br> ' +
              '<p><b>Fun Fact:</b> Fun fact goes here!</p><br>' +
              '<IMG style="max-width: 400px;width:100%; height:  auto;class="ImageBorder" SRC="https://i.imgur.com/9ByhOFK.jpg">' +
              '</div>' +
              '</div>'
          }, {
            position: new google.maps.LatLng(40.775896, -75.066957),
            desc: '<div id="content">' +
              '<div id="siteNotice">' +
              '</div>' +
              '<h1 id="firstHeading" class="firstHeading">Summerfield Brews</h1>' +
              '<div id="bodyContent">' +
              '<p>The <b>Summerfield Brews</b> location is home to 6 different beers. ' +
              '</p><br>' +
              '<p><b>Fun Fact:</b> Fun fact goes here!</p><br>' +
              '<IMG style="max-width: 400px;width:100%; height:  auto;class="ImageBorder" SRC="https://i.imgur.com/9ByhOFK.jpg">' +
              '</div>' +
              '</div>'
          }];
```
Then create a function to add the Markers and create the InfoWindow when it a `click` event triggers.  One of the options for the marker is `icon` which I have set to a URL a purple pin from [Jeffs-icons.com](http://www.jeffs-icons.com/map_icons.html)
```javascript
  var currentMarker = false
  function addMarker(brewery) {
    var marker = new google.maps.Marker({
      position: brewery.position,
      map: map,
      icon: 'http://www.jeffs-icons.com/map_icons/ICONS/Pin/pin-red_violet-R.png',
      zIndex: brewery[1]
      });

    // Create the infowindow
    marker.info = new google.maps.InfoWindow({
      content: brewery.desc
      });

    // When marker is clicked, open infowindow and close any open ones
    google.maps.event.addListener(marker, 'click', function() {
      if (currentMarker) {
          currentMarker.close();
      }
      currentMarker = marker.info
      currentMarker.open(map, marker);
      });
```

And finally, loop over the items in our `breweries` array and call the `addMarker` function on each item.  This loop should be in the `initMap()` scope:

```javascript
  for (var i = 0, brewery; brewery = breweries[i]; i++) {
            addMarker(brewery);
          }
```

Refresh the browser and click on one of the markers and voila!  But there are two more things we want to improve.  
1.  We have to click the tiny 'x' icon to close out the InfoWindow.
2.  When the InfoWindow opens, the map will move to display the InfoWindow. After closing the InfoWindow, our map is no longer centered over Warren County.

**Solution: add eventListeners so that the user can click anywhere on the map and the InfoWindow will close and the map will re-center itself back to it's initial setting.**

In the `addMarker()` function, add the following:

```javascript
  // The same 'center' coordinates from initMap()  
  var myLatlng =  new google.maps.LatLng(40.869176, -74.943978);

  // If user clicks in map, close infowindow(s)
  google.maps.event.addListener(map, 'click', function() {
    marker.info.close(map, marker);
    map.setCenter(myLatlng);
  });

  // If user clicks in surrounding area, close infowindow(s)
  google.maps.event.addListener(warrenCountyBorder, 'click', function() {
    marker.info.close(warrenCountyBorder, marker);
    map.setCenter(myLatlng);
  });

```

Save and refresh the browser, and test that everything works as expected.  If not, the source code is available below and here is a link to the Code Snippet on jsfiddle: [JSFiddle](http://jsfiddle.net/meqjfs7x/2/)

<img style="max-width: 800px;width:100%; height:  auto;"src="/images/googlemapsfinished.jpg">

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Simple Map</title>
    <meta name="viewport" content="initial-scale=1.0">
    <meta charset="utf-8">
    <style>
      /* Always set the map height explicitly to define the size of the div
       * element that contains the map. */
      #map {
        height: 100%;
      }
      /* Optional: Makes the sample page fill the window. */
      html, body {
        height: 100%;
        margin: 0;
        padding: 0;
      }
       #firstHeading {
            text-align: center;
        }

      .ImageBorder {
        border-radius: 5px;
        max-width: 300px !important;
        height: auto;
       }

       #bodyContent {
        text-align: justify;
        text-align-last: center;
       }

       #content {
        height: 100%;
       }

       
    </style>
  </head>
  <body>
    <div id="map"></div>
    <script>
    var map;
    function initMap() {
        map = new google.maps.Map(document.getElementById('map'), {
          center: {lat: 40.869176, lng: -74.943978},
          zoom: 10,
          styles: [{"elementType":"geometry","stylers":[{"color":"#f5f5f5"}]},{"elementType":"labels.icon","stylers":[{"visibility":"off"}]},{"elementType":"labels.text.fill","stylers":[{"color":"#616161"}]},{"elementType":"labels.text.stroke","stylers":[{"color":"#f5f5f5"}]},{"featureType":"administrative.land_parcel","elementType":"labels.text.fill","stylers":[{"color":"#bdbdbd"}]},{"featureType":"poi","elementType":"geometry","stylers":[{"color":"#eeeeee"}]},{"featureType":"poi","elementType":"labels.text.fill","stylers":[{"color":"#757575"}]},{"featureType":"poi.park","elementType":"geometry","stylers":[{"color":"#e5e5e5"}]},{"featureType":"poi.park","elementType":"labels.text.fill","stylers":[{"color":"#9e9e9e"}]},{"featureType":"road","elementType":"geometry","stylers":[{"color":"#ffffff"}]},{"featureType":"road.arterial","elementType":"labels.text.fill","stylers":[{"color":"#757575"}]},{"featureType":"road.highway","elementType":"geometry","stylers":[{"color":"#dadada"}]},{"featureType":"road.highway","elementType":"labels.text.fill","stylers":[{"color":"#616161"}]},{"featureType":"road.local","elementType":"labels.text.fill","stylers":[{"color":"#9e9e9e"}]},{"featureType":"transit.line","elementType":"geometry","stylers":[{"color":"#e5e5e5"}]},{"featureType":"transit.station","elementType":"geometry","stylers":[{"color":"#eeeeee"}]},{"featureType":"water","elementType":"geometry","stylers":[{"color":"#c9c9c9"}]},{"featureType":"water","elementType":"labels.text.fill","stylers":[{"color":"#9e9e9e"}]}]
        });
        var warrenCountyCoordinates = [
            {lat: 40.92404, lng: -75.09537},
            {lat: 40.94308, lng: -75.10839},
            {lat: 40.96622, lng: -75.11937},
            {lat: 40.9683, lng: -75.12043},
            {lat: 40.96924, lng: -75.12131},
            {lat: 40.96965, lng: -75.1259},
            {lat: 40.96925, lng: -75.13127},
            {lat: 40.9738, lng: -75.13553},
            {lat: 40.97949, lng: -75.13356},
            {lat: 40.98273, lng: -75.13207},
            {lat: 40.98633, lng: -75.13148},
            {lat: 40.99005, lng: -75.1313},
            {lat: 40.99358, lng: -75.12768},
            {lat: 40.99917, lng: -75.11695},
            {lat: 41.0041, lng: -75.10911},
            {lat: 41.00571, lng: -75.10424},
            {lat: 41.01523, lng: -75.08809},
            {lat: 41.01636, lng: -75.08306},
            {lat: 41.01719, lng: -75.07492},
            {lat: 41.03021, lng: -75.0447},
            {lat: 41.03909, lng: -75.02827},
            {lat: 41.04213, lng: -75.02588},
            {lat: 41.05549, lng: -75.01724},
            {lat: 41.06755, lng: -75.00927},
            {lat: 41.07352, lng: -74.99997},
            {lat: 41.07731, lng: -74.99306},
            {lat: 41.07917, lng: -74.98259},
            {lat: 41.08529, lng: -74.97099},
            {lat: 41.09069, lng: -74.96728},
            {lat: 41.09377, lng: -74.96681},
            {lat: 41.09452, lng: -74.96692},
            {lat: 41.09445, lng: -74.96684},
            {lat: 41.09163, lng: -74.96372},
            {lat: 41.0892, lng: -74.96129},
            {lat: 41.0788, lng: -74.94994},
            {lat: 41.06187, lng: -74.93138},
            {lat: 41.04911, lng: -74.91775},
            {lat: 41.03732, lng: -74.90515},
            {lat: 41.02011, lng: -74.88658},
            {lat: 41.01617, lng: -74.8823},
            {lat: 41.01291, lng: -74.87876},
            {lat: 40.99648, lng: -74.86091},
            {lat: 40.9905, lng: -74.85441},
            {lat: 40.9803, lng: -74.84321},
            {lat: 40.98007, lng: -74.84299},
            {lat: 40.96701, lng: -74.82869},
            {lat: 40.96597, lng: -74.82754},
            {lat: 40.96511, lng: -74.82659},
            {lat: 40.9607, lng: -74.82171},
            {lat: 40.95408, lng: -74.81419},
            {lat: 40.94936, lng: -74.80907},
            {lat: 40.94195, lng: -74.80096},
            {lat: 40.9288, lng: -74.78641},
            {lat: 40.92383, lng: -74.78104},
            {lat: 40.9165, lng: -74.77301},
            {lat: 40.91228, lng: -74.7683},
            {lat: 40.91187, lng: -74.7679},
            {lat: 40.91182, lng: -74.76787},
            {lat: 40.9117, lng: -74.7681},
            {lat: 40.90516, lng: -74.77621},
            {lat: 40.90412, lng: -74.77973},
            {lat: 40.90216, lng: -74.78251},
            {lat: 40.90035, lng: -74.78306},
            {lat: 40.8988, lng: -74.78604},
            {lat: 40.88816, lng: -74.79675},
            {lat: 40.88403, lng: -74.80576},
            {lat: 40.88013, lng: -74.80689},
            {lat: 40.87315, lng: -74.80615},
            {lat: 40.86744, lng: -74.80662},
            {lat: 40.86157, lng: -74.80323},
            {lat: 40.86016, lng: -74.80966},
            {lat: 40.85332, lng: -74.81162},
            {lat: 40.84718, lng: -74.82184},
            {lat: 40.84144, lng: -74.82057},
            {lat: 40.83491, lng: -74.82235},
            {lat: 40.82569, lng: -74.83008},
            {lat: 40.81969, lng: -74.8348},
            {lat: 40.81325, lng: -74.84198},
            {lat: 40.80521, lng: -74.84935},
            {lat: 40.80195, lng: -74.8607},
            {lat: 40.80205, lng: -74.86554},
            {lat: 40.79466, lng: -74.8707},
            {lat: 40.79082, lng: -74.87964},
            {lat: 40.78795, lng: -74.8896},
            {lat: 40.78783, lng: -74.88975},
            {lat: 40.78777, lng: -74.88984},
            {lat: 40.7807, lng: -74.90443},
            {lat: 40.77139, lng: -74.90313},
            {lat: 40.76157, lng: -74.91599},
            {lat: 40.75433, lng: -74.92732},
            {lat: 40.74704, lng: -74.93448},
            {lat: 40.737, lng: -74.94375},
            {lat: 40.72718, lng: -74.95293},
            {lat: 40.71908, lng: -74.96418},
            {lat: 40.70993, lng: -74.9707},
            {lat: 40.70517, lng: -74.98423},
            {lat: 40.69645, lng: -75.00024},
            {lat: 40.69451, lng: -75.01697},
            {lat: 40.68321, lng: -75.03865},
            {lat: 40.67524, lng: -75.05694},
            {lat: 40.66658, lng: -75.07078},
            {lat: 40.65751, lng: -75.08241},
            {lat: 40.65035, lng: -75.09329},
            {lat: 40.64027, lng: -75.10843},
            {lat: 40.63637, lng: -75.1202},
            {lat: 40.63056, lng: -75.13474},
            {lat: 40.62568, lng: -75.14809},
            {lat: 40.62031, lng: -75.15611},
            {lat: 40.61049, lng: -75.16551},
            {lat: 40.59821, lng: -75.17751},
            {lat: 40.59188, lng: -75.18945},
            {lat: 40.59178, lng: -75.1896},
            {lat: 40.59213, lng: -75.18977},
            {lat: 40.59294, lng: -75.19014},
            {lat: 40.59346, lng: -75.1905},
            {lat: 40.59382, lng: -75.19074},
            {lat: 40.59418, lng: -75.19099},
            {lat: 40.59431, lng: -75.19108},
            {lat: 40.59549, lng: -75.19144},
            {lat: 40.59665, lng: -75.19165},
            {lat: 40.59745, lng: -75.19174},
            {lat: 40.59752, lng: -75.19175},
            {lat: 40.59799, lng: -75.19185},
            {lat: 40.59855, lng: -75.19197},
            {lat: 40.5987, lng: -75.19201},
            {lat: 40.59973, lng: -75.19223},
            {lat: 40.60105, lng: -75.19222},
            {lat: 40.60143, lng: -75.1922},
            {lat: 40.60145, lng: -75.1922},
            {lat: 40.60168, lng: -75.19219},
            {lat: 40.60268, lng: -75.19229},
            {lat: 40.60346, lng: -75.19271},
            {lat: 40.60431, lng: -75.19373},
            {lat: 40.60464, lng: -75.19413},
            {lat: 40.60583, lng: -75.19514},
            {lat: 40.60679, lng: -75.19592},
            {lat: 40.60767, lng: -75.19642},
            {lat: 40.60815, lng: -75.19671},
            {lat: 40.60858, lng: -75.1968},
            {lat: 40.62149, lng: -75.18928},
            {lat: 40.64391, lng: -75.19628},
            {lat: 40.65387, lng: -75.1976},
            {lat: 40.66509, lng: -75.18431},
            {lat: 40.67483, lng: -75.17694},
            {lat: 40.67971, lng: -75.18778},
            {lat: 40.68788, lng: -75.20225},
            {lat: 40.7124, lng: -75.19508},
            {lat: 40.72117, lng: -75.18613},
            {lat: 40.73727, lng: -75.18578},
            {lat: 40.75778, lng: -75.18731},
            {lat: 40.77565, lng: -75.1737},
            {lat: 40.77479, lng: -75.14938},
            {lat: 40.78188, lng: -75.12746},
            {lat: 40.79016, lng: -75.11067},
            {lat: 40.80627, lng: -75.10057},
            {lat: 40.82427, lng: -75.08404},
            {lat: 40.84052, lng: -75.09742},
            {lat: 40.84972, lng: -75.07876},
            {lat: 40.85412, lng: -75.05984},
            {lat: 40.87998, lng: -75.06041},
            {lat: 40.91349, lng: -75.07901},
            {lat: 40.92327, lng: -75.09419},
        ];

        // Random polygon covering northeast region
        var everythingElse = [
            {lat: 42.729886, lng: -71.420584},
            {lat: 42.568274, lng: -77.045584},
            {lat: 38.586262, lng:-76.769553},
            {lat:38.500334, lng:-73.089133}
        ];
        
        var warrenCountyBorder = new google.maps.Polygon({
            paths: [everythingElse, warrenCountyCoordinates],
            strokeColor: '#000000',
            strokeOpacity: 0.8,
            strokeWeight: 2,
            fillColor: '#000000',
            fillOpacity: 0.35
        });
        
        var breweries = [{
          position: new google.maps.LatLng(40.971508, -75.003786),
          desc: '<div id="content">' +
            '<div id="siteNotice">' +
            '</div>' +
            '<h1 id="firstHeading" class="firstHeading">Blairstown Brews</h1>' +
            '<div id="bodyContent">' +
            '<p><b>Blairstown Brews</b> is home to our Blairstown Blues; playing live Fri-Sun, 12-4pm.fr thus iuajsoijt rlopren amoie frujer d iwuc eriuj . eur jfeiurjf  ieurhf eiurfjeirujf eirujf</p><br> ' +
            '<IMG class="ImageBorder" SRC="https://i.imgur.com/9ByhOFK.jpg">' +
            '</div>' +
            '</div>'
        },{
          position: new google.maps.LatLng(40.910303, -74.887056),
          desc: '<div id="content">' +
            '<div id="siteNotice">' +
            '</div>' +
            '<h1 id="firstHeading" class="firstHeading">Jenny Jump Brews</h1>' +
            '<div id="bodyContent">' +
            '<p><b>Jenny Jump</b> location is home to our famous Jenny Jump IPA.</p><br> ' +
            '<IMG class="ImageBorder" SRC="https://i.imgur.com/9ByhOFK.jpg">' +
            '</div>' +
            '</div>'
        }, {
          position: new google.maps.LatLng(40.775896, -75.066957),
          desc: '<div id="content">' +
            '<div id="siteNotice">' +
            '</div>' +
            '<h1 id="firstHeading" class="firstHeading">Summerfield Brews</h1>' +
            '<div id="bodyContent">' +
            '<p>The <b>Summerfield Brews</b> location is home to 6 different beers. ' +
            '</p><br>' +
            '<IMG class="ImageBorder" SRC="https://i.imgur.com/9ByhOFK.jpg">' +
            '</div>' +
            '</div>'
        }];
        var currentMarker = false
        function addMarker(brewery) {
          var marker = new google.maps.Marker({
            position: brewery.position,
            icon: 'http://www.jeffs-icons.com/map_icons/ICONS/Pin/pin-red_violet-R.png',
            map: map,
            zIndex: brewery[1]
            });
          marker.info = new google.maps.InfoWindow({
            content: brewery.desc,
            maxWidth: 300
            });
          
          // When marker is clicked, open infowindow and close any open ones
          google.maps.event.addListener(marker, 'click', function() {
            if (currentMarker) {
                currentMarker.close();
            }
            currentMarker = marker.info
            currentMarker.open(map, marker);
            });
        
          // The same 'center' coordinates from initMap()  
          var myLatlng =  new google.maps.LatLng(40.869176, -74.943978);
          
          // If user clicks in map, close infowindow(s)
          google.maps.event.addListener(map, 'click', function() {
            marker.info.close(map, marker);
            map.setCenter(myLatlng);
          });

          // If user clicks in surrounding area, close infowindow(s)
          google.maps.event.addListener(warrenCountyBorder, 'click', function() {
            marker.info.close(warrenCountyBorder, marker);
            map.setCenter(myLatlng);
          });

        } // End addMarker() function
        
        // create marker from each brewery in our list
        for (var i = 0, brewery; brewery = breweries[i]; i++) {
          addMarker(brewery);
        }

        // Add the county border layer to the map
        warrenCountyBorder.setMap(map);

    } // End initMap()
    </script>
    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBQ26wZWQ95D6J4u8obmH-HoD-_Ftqvk-M&callback=initMap"
    async defer></script>
  </body>
</html>
```
