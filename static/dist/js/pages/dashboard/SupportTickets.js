var thisSendMessageButt = document.getElementById('SendMessageButt');
function ShowTicket(strUserID){
        var vstrChoice = 0;
        var dataString = '&vstrUserID=' + strUserID + '&vstrChoice=' + vstrChoice;
      $.ajax({
            type: "post",
            url: '/dashboard/tickets',
            data: dataString,
            cache: false,
          success: function(html){
            $('#TicketSystemINFDIV').html(html)
          }
      });
}

thisSendMessageButt.addEventListener("click", function () {
    var vstrChoice = 1;
    var vstrComment = document.getElementById('strComment');
    var vstrTicketID = document.getElementById('strTicketID');
    var vstrThreadID = document.getElementById('strThreadID');
    var vstrUserID = document.getElementById('strUserID');
    var dataString = '&vstrChoice=' + vstrChoice + '&vstrComment=' + vstrComment + '&vstrTicketID=' + vstrTicketID + '&vstrThreadID=' + vstrThreadID +
    '&vstrUserID=' + vstrUserID;
    $.ajax({
            type: "post",
            url: "/dashboard/tickets",
            data: dataString,
            cache: false,
          success: function(html){
            $('#TicketSystemINFDIV').html(html);
                setInterval(UpdateChat,1000);
            }

    });
});



