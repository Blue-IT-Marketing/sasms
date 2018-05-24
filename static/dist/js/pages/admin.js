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


var thisContactButt = document.getElementById("ContactsButt");
var thisSendReceiveSMSButt = document.getElementById("SendReceiveSMSButt");
var thisOrganizationDetailsButt = document.getElementById("OrganizationDetailsButt");
var thisManageUsersButt = document.getElementById("ManageUsersButt");
var thisAccountButt = document.getElementById("AccountButt");

thisContactButt.addEventListener("click",function () {
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
        }
    })
});

thisSendReceiveSMSButt.addEventListener("click",function(){
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
    }
})});

thisOrganizationDetailsButt.addEventListener("click",function() {
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
        }
    })
});

thisManageUsersButt.addEventListener("click",function(){
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
        }
    })
});

thisAccountButt.addEventListener("click",function() {
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
        }
    })

});
//AdminMenuINFDIV
function LoadMenu(){
  firebase.auth().onAuthStateChanged(function(user) {
    if (user)
    {
    user.getIdToken().then(function(accessToken) {
        // User is signed in.
        var displayName = user.displayName;
        var email = user.email;
        var photoURL = user.photoURL;
        var isAnonymous = user.isAnonymous;
        var providerData = user.providerData;
        var struid = user.uid;

        var dataString = "vstrUserID=" + struid + '&vstrUserEmail=' + email + '&vstraccessToken=' + accessToken;
           $.ajax({
               type: "post",
               url: "/admin",
               data: dataString,
               cache: false,
               success: function(html){$('#AdminMenuINFDIV').html(html)}});
    })}});

}


