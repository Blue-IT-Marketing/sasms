/**
 * Handler Script for adverts/sub/payments.html
 *
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



var thisAdvertButt = document.getElementById("AdvertButt");
var thisMyStatsButt = document.getElementById("MyStatsButt");
var thisCreateNewOrderButt = document.getElementById("CreateNewOrderButt");
var thisCreatePaymentRequestButt = document.getElementById("CreatePaymentRequestButt");
//AdvertButt Handler
thisAdvertButt.addEventListener("click",function() {


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
                var vstrAdvertID = document.getElementById('strAdvertID').value;
                var thisURL = "/adverts/manage/" + vstrAdvertID;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrAdvertID=' + vstrAdvertID + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: thisURL,
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#AdvertiseINFDIV').html(html)
                    }
                });
            })
        }
    })
});


//My Stats handler

thisMyStatsButt.addEventListener("click", function () {

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

                var vstrChoice = 2;
                var vstrAdvertID = document.getElementById('strAdvertID').value;
                var thisURL = "/adverts/manage/" + vstrAdvertID;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrAdvertID=' + vstrAdvertID + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: thisURL,
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#AdvertiseINFDIV').html(html)
                    }
                });
            })
        }
    })
});


thisCreateNewOrderButt.addEventListener("click", function () {
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

                var vstrChoice = 5;
                var vstrAdvertID = document.getElementById('strAdvertID').value;
                var vstrPackage = document.getElementById('strPackage').value;
                var vstrStartDate = document.getElementById('strStartDate').value;
                var vstrStartTime = document.getElementById('strStartTime').value;

                var thisURL = "/adverts/manage/" + vstrAdvertID;

                var dataString = '&vstrChoice=' + vstrChoice + '&vstrAdvertID=' + vstrAdvertID + '&vstrPackage=' + vstrPackage +
                    '&vstrStartDate=' + vstrStartDate + '&vstrStartTime=' + vstrStartTime + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: thisURL,
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#CreateNewOrderINFDIV').html(html)
                    }
                });
            })
        }
    })
});

thisCreatePaymentRequestButt.addEventListener("click", function () {
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

                var vstrChoice = 6;
                var vstrTotalCredits = document.getElementById("strTotalCredits").value;
                var vstrAdvertID = document.getElementById('strAdvertID').value;
                var vstrSelectOrder = document.getElementById('strSelectOrder').value;
                var vstrPaymentMethod = document.getElementById('strPaymentMethod').value;

                var thisURL = "/adverts/manage/" + vstrAdvertID;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrAdvertID=' + vstrAdvertID + '&vstrSelectOrder=' + vstrSelectOrder +
                    '&vstrPaymentMethod=' + vstrPaymentMethod + '&vstrTotalCredits=' + vstrTotalCredits + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: thisURL,
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        var newWindow = window.open("", "new window", "width=1024, height=800");
                        //write the data to the document of the newWindow
                        newWindow.document.write(html);
                    }
                });
            })
        }
    })
});
