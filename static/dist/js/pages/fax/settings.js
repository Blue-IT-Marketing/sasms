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

var thisGetFaxNumberButt = document.getElementById("GetFaxNumberButt");
thisGetFaxNumberButt.addEventListener("click", function () {

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
                    url: "/fax/settings",
                    data: dataString,
                    cache: false,
                    success: function (Response) {
                        document.getElementById("strFaxNumber").value = Response;
                    }
                })
            })
        }
    })
});

var thisCreateEmailToFaxButt = document.getElementById("CreateEmailToFaxButt");
thisCreateEmailToFaxButt.addEventListener("click", function () {
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
                    url: "/fax/settings",
                    data: dataString,
                    cache: false,
                    success: function (Response) {
                        document.getElementById("strEmailToFax").value = Response;
                    }
                })

            })
        }
    })
});

var thisCreateAPIKeyButt = document.getElementById("CreateAPIKeyButt");
thisCreateAPIKeyButt.addEventListener("click", function () {
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
                    url: "/fax/settings",
                    data: dataString,
                    cache: false,
                    success: function (Response) {
                        document.getElementById("strAPIKey").value = Response;
                    }
                })
            })
        }
    })
});

var thisCreateSecretCodeButt = document.getElementById("CreateSecretCodeButt");
thisCreateSecretCodeButt.addEventListener("click", function () {
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
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: "/fax/settings",
                    data: dataString,
                    cache: false,
                    success: function (Response) {
                        document.getElementById("strSecretCode").value = Response;
                    }
                })
            })
        }
    })
});

var thisUpdateSettingsButt = document.getElementById("UpdateSettingsButt");
thisUpdateSettingsButt.addEventListener("click", function () {
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
                var vstrFaxNumber = document.getElementById("strFaxNumber").value;

                var vstrSMSNotifyOnSend = "NO";
                if (document.getElementById("strSMSNotifyOnSend").checked === true) {
                    vstrSMSNotifyOnSend = "YES";
                }
                var vstrSMSCreditNotify = "NO";
                if (document.getElementById("strSMSCreditNotify").checked === true) {
                    vstrSMSCreditNotify = "YES";
                }

                var vstrSMSNotifyOnReceive = "YES";
                if (document.getElementById("strSMSNotifyOnReceive").checked === true) {
                    vstrSMSNotifyOnReceive = "YES";
                }

                var vstrEmailToFax = document.getElementById("strEmailToFax").value;
                var vstrAPIKey = document.getElementById("strAPIKey").value;
                var vstrSecretCode = document.getElementById("strSecretCode").value;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrFaxNumber=' + vstrFaxNumber + '&vstrSMSNotifyOnSend=' + vstrSMSNotifyOnSend +
                    '&vstrSMSCreditNotify=' + vstrSMSCreditNotify + '&vstrSMSNotifyOnReceive=' + vstrSMSNotifyOnReceive + '&vstrEmailToFax=' + vstrEmailToFax +
                    '&vstrAPIKey=' + vstrAPIKey + '&vstrSecretCode=' + vstrSecretCode + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: "/fax/settings",
                    data: dataString,
                    cache: false,
                    success: function (Response) {
                        $('#UpdateSettingsINFDIV').html(Response)
                    }
                })

            })
        }
    })
});
