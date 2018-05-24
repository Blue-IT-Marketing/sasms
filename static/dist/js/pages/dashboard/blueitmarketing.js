var thisUpdateEmployeeButt = document.getElementById("UpdateEmployeeButt");
var thisUpdateConsultantButt = document.getElementById("UpdateConsultantButt");
var thisUpdateBankDetailsButt = document.getElementById("UpdateBankDetailsButt");
var thisUpdateSMSAccountButt = document.getElementById("UpdateSMSAccountButt");

thisUpdateEmployeeButt.addEventListener("click", function () {
    var vstrChoice =0;
    var vstrNames = document.getElementById('strNames').value;
    var vstrSurname = document.getElementById('strSurname').value;
    var vstrCell = document.getElementById('strCell').value;
    var vstrTel = document.getElementById('strTel').value;
    var vstrEmail = document.getElementById('strEmail').value;
    var vstrPosition = document.getElementById('strPosition').value;
    var vstrSendNotices = document.getElementById('strSendNotices').value;
    var dataString = '&vstrChoice='+ vstrChoice + '&vstrNames=' + vstrNames + '&vstrSurname=' + vstrSurname +
        '&vstrCell=' + vstrCell + '&vstrTel=' + vstrTel + '&vstrEmail=' + vstrEmail + '&vstrPosition=' + vstrPosition +
        '&vstrSendNotices=' + vstrSendNotices;
      $.ajax({
            type: "post",
            url: "/dashboard/blueitmarketing",
            data: dataString,
            cache: false,
          success: function(html){
            $('#UpdateEmployeeINFDIV').html(html)
          }
      });
});
thisUpdateConsultantButt.addEventListener("click", function () {
    var vstrChoice =1;
    var vstrConsNames = document.getElementById('strConsNames').value;
    var vstrConsSurname = document.getElementById('strConsSurname').value;
    var vstrConsCell = document.getElementById('strConsCell').value;
    var vstrConsTel = document.getElementById('strConsTel').value;
    var vstrConsEmail = document.getElementById('strConsEmail').value;
    var vstrConsPosition = document.getElementById('strConsPosition').value;
    var vstrConsSendNotices = document.getElementById('strConsSendNotices').value;
    var dataString = '&vstrChoice='+ vstrChoice + '&vstrConsNames=' + vstrConsNames + '&vstrConsSurname=' + vstrConsSurname +
        '&vstrConsCell=' + vstrConsCell + '&vstrConsTel=' + vstrConsTel + '&vstrConsEmail=' + vstrConsEmail + '&vstrConsPosition=' + vstrConsPosition +
        '&vstrConsSendNotices=' + vstrConsSendNotices;
      $.ajax({
            type: "post",
            url: "/dashboard/blueitmarketing",
            data: dataString,
            cache: false,
          success: function(html){
            $('#UpdateConsultantINFDIV').html(html)
          }
      });
});
thisUpdateBankDetailsButt.addEventListener("click",function () {
    var vstrChoice =2;
    var vstrAccountHolder = document.getElementById('strAccountHolder').value;
    var vstrAccountNumber = document.getElementById('strAccountNumber').value;
    var vstrBankName = document.getElementById('strBankName').value;
    var vstrBranchName = document.getElementById('strBranchName').value;
    var vstrBranchCode = document.getElementById('strBranchCode').value;
    var dataString = '&vstrChoice='+ vstrChoice + '&vstrAccountHolder=' + vstrAccountHolder + '&vstrAccountNumber=' + vstrAccountNumber +
        '&vstrBankName=' + vstrBankName + '&vstrBranchName=' + vstrBranchName + '&vstrBranchCode=' + vstrBranchCode;

      $.ajax({
            type: "post",
            url: "/dashboard/blueitmarketing",
            data: dataString,
            cache: false,
          success: function(html){
            $('#UpdateBankDetailINFDIV').html(html)
          }
      });
});
thisUpdateSMSAccountButt.addEventListener("click", function () {
    var vstrChoice =3;
    var vstrTotalSMS = document.getElementById('strTotalSMS').value;
    var vstrPortal = document.getElementById('strPortal').value;
    var dataString = '&vstrChoice='+ vstrChoice + '&vstrTotalSMS=' + vstrTotalSMS + '&vstrPortal=' + vstrPortal;
      $.ajax({
            type: "post",
            url: "/dashboard/blueitmarketing",
            data: dataString,
            cache: false,
          success: function(html){
            $('#UpdateSMSAccountINFDIV').html(html)
          }
      });
});