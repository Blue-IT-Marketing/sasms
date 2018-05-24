
function isEmpty(a){
if (a == null || a ==''){
    return true;
}else{
    return false;
}
}

var thisUploadContactButt = document.getElementById("UploadContactButt");
var thisBulkUploadContactsButt = document.getElementById("BulkUploadContactsButt");
var thisRemoveButt = document.getElementById("RemoveButt");
var thisUploadPartnerButt = document.getElementById("UploadPartnerButt");
var thisUploadEndPointButt = document.getElementById("UploadEndPointButt");
thisUploadContactButt.addEventListener("click", function () {
var vstrChoice = 0;
var vstrNames = document.getElementById('strNames').value;
var vstrSurname = document.getElementById('strSurname').value;
var vstrCellNumber = document.getElementById('strCellNumber').value;
var vstrEmail = document.getElementById('strEmail').value;
var thisURL = "/dashboard/advertise";
var dataString = '&vstrChoice='+ vstrChoice + '&vstrNames=' + vstrNames + '&vstrSurname=' + vstrSurname +
        '&vstrCellNumber=' + vstrCellNumber +'&vstrEmail=' + vstrEmail;
  $.ajax({
        type: "post",
        url:thisURL,
        data: dataString,
        cache: false,
      success: function(html){
        $('#UploadContactINFDIV').html(html)
      }
  });
});
thisBulkUploadContactsButt.addEventListener("click", function () {
    var vstrChoice = 1;
    //var vstrContactList = $('strContacts').val().split('\n');
    var vstrContactList = document.getElementById('strContacts').value;
    alert(vstrContactList);
    var vstrContactList = vstrContactList.split('\n');
    var vstrThisContactList = "";
    for (thisContact in vstrContactList){
        if (isEmpty(vstrThisContactList) === true){
            vstrThisContactList= vstrContactList[thisContact];
        }else{
            vstrThisContactList = vstrThisContactList + "|" + vstrContactList[thisContact];
        }
    }
    var thisURL = "/dashboard/advertise";
    var dataString = '&vstrChoice='+ vstrChoice + '&vstrContacts=' + vstrThisContactList;
      $.ajax({
            type: "post",
            url:thisURL,
            data: dataString,
            cache: false,
          success: function(html){
            $('#BulkUploadContactsINFDIV').html(html)
          }
      });
});
thisRemoveButt.addEventListener("click", function () {
var vstrChoice = 2;
var vstrRemoveCell = document.getElementById('strRemoveCell').value;
var thisURL = "/dashboard/advertise";
var dataString = '&vstrChoice='+ vstrChoice + '&vstrRemoveCell=' + vstrRemoveCell;
  $.ajax({
        type: "post",
        url:thisURL,
        data: dataString,
        cache: false,
      success: function(html){
        $('#RemoveContactINFDIV').html(html)
      }
  });
});
thisUploadPartnerButt.addEventListener("click", function () {
    var vstrChoice = 3;
    var vstrPartnerURL = document.getElementById('strPartnerURL').value;
    var thisURL = "/dashboard/advertise";
    var dataString = '&vstrChoice='+ vstrChoice + '&vstrPartnerURL=' + vstrPartnerURL;
      $.ajax({
            type: "post",
            url:thisURL,
            data: dataString,
            cache: false,
          success: function(html){
            $('#UploadPartnerINFDIV').html(html)
          }
      });

});
thisUploadEndPointButt.addEventListener("click", function () {
var vstrChoice = 4;
var vstrEndpoint = document.getElementById('strEndpoint').value;
var thisURL = "/dashboard/advertise";
var dataString = '&vstrChoice='+ vstrChoice + '&vstrEndpoint=' + vstrEndpoint;
  $.ajax({
        type: "post",
        url:thisURL,
        data: dataString,
        cache: false,
      success: function(html){
        $('#UploadEndPointINFDIV').html(html)
      }
  });
});