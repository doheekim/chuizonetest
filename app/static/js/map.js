window.onload = function() {
	var position = new daum.maps.LatLng(37.537123, 127.005523);

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
		content: 'Hello, Chuizone! We are preparing for hobby map and hobby matching system'
	});
	infowindow.open(map, marker);
};