$(document).ready(function() {


  var url = window.location.href
  var u = url.split('/')
  var uu = u[3]
  console.log(u[3])
  console.log(uu)
  var home = document.getElementById("home");
  var around = document.getElementById("around");
  var community = document.getElementById("community");
  var market = document.getElementById("market");
  var mypage = document.getElementById("mypage");
    if (url == "http://127.0.0.1:8000/"){
    home.style.color = "#6E6CBF";
    home.style.fontWeight = "bold";
    }
    if (uu == "social"){
    around.style.color = "#6E6CBF";
    around.style.fontWeight = "bold";
    }
    if (uu == "board"){
    community.style.color = "#6E6CBF";
    community.style.fontWeight = "bold";
    }
    if (uu == "market"){
    market.style.color = "#6E6CBF";
    market.style.fontWeight = "bold";
    }
    if (uu == "user"){
    mypage.style.color = "#6E6CBF";
    mypage.style.fontWeight = "bold";
    }



    setInterval(function()
    {

       chk.click();


    },10000);
const clock = document.getElementById('clock');


function getTime(){
var date = new Date();

    // date Object를 받아오고
    var month = date.getMonth();

    // 달을 받아옵니다
    var clockDate = date.getDate();

    // 몇일인지 받아옵니다
    var day = date.getDay();

    // 요일을 받아옵니다.
    var week = ['일', '월', '화', '수', '목', '금', '토'];
    const time = new Date();
    const hour = time.getHours();
    const minutes = time.getMinutes();
    const seconds = time.getSeconds();
    //clock.innerHTML = hour +":" + minutes + ":"+seconds;

    clock.innerHTML = `${month+1}월 ${clockDate}일 ${week[day]}요일 ` +`${hour<10 ? `0${hour}`:hour}:${minutes<10 ? `0${minutes}`:minutes}:${seconds<10 ? `0${seconds}`:seconds}`
}


function init(){
    setInterval(getTime, 1000);
}

init();
});