var position = new daum.maps.LatLng(37.572950635570876,126.9768891413955);

var map = new daum.maps.Map(document.getElementById('map'), {			
	center: position,
	level: 8,
	mapTypeId: daum.maps.MapTypeId.ROADMAP
});

var marker = new daum.maps.Marker({
	position: position
});
marker.setMap(map);

var infowindow = new daum.maps.InfoWindow({
	content: "지역을 선택하세요"
});
	infowindow.open(map, marker);		

$("#searcher_1").change(function() {
	var gu_latlng = $(this).val().split(",");
	var lat = parseFloat(gu_latlng[0]);
	var lng = parseFloat(gu_latlng[1]);
	var gu_name = $(this).children("option:selected").text();

	var position = new daum.maps.LatLng(lat, lng);

	var mapContainer = document.getElementById('map'), // 지도를 표시할 div  
		mapOption = {
			center: position, // 지도의 중심좌표
			level: 4 // 지도의 확대 레벨
		};
	
	var map = new daum.maps.Map(mapContainer, mapOption);

	$.ajax({
		url : "/mapdata",
		dataType : "json",
		data : {
			location : location
		},
		success : function(resp){
			current_row += 2;
			academy_list = resp.data;
			for(var i in academy_list){
				academy = academy_list[i];
				string = "<h1>"+ academy.id 
				+"</h1><h6>"+ academy.latlng +"</h6>";
				$("#academy_list").append(string);
		}
	},
	error : function(resp){
		console.log('invalid response!. Server error!');
	}	
	})

	
	var positions = [
		{
			title: 'LHOOQ', 
			latlng: new daum.maps.LatLng(37.500410,127.027005)
		},
		{
	    	title: 'Sarah Garden', 
	    	latlng: new daum.maps.LatLng(37.499022,127.029561)
		},
		{
	    	title: 'Leather Craft', 
	    	latlng: new daum.maps.LatLng(37.496860,127.025704)
		},
		{
	    	title: 'My Kitchen',
	    	latlng: new daum.maps.LatLng(37.496327,127.030125)
		},
		{
			title: 'Your Piano',
			latlng: new daum.maps.LatLng(37.498581,127.024800)
		}
	];

	var imageSrc = "http://i1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png";
	
	for (var i = 0; i < positions.length; i ++) {

		// 마커 이미지의 이미지 크기 입니다
		var imageSize = new daum.maps.Size(24, 35); 

		// 마커 이미지를 생성합니다    
		var markerImage = new daum.maps.MarkerImage(imageSrc, imageSize); 

		// 마커를 생성합니다
		var marker = new daum.maps.Marker({
			map: map, // 마커를 표시할 지도
			position: positions[i].latlng, // 마커를 표시할 위치
			// title : positions[i].title, // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
			image : markerImage // 마커 이미지 
		});

		var infowindow = new daum.maps.InfoWindow({
			content: positions[i].title
		});
		infowindow.open(map, marker);
	}			

	var marker = new daum.maps.Marker({
		position: position
	});
	marker.setMap(map);

	var infowindow = new daum.maps.InfoWindow({
		content: gu_name
	});
	infowindow.open(map, marker);

	var content = '<div class="overlaybox">' +
			'    <div class="boxtitle">추천 학원 정보</div>' +
			'    <div class="first">' +
			'        <div class="triangle text">1</div>' +
			'        <div class="academytitle text">LHOOQ</div>' +
			'    </div>' +
			'    <ul>' +
			'        <li class="up">' +
			'            <span class="number">2</span>' +
			'            <span class="title">Sarah garden</span>' +
			'            <span class="arrow up"></span>' +
			'            <span class="count">2</span>' +
			'        </li>' +
			'        <li>' +
			'            <span class="number">3</span>' +
			'            <span class="title">Leather Craft</span>' +
			'            <span class="arrow up"></span>' +
			'            <span class="count">6</span>' +
			'        </li>' +
			'        <li>' +
			'            <span class="number">4</span>' +
			'            <span class="title">My Kitchen</span>' +
			'            <span class="arrow up"></span>' +
			'            <span class="count">3</span>' +
			'        </li>' +
			'        <li>' +
			'            <span class="number">5</span>' +
			'            <span class="title">Chuizone Piano</span>' +
			'            <span class="arrow down"></span>' +
			'            <span class="count">1</span>' +
			'        </li>' +
			'    </ul>' +
			'</div>';

	var customOverlay = new daum.maps.CustomOverlay({
		position: position,
		content: content,
		xAnchor: -0.1,
		yAnchor: 0
	});

	customOverlay.setMap(map);	
});