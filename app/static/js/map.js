window.onload = function() {
	$.ajax({
		url: '/mapnlist',
		type: 'POST',
		dataType: 'JSON',
		success: function(data) {
			if(data.success){
				var position = new daum.maps.LatLng(data.gu_latlng);
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
					content: data.gu_name + '취미학원 표시'
				});
				infowindow.open(map, marker);
			else{
				console.log('fail!');
			}
		},
		error: function(data) {
			console.log('Server Error');
		}
	})
});


	


