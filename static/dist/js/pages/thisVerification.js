/**
 * Verification Event Handler
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
var thisContactsButt = document.getElementById("ContactsButt");
var thisSendReceiveSMSButt = document.getElementById("SendReceiveSMSButt");
var thisOrganizationDetailsButt = document.getElementById("OrganizationDetailsButt");
var thisManageUsersButt = document.getElementById("ManageUsersButt");
var thisAccountButt = document.getElementById("AccountButt");
var thisVerifyAccountButt = document.getElementById("VerifyAccountButt");

thisContactsButt.addEventListener("click", function () {
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
                    type: "get",
                    url: "/admin/contacts",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#SMSAdminINFDIV').html(html)
                    }
                });
            })
        }else{
            alert("Please login to continue")
        }
    })
});
thisSendReceiveSMSButt.addEventListener("click", function () {
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
                    type: "get",
                    url: "/admin/mysms",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#SMSAdminINFDIV').html(html)
                    }
                });
            })
        }else{
            alert("Please login before you access your SMS Messages")
        }
    })
});
thisOrganizationDetailsButt.addEventListener("click", function () {
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
                    type: "get",
                    url: "/admin/org",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#SMSAdminINFDIV').html(html)
                    }
                });
            })
        }else{
            alert("Please login before you access your organization details")
        }
    })
});

thisManageUsersButt.addEventListener("click", function () {
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
                    type: "get",
                    url: "/admin/users",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#SMSAdminINFDIV').html(html)
                    }
                });
            })
        }else{
            alert("Please login before you manage your Users")
        }
    })
});

thisAccountButt.addEventListener("click", function () {
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
                    type: "get",
                    url: "/admin/sms/groups",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#SMSAdminINFDIV').html(html)
                    }
                });
            })
        }else{
            alert("Please login before you access your account")
        }
    })
});

thisVerifyAccountButt.addEventListener("click", function () {
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
                var vstrRegLink = document.getElementById('strRegLink').value;
                var vstrVerificationCode = document.getElementById('strVerificationCode').value;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrRegLink=' + vstrRegLink + '&vstrVerificationCode=' + vstrVerificationCode +
                      '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;

                $.ajax({
                    type: "post",
                    url: "/org/reg/" + vstrRegLink,
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#VerificationResponseINFDIV').html(html)
                    }
                });
            })
        }else{
            alert("Please login before you verify your account")
        }
    })
});