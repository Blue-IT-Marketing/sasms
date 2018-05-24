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
}catch (err) {
}
var thisAccountButt = document.getElementById("AccountButt");
var thisMyAdvertsButt = document.getElementById("MyAdvertsButt");
var thisOrdersButt = document.getElementById("OrdersButt");
var thisInvoicesButt = document.getElementById("InvoicesButt");
//AccountButt Event Listener
thisAccountButt.addEventListener("click",function () {
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
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: "/advertise",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#AdvertiseINFDIV').html(html)
                    }
                });
            })
        }else{
            alert("Please login to create adverts..")
        }
    })
});
// My Adverts Event Listener
thisMyAdvertsButt.addEventListener("click", function () {
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
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: "/advertise",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#AdvertiseINFDIV').html(html)
                    }
                });
            })
        }else{
            alert("Please login to open my adverts")
        }
    })
});
// Orders Butt Event Listener
thisOrdersButt.addEventListener("click", function () {
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
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: "/advertise",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#AdvertiseINFDIV').html(html)
                    }
                });
            })
        }else{
            alert("Please login to access your orders")
        }
    })
});
// Invoice Butt Event Listener
thisInvoicesButt.addEventListener("click", function () {
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
                var dataString = '&vstrChoice=' + vstrChoice  + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: "/advertise",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#AdvertiseINFDIV').html(html)
                    }
                });
            })
        }else{
            alert("Please login to access your Invoices")
        }
    })
});

function LoadAdvertiseSubMenu() {
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

                var vstrChoice = 7;
                var dataString = '&vstrChoice=' + vstrChoice  + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: "/advertise",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#AdvertiseSubMenuINFDIV').html(html)
                    }
                });
            })
        }
    })
}