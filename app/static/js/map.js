window.onload = function(data) {
	var position101 = new daum.maps.LatLng(37.49796298370522, 127.02761094942744);
	var position102 = new daum.maps.LatLng(37.53589682068908, 127.13235618124992);	
	var position123 = new daum.maps.LatLng(37.57042061397492, 126.99213459583619);	

	var map = new daum.maps.Map(document.getElementById('map'), {
		center: data.position,
		level: 4,
		mapTypeId: daum.maps.MapTypeId.ROADMAP
	});

	var marker = new daum.maps.Marker({
		position: data.position
	});
	marker.setMap(map);

	var infowindow = new daum.maps.InfoWindow({
		content: data.local + '취미학원 표시'
	});
	infowindow.open(map, marker);
};
