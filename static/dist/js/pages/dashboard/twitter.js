var thisAddTwitterMessageButt = document.getElementById("AddTwitterMessageButt");
var thisAddTwitterSettingsButt = document.getElementById("AddTwitterSettingsButt");
thisAddTwitterMessageButt.addEventListener("click", function () {
    var vstrChoice = 2;
    var vstrMessage = document.getElementById("strMessage").value;
    var dataString = '&vstrChoice=' + vstrChoice + '&vstrMessage=' + vstrMessage;
    $.ajax({
        type: "post",
        url: "/dashboard/marketing",
        data: dataString,
        cache: false,
        success: function (Response) {
            $('#AddTwitterMessageINFDIV').html(Response)
            }
        })
});
function ShowTwitterMessage(messageid){
    var vstrChoice = 3;
    var dataString = '&vstrChoice=' + vstrChoice + '&vstrMessageID=' + messageid;
    $.ajax({
        type: "post",
        url: "/dashboard/marketing",
        data: dataString,
        cache: false,
        success: function (Response) {
            $('#AddFacebookMessageINFDIV').html(Response)
            }
        })
}
thisAddTwitterSettingsButt.addEventListener("click", function () {
   var vstrChoice = 4;
   var vstrConsumerAPI = document.getElementById("strConsumerAPI").value;
   var vstrConsumerSecret = document.getElementById("strConsumerSecret").value;
   var vstrAccessTokenKey = document.getElementById("strAccessTokenKey").value;
   var vstrAccessTokenSecret = document.getElementById("strAccessTokenSecret").value;
   var dataString = '&vstrChoice=' + vstrChoice + '&vstrConsumerAPI=' + vstrConsumerAPI + '&vstrConsumerSecret=' + vstrConsumerSecret +
       '&vstrAccessTokenKey=' + vstrAccessTokenKey + '&vstrAccessTokenSecret=' + vstrAccessTokenSecret;
    $.ajax({
        type: "post",
        url: "/dashboard/marketing",
        data: dataString,
        cache: false,
        success: function (Response) {
            $('#AddTwitterSettingsINFDIV').html(Response)
            }
        })

});