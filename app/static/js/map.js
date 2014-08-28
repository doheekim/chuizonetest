$(document).ready(function(){
	var element = document.getElementById("new-element-1");
	var position = new daum.maps.LatLng(position)
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
		content: guname + '취미학원 표시'
	});
	infowindow.open(map, marker);
});


	


