var thisUpdateBlogButt = document.getElementById("UpdateBlogButt");
thisUpdateBlogButt.addEventListener("click", function () {
   var vstrChoice = 1;
   var vstrHeading = document.getElementById("strHeading").value;
   var vstrIntroduction = document.getElementById("strIntroduction").value;
   var vstrBody = document.getElementById("strBody").value;
   var dataString = '&vstrChoice=' + vstrChoice + '&vstrHeading=' + vstrHeading + '&vstrIntroduction=' + vstrIntroduction + '&vstrBody=' + vstrBody;
   $.ajax({
       type: "post",
       url: "/blog",
       data: dataString,
       cache: false,
       success: function (Response) {
           $('#UpdateBlogINFDIV').html(Response)
       }
   })
});
