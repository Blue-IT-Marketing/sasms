var thisLoadDepositSlipButt = document.getElementById("LoadDepositSlipButt");
var thisAddCreditsButt = document.getElementById("AddCreditsButt");


thisLoadDepositSlipButt.addEventListener("click", function () {
    var vstrChoice = 0;
    var vstrDepositSlipFilename = document.getElementById("strDepositSlipFilename").value;
    var vstrTopUpReference = document.getElementById("strTopUpReference").value;
    var dataString = '&vstrChoice=' + vstrChoice + '&vstrDepositSlipFilename=' + vstrDepositSlipFilename + '&vstrTopUpReference=' + vstrTopUpReference;
    $.ajax({
        type: "post",
        url: "/dashboard/topup/" + vstrTopUpReference,
        data: dataString,
        cache: false,
        success: function(Response){
            $('#LoadDepositSlipINFDIV').html(Response)
    }
    });
});
thisAddCreditsButt.addEventListener("click", function () {
    var vstrChoice = 1;
    var vstrTopUpReference = document.getElementById("strTopUpReference").value;
    var vstrAccountName = document.getElementById("strAccountName").value;
    var dataString = '&vstrChoice=' + vstrChoice + '&vstrTopUpReference=' + vstrTopUpReference + '&vstrAccountName=' + vstrAccountName;
    $.ajax({
        type: "post",
        url: "/dashboard/topup/" + vstrTopUpReference,
        data: dataString,
        cache: false,
        success: function(Response){
            $('#AddCreditsINFDIV').html(Response)
        }
    })
});