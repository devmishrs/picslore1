var map;
$(document).ready(function(){
    getLocation();
    $('#id_get_location').click(function(position){
        getLocation();
        console.log('ajax called.');
        console.log('Ajax Done.');
    });
});
function getLocation(){
    console.log("Location called");
    navigator.geolocation.getCurrentPosition(function(position){
    let lat = position.coords.latitude
    let long = position.coords.longitude
    console.log('Getting Location');

    $.ajax({
        type:'POST',
        url:'/get_location/',
        data:{'latitude':position.coords.latitude, 'longitude':position.coords.longitude},
        success:function(){
            console.log('Location saved.');
            
        }
    
    });
    console.log(lat);
    console.log(long);
    console.log('This is Location') ;   
    })
}


function showPosition(position){
    var valu = document.getElementById('demo');
    valu.innerHTML  = 'Latitude:  '+position.coords.latitude+"<br> Longitude:  "+position.coords.longitude;
    var Lat = position.coords.latitude
    var Long = position.coords.Longitude
    console.log(valu.innerHTML)
    console.log(position.coords.latitude,'---------------');
}

function initMap() {
    map = new google.maps.Map(document.getElementById('id_map'), {
      center: {lat: -34.397, lng: 150.644},
      zoom: 8
    });
  }


