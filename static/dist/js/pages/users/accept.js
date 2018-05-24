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

var thisAcceptInviteButt = document.getElementById("AcceptInviteButt");
    function ResendActivation() {
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
                    var vstrCell = document.getElementById('strCell').value;

                    var dataString = '&vstrChoice=' + vstrChoice + '&vstrCell=' + vstrCell +
                        '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAcceptToken=' + accessToken;

                    $.ajax({
                        type: "post",
                        url: "/admin/users/invites",
                        data: dataString,
                        cache: false,
                        success: function (html) {
                            $('#AcceptInviteINFDIV').html(html)
                        }
                    });

                })
            }
        })
    }

thisAcceptInviteButt.addEventListener("click", function () {
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
                var vstrNames = document.getElementById('strNames').value;
                var vstrSurname = document.getElementById('strSurname').value;
                var vstrCell = document.getElementById('strCell').value;
                var vstrEmail = document.getElementById('strEmail').value;
                var vstrSecurityCode = document.getElementById('strSecurityCode').value;

                var dataString = '&vstrChoice=' + vstrChoice + '&vstrCell=' + vstrCell + '&vstrNames=' + vstrNames +
                    '&vstrSurname=' + vstrSurname + '&vstrEmail=' + vstrEmail + '&vstrSecurityCode=' + vstrSecurityCode +
                '&vstrUserID=' + struid + '&vstrAcceptToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: "/admin/users/invites",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#AcceptInviteINFDIV').html(html)
                    }
                });
            })
        }
    })
});