$(document).ready(function(){
	// location = $('asdf').eval();
	var position = new daum.maps.LatLng()
	var map = new daum.maps.Map(document.getElementById('map'), {
		center: position,
		level: 4,
		mapTypeId: daum.maps.MapTypeId.ROADMAP
	});

	var marker = new daum.maps.Marker({
		position: position
	});
	marker.setMap(map);

	var infowindow = new daum.maps.InfoWindow({
		content: data.local + '취미학원 표시'
	});
	infowindow.open(map, marker);
});


	


