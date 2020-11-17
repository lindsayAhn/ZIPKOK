
$(function(){

    // 질문유형을 선택한다.
    account('0' , '00');

});

function account(type , select) {

    $('#lowaccount').empty();
    //
        if (type == '0') {

        } else if (type == '1') { // 미술
            $('#lowaccount').append("<option value='11' >아이패드 드로잉</option>'");
            $('#lowaccount').append("<option value='12' >파스텔/ 오일파스텔</option>'");
            $('#lowaccount').append("<option value='13' >유화</option>'");
            $('#lowaccount').append("<option value='14' >캘리그래피</option>'");
        } else if (type == '2') {  // 공예
            $('#lowaccount').append("<option value='21' >프랑스자수</option>'");
            $('#lowaccount').append("<option value='22' >십자수</option>'");
            $('#lowaccount').append("<option value='23' >라탄 공예</option>'");
            $('#lowaccount').append("<option value='24' >레진 공예</option>'");
            $('#lowaccount').append("<option value='25' >펠트 공예</option>'");
            $('#lowaccount').append("<option value='26' >뜨개질</option>'");
            $('#lowaccount').append("<option value='27' >향초</option>'");
        } else if (type == '3') {  // 윤동
            $('#lowaccount').append("<option value='31' >여성 홈트레이닝</option>'");
            $('#lowaccount').append("<option value='32' >남성 홈트레이닝</option>'");
            $('#lowaccount').append("<option value='33' >PT 기구 사용법</option>'");
        } else if (type == '4') {  // 음악/댄스

        } else if (type == '5') {  // 악기
            $('#lowaccount').append("<option value='51' >통기타/ 일렉기타</option>'");
            $('#lowaccount').append("<option value='52' >우쿠렐레</option>'");
            $('#lowaccount').append("<option value='53' >피아노</option>'");
            $('#lowaccount').append("<option value='54' >기타</optio>'");
        } else if (type == '6') {  // 요리

        } else if (type == '7') {  // 홈카페

        } else if (type == '8') {  // 영화감상

        } else if (type == '9') {  // 독서

        } else if (type == '10') {  // 기타
            $('#lowaccount').append("<option value='101' >다이어리 꾸미기</option>'");
            $('#lowaccount').append("<option value='102' >주식투자</option>'");
        }
        document.getElementById("lowaccount").style.display = "";

        if ($.trim(select) != "") {
            $('#select1').val(type);
            $('#lowaccount').val(select);
        }

 }

 $('#dontSubmit').click(function () {
  // if (type == 0) {
    //   alert('카테고리를 선택해 주세요.')
      // $("#select1").focus();
       //return false;
   //} else if (type != '') {
     //  var urladress = $('#urladress').val()
       //  if (urladress == '') {
         //  alert('url주소를 입력하세요.')
         //$("#urladress").focus();
   //    return false;
  // }
   // }
})

