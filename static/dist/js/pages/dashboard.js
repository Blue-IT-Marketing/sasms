var thisBlueITMarketingButt = document.getElementById("BlueITMarketingButt");
var thisContactMessagesButt = document.getElementById("ContactMessagesButt");
var thisBulkSMSButt = document.getElementById("BulkSMSButt");
var thisSendBulkSMSButt = document.getElementById("SendBulkSMSButt");
var thisAccountsButt = document.getElementById("AccountsButt");
var thisLeadsListButt = document.getElementById("LeadsListButt");
var thisSuportTicketsButt = document.getElementById("SuportTicketsButt");
var thisGlobalSentReportsButt = document.getElementById("GlobalSentReportsButt");
var thisClientTopUPButt = document.getElementById("ClientTopUPButt");
var thisEmailsButt = document.getElementById("EmailsButt");
var thisBlogButt = document.getElementById("BlogButt");
var thisFacebookButt = document.getElementById("FacebookButt");
var thisTwitterButt = document.getElementById("TwitterButt");

thisBlueITMarketingButt.addEventListener("click", function () {

    var vstrChoice = 1;
    var dataString = '&vstrChoice='+ vstrChoice ;
      $.ajax({
            type: "get",
            url: "/dashboard/blueitmarketing",
            data: dataString,
            cache: false,
          success: function(html){
            $('#dashboardINFDIV').html(html)
          }
      });
});
thisContactMessagesButt.addEventListener("click", function () {
    var vstrChoice = 1;
    var dataString = '&vstrChoice='+ vstrChoice ;
      $.ajax({
            type: "get",
            url: "/dashboard/contacts",
            data: dataString,
            cache: false,
          success: function(html){
            $('#dashboardINFDIV').html(html)
          }
      });
});
thisBulkSMSButt.addEventListener("click", function () {
    var vstrChoice = 1;
    var dataString = '&vstrChoice='+ vstrChoice ;
      $.ajax({
            type: "get",
            url: "/dashboard/bulksms",
            data: dataString,
            cache: false,
          success: function(html){
            $('#dashboardINFDIV').html(html)
          }
      });
});
thisSendBulkSMSButt.addEventListener("click", function () {
    var vstrChoice = 2;
    var dataString = '&vstrChoice='+ vstrChoice ;
    $.ajax({
        type: "post",
        url: "/dashboard/bulksms",
        data: dataString,
        cache: false,
      success: function(html){
        $('#dashboardINFDIV').html(html)
      }
    });
});
thisAccountsButt.addEventListener("click", function () {
var vstrChoice = 3;
var dataString = '&vstrChoice='+ vstrChoice ;
  $.ajax({
        type: "post",
        url: "/dashboard/bulksms",
        data: dataString,
        cache: false,
      success: function(html){
        $('#dashboardINFDIV').html(html)
      }
  });
});
thisLeadsListButt.addEventListener("click", function () {
var vstrChoice = 0;
var dataString = '&vstrChoice='+ vstrChoice ;
  $.ajax({
        type: "get",
        url: "/dashboard/advertise",
        data: dataString,
        cache: false,
      success: function(html){
        $('#dashboardINFDIV').html(html)
      }
  });
});
thisSuportTicketsButt.addEventListener("click", function () {
   var vstrChoice = 0;
   var dataString = '&vstrChoice=' + vstrChoice;
      $.ajax({
            type: "get",
            url: "/dashboard/tickets",
            data: dataString,
            cache: false,
          success: function(html){
            $('#dashboardINFDIV').html(html)
          }
      });

});
thisGlobalSentReportsButt.addEventListener("click", function () {
   var vstrChoice = 0;
   var dataString = '&vstrChoice=' + vstrChoice;
      $.ajax({
            type: "get",
            url: "/dashboard/globalreports",
            data: dataString,
            cache: false,
          success: function(html){
            $('#dashboardINFDIV').html(html)
          }
      });
});
thisClientTopUPButt.addEventListener("click", function () {
   var vstrChoice = 0;
   var dataString = '&vstrChoice=' + vstrChoice;

   $.ajax({
       type: "get",
       url: "/dashboard/topupverification",
       data: dataString,
       cache: false,
       success: function (Response) {
           $('#dashboardINFDIV').html(Response)
           
       }
   })
});
thisEmailsButt.addEventListener("click", function () {
    var vstrChoice = 0;
    var dataString = '&vstrChoice=' + vstrChoice;

   $.ajax({
       type: "get",
       url: "/dashboard/emails",
       data: dataString,
       cache: false,
       success: function (Response) {
           $('#dashboardINFDIV').html(Response)

       }
   })

});
thisBlogButt.addEventListener("click", function () {
   var vstrChoice = 0;
   var dataString = '&vstrChoice=' + vstrChoice;
   $.ajax({
       type: "post",
       url: "/blog",
       data: dataString,
       cache: false,
       success: function (Response) {
           $('#dashboardINFDIV').html(Response)
           
       }
   })
});
thisFacebookButt.addEventListener("click", function () {
   var vstrChoice = 0;
   var dataString = '&vstrChoice=' + vstrChoice;
   $.ajax({
       type: "get",
       url: "/dashboard/marketing",
       data: dataString,
       cache: false,
       success: function (Response) {
           $('#dashboardINFDIV').html(Response)

       }
   })

});
thisTwitterButt.addEventListener("click", function () {
   var vstrChoice = 1;
   var dataString = '&vstrChoice=' + vstrChoice;
   $.ajax({
       type: "get",
       url: "/dashboard/marketing",
       data: dataString,
       cache: false,
       success: function (Response) {
           $('#dashboardINFDIV').html(Response)

       }
   })
});