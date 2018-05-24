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
var thisCreditsButt = document.getElementById('CreditsButt');
var thisAccountDetailsButt = document.getElementById('AccountDetailsButt');
var thisStatisticsButt = document.getElementById('StatisticsButt');
var thisShareLinksButt = document.getElementById('ShareLinksButt');

thisCreditsButt.addEventListener("click", function () {
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
                    url: "/affiliates",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#AffiliateINFDIV').html(html)
                    }
                });
            })
        }else{
            alert("Please login to access your affiliate credits information")
        }
    })
});

thisAccountDetailsButt.addEventListener("click", function () {
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
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: "/affiliates",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#AffiliateINFDIV').html(html)
                    }
                });
            })
        }else{
            alert("Please login to access your affiliate account")
        }
    })
});

thisStatisticsButt.addEventListener("click", function () {
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
                var dataString = '&vstrChoice=' + vstrChoice  + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: "/affiliates",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#AffiliateINFDIV').html(html)
                    }
                });
            })
        }else{
            alert("Please login to access your statistics")
        }
    })
});
thisShareLinksButt.addEventListener("click", function () {
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
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: "/affiliates",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#AffiliateINFDIV').html(html)
                    }
                });
            })
        }else{
            alert("Please login to access your social page")
        }
    })
});

function AffiliateSubMenu() {
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


                var vstrChoice = 9;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: "/affiliates",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#AffiliateSubMenuINFDIV').html(html)
                    }
                });
            })
        }
    })
}