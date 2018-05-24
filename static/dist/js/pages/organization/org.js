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
}catch (err){

}

var thisUpdateOrganizationButt = document.getElementById("UpdateOrganizationButt");
var thisUpdatePaymentDetailsButt = document.getElementById("UpdatePaymentDetailsButt");
thisUpdateOrganizationButt.addEventListener('click', function () {
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
                    var vstrOrganization = document.getElementById('strOrganization').value;
                    var vstrDescription = document.getElementById('strDescription').value;
                    var vstrRegistration = document.getElementById('strRegistration').value;
                    var vstrCell = document.getElementById('strCell').value;
                    var vstrTel = document.getElementById('strTel').value;

                    var vstrWebsite = document.getElementById('strWebsite').value;
                    var dataString = '&vstrChoice=' + vstrChoice + '&vstrOrganization=' + vstrOrganization + '&vstrDescription=' + vstrDescription +
                        '&vstrRegistration=' + vstrRegistration + '&vstrCell=' + vstrCell + '&vstrTel=' + vstrTel  +
                        '&vstrWebsite=' + vstrWebsite + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                    $.ajax({
                        type: "post",
                        url: "/admin/org",
                        data: dataString,
                        cache: false,
                        success: function (html) {
                            $('#UpdateOrganizationINFDIV').html(html)
                        }
                    });
                })
            }
        })
});

thisUpdatePaymentDetailsButt.addEventListener('click', function () {
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

                    var vstrChoice = 1;
                    var vstrAccountHolder = document.getElementById('strAccountHolder').value;
                    var vstrAccountNumber = document.getElementById('strAccountNumber').value;
                    var vstrAccountType = document.getElementById('strAccountType').value;
                    var vstrBankName = document.getElementById('strBankName').value;
                    var vstrBranchName = document.getElementById('strBranchName').value;
                    var vstrBranchCode = document.getElementById('strBranchCode').value;

                    var dataString = '&vstrChoice=' + vstrChoice + '&vstrAccountHolder=' + vstrAccountHolder + '&vstrAccountNumber=' + vstrAccountNumber +
                        '&vstrAccountType=' + vstrAccountType + '&vstrBankName=' + vstrBankName + '&vstrBranchName=' + vstrBranchName + '&vstrBranchCode=' + vstrBranchCode +
                        '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                    $.ajax({
                        type: "post",
                        url: "/admin/org",
                        data: dataString,
                        cache: false,
                        success: function (html) {
                            $('#PaymentDetailsINFDIV').html(html)
                        }
                    })
                })
            }
        })
});