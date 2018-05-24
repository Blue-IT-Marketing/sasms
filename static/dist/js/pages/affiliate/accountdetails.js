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

var thisCheckLinkButt = document.getElementById("CheckLinkButt");
var thisUpdateAffiliateAccountButt = document.getElementById("UpdateAffiliateAccountButt");

thisCheckLinkButt.addEventListener("click", function () {
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
                var vstrAffiliateLink = document.getElementById('strAffiliateLink').value;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrAffiliateLink=' + vstrAffiliateLink + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;

                $.ajax({
                    type: "post",
                    url: "/affiliates",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        if (html == "YES") {
                            document.getElementById('CheckLinkButt').classList.remove('btn-danger');
                            document.getElementById('CheckLinkButt').classList.remove('btn-default');
                            document.getElementById('CheckLinkButt').classList.add('btn-info');
                            document.getElementById('CheckLinkButt').innerHTML = "";
                            document.getElementById('CheckLinkButt').innerHTML = "<strong> Link Available </strong>";
                        } else {
                            document.getElementById('CheckLinkButt').classList.remove('btn-info');
                            document.getElementById('CheckLinkButt').classList.remove('btn-default');
                            document.getElementById('CheckLinkButt').classList.add('btn-danger');
                            document.getElementById('CheckLinkButt').innerHTML = "<strong>Link Already Taken</strong>";
                        }
                    }
                });
            })
        }
    })
});


thisUpdateAffiliateAccountButt.addEventListener("click", function () {
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
                var vstrAffiliateLink = document.getElementById('strAffiliateLink').value;
                var vstrPaymentMethod = document.getElementById('strPaymentMethod').value;

                var dataString = '&vstrChoice=' + vstrChoice + '&vstrAffiliateLink=' + vstrAffiliateLink +
                    '&vstrPaymentMethod=' + vstrPaymentMethod + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: "/affiliates",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#UpdateAffiliateINFDIV').html(html)
                    }
                });
            })
        }
    })
});


