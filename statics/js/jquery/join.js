   /* 중복체크! */
   $(function(){
      /* 아이디 수정했을 때 */
      $('#email').change(function () {
         $('#img-email').hide();
         $('#btn-email').show();
      });



      $('#join-submit').click(function () {
         var name = $('#name').val()
         if(name == ''){
            alert('이름을 입력해 주세요.')
            $("#name").focus();
            return false;
         }
         var email = $('#email').val()
         if(email ==''){
            alert('이메일을 입력해 주세요')
            $("#email").focus();
            return false;
         }
         if($("#join-submit").attr("id_check_result") == "fail") {
            alert("이메일 중복체크를 해주시기 바랍니다.");
            $("#email").focus();
            return false;
          }
         var password = $('#password').val()
         if(password == ''){
            alert('비밀번호를 입력해 주세요.')
            $("#password").focus();
            return false;
         }
         if(password.length < 8){
            alert('8글자 이상 입력해주세요.')
            $("#password").focus();
            return false;
         }

         var password2 = $('#password2').val()
         if(password2 == ''){
            alert('비밀번호 확인을 입력해주세요.')
            $("#password2").focus();
            return false;
         }
         if (password != "" || password2 != "") {
            if (password == password2) {
            } else {
               alert("비밀번호가 일치하지 않습니다. 비밀번호를 재확인해주세요.");
               return false;
            }
         }
      });


      $('#btn-email').click(function(){

         if(email == ''){
            alert('이메일을 입력해주세요.')
            return;
         }



         $.ajax({
            url:'/user/api/checkemail?email='+email,
            type:'get',
            dataType:'json',
            success:function(response){
               if(response.result != 'success'){
                  console.error(response.data)
                  return;
               }
               if(response.data == 'exist'){
                  alert("존재하는 이메일 입니다.");
                  $('#email').val('').focus();
                  return;
               }else{
                  $('#img-email').show();
                  $('#btn-email').hide();
                  $("#join-submit").attr("id_check_result", "success");
                  return;
               }
               // console.log(response)
            },
                error : function(xhr, error){
               alert("서버와의 통신에서 문제가 발생했습니다.");
               console.error("error : " + error);
            }
         })
      });

    // $('#join-form').submit(function() {
   //
   //
   //
   //
   //
   //
   //    });

      $("#email").on("propertychange change keyup paste input", function(){
         $('#img-email').hide();
         $('#btn-email').show();
         $("#join-submit").attr("id_check_result", "fail");
      });
   });