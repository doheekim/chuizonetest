$(document).ready(function(){
	$.ajax({
		url: '/mapnlist',
		type: 'GET',
		dataType: 'JSON',
		success: function(data){
			if(data.position){
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
			}
			else{
				console.log('position error');
			}
		},
		error: function(data) {
			console.log('Server Error');
		}
	})
});


	


