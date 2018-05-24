try {
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


}
catch (err){

}
var thisContactsButt = document.getElementById("ContactsButt");
var thisCreateGroupMessageButt = document.getElementById("CreateGroupMessageButt");
var thisEditSMSGroupButt = document.getElementById("EditSMSGroupButt");
var thisDeleteSMSGroupButt = document.getElementById("DeleteSMSGroupButt");
var thisMessageDeliveryReports = document.getElementById("MessageDeliveryReports");

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

                var vstrChoice = 0;
                var vstrGroupID = document.getElementById('strGroupID').value;
                var thisURL = "/sms/groupman/" + vstrGroupID;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrGroupID=' + vstrGroupID  + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: thisURL,
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#GroupSMSINFDIV').html(html)
                    }
                });

            })
        }
    })
});

thisCreateGroupMessageButt.addEventListener("click", function () {
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
                var vstrGroupID = document.getElementById('strGroupID').value;
                var thisURL = "/sms/groupman/" + vstrGroupID;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrGroupID=' + vstrGroupID + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: thisURL,
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#GroupSMSINFDIV').html(html)
                    }
                });

            })
        }
    })
});
thisEditSMSGroupButt.addEventListener("click", function () {
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
                var vstrGroupID = document.getElementById('strGroupID').value;
                var thisURL = "/sms/groupman/" + vstrGroupID;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrGroupID=' + vstrGroupID + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: thisURL,
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#GroupSMSINFDIV').html(html)
                    }
                });
            })
        }
    })
});
thisDeleteSMSGroupButt.addEventListener("click", function () {

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
                var vstrGroupID = document.getElementById('strGroupID').value;
                var thisURL = "/sms/groupman/" + vstrGroupID;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrGroupID=' + vstrGroupID + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: thisURL,
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#GroupSMSINFDIV').html(html)
                    }
                });
            })
        }
    })
});
thisMessageDeliveryReports.addEventListener("click", function () {

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

                var vstrChoice = 10;
                var vstrGroupID = document.getElementById('strGroupID').value;
                var thisURL = "/sms/groupman/" + vstrGroupID;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrGroupID=' + vstrGroupID + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: thisURL,
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#GroupSMSINFDIV').html(html)
                    }
                });
            })
        }
    })
});

