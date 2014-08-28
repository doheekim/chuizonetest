window.onload = function(data) {
	$.ajax({
		url: '/mapnlist',
		type: 'GET',
		dataType: 'JSON',

		var position = new daum.maps.LatLng(data.position)
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
	})
});




