
try{
var config =
{
    apiKey: "AIzaSyBhNkqMr7zXi4r_bToSFiqPQ8BQLja47_g",
    authDomain: "sa-sms-b.firebaseapp.com",
    databaseURL: "https://sa-sms-b.firebaseio.com",
    projectId: "sa-sms-b",
    storageBucket: "sa-sms-b.appspot.com",
    messagingSenderId: "3221236137"
};
if (!firebase.apps.length) {
    firebase.initializeApp(config);
}else {
}

}catch (error){

}
var thisCreditAccountButt = document.getElementById("CreditAccountButt");

function CreateQuote(clicked_id) {
    var vstrSMSAmount = parseInt(document.getElementById(clicked_id).value);
    var vstrBudgetSystemCredit = parseInt(document.getElementById('strBudgetSystemCredit').value);
    var vstrVodacomSystemCredit = parseInt(document.getElementById('strVodacomSystemCredit').value);
    var vstrBudgetSellPrice = parseInt(document.getElementById('strBudgetSellPrice').value);
    var vstrVodacomSellPrice = parseInt(document.getElementById('strVodacomSellPrice').value);
    if (vstrSMSAmount <= vstrBudgetSystemCredit){
        document.getElementById('strDepositAmount').value = ((vstrBudgetSellPrice)/100) * vstrSMSAmount;
    }else{
        document.getElementById('strDepositAmount').value = ((vstrVodacomSellPrice)/100) * vstrSMSAmount;
    }
}
thisCreditAccountButt.addEventListener("click", function () {

    firebase.auth().onAuthStateChanged(function (user) {
        if (user) {
            user.getIdToken().then(function (accessToken) {
                // User is signed in.
                var displayName = user.displayName;
                var email = user.email;
                var photoURL = user.photoURL;
                var isAnonymous = user.isAnonymous;
                var providerData = user.providerData;
                var struid = user.uid;

                var vstrChoice = 0;
                var vstrSMSPackages = document.getElementById('strSMSPackages').value;
                var vstrDepositAmount = document.getElementById('strDepositAmount').value;
                var vstrDepositMethod = document.getElementById('strDepositMethod').value;
                var vstrOrganizationID = document.getElementById('strOrganizationID').value;
                var thisURL = "/sms/credits";
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrOrganizationID=' + vstrOrganizationID +
                    '&vstrSMSPackages=' + vstrSMSPackages + '&vstrDepositAmount=' + vstrDepositAmount +
                    '&vstrDepositMethod=' + vstrDepositMethod + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: thisURL,
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#AccountDeposit').html(html)
                    }
                });

            })
        }
    })
});