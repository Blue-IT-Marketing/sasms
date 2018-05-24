/**
 * Handler Script for /adverts/sub/addmanager.html
 * @type {Element}
 */
  // Initialize Firebase
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
var thisResponsesButt = document.getElementById("ResponsesButt");
var thisPaymentsButt = document.getElementById("PaymentsButt");
//Advert Butt Event Listener
thisAdvertButt.addEventListener("click",function () {
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
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrAdvertID=' + vstrAdvertID +
                    '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
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
        }else{
            alert("Please login to access your adverts")
        }
    })
});
//MyStatsButt event Listener
thisMyStatsButt.addEventListener("click",function () {
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
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrAdvertID=' + vstrAdvertID +
                    '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
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
        }else{
            alert("Please login to access your Advert Statistics")
        }
    })
});

//ResponseButt event Listener
thisResponsesButt.addEventListener("click",function() {
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

                var vstrChoice = 3;
                var vstrAdvertID = document.getElementById('strAdvertID').value;
                var thisURL = "/adverts/manage/" + vstrAdvertID;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrAdvertID=' + vstrAdvertID +
                    '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
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
        }else{
            alert("Please login to access your advert responses")
        }
    })
});
//PaymentsButt Event Listener
thisPaymentsButt.addEventListener("click",function() {
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

                var vstrChoice = 4;
                var vstrAdvertID = document.getElementById('strAdvertID').value;
                var thisURL = "/adverts/manage/" + vstrAdvertID;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrAdvertID=' + vstrAdvertID +
                    '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
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
        }else{
            alert("Please login to access your advert payments")
        }
    })
});