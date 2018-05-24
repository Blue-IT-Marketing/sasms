var thisAddFacebookMessageButt = document.getElementById("AddFacebookMessageButt");
thisAddFacebookMessageButt.addEventListener("click", function () {
    var vstrChoice = 0;
    var vstrMessage = document.getElementById("strMessage").value;
    var dataString = '&vstrChoice=' + vstrChoice + '&vstrMessage=' + vstrMessage;
    $.ajax({
        type: "post",
        url: "/dashboard/marketing",
        data: dataString,
        cache: false,
        success: function (Response) {
            $('#AddFacebookMessageINFDIV').html(Response)
            }
        })
});
function ShowMessage(messageID){
    var vstrChoice = 1;
    var dataString = '&vstrChoice=' + vstrChoice + '&vstrMessageID=' + messageID;
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