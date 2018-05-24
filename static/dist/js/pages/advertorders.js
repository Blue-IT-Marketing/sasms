/**
 * Advert Orders Event Handler
 * @type {Element}
 */
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

var thisUploadPaymentButt = document.getElementById("UploadPaymentButt");
thisUploadPaymentButt.addEventListener("click", function () {
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
                var vstrDepositReference = document.getElementById('strDepositReference').value;
                var vstrAmount = document.getElementById('strAmount').value;
                var vstrPaymentMethod = document.getElementById('strPaymentMethod').value;
                var thisURL = "/org/advaccounts/" + vstrDepositReference;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrAmount=' + vstrAmount +
                    '&vstrPaymentMethod=' + vstrPaymentMethod + '&vstrDepositReference=' + vstrDepositReference +
                    '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: thisURL,
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#UploadPaymentINFDIV').html(html)
                    }
                });
            })
        }else{
            alert("Please login to upload your payment")
        }
    })
});
