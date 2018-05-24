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

var thisEditSMSButt = document.getElementById("EditSMSButt");
var thisManageScheduleButt = document.getElementById("ManageScheduleButt");
var thisSendNowButt = document.getElementById("SendNowButt");
var thisMessageDeliveryReportsButt = document.getElementById("MessageDeliveryReportsButt");

thisEditSMSButt.addEventListener("click", function () {
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
                var vstrMessageID = document.getElementById('strMessageID').value;
                var thisURL = "/sms/manage/" + vstrGroupID;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrGroupID=' + vstrGroupID + '&vstrMessageID=' + vstrMessageID +
                '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: thisURL,
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#SMSINFDIV').html(html)
                    }
                });
            })
        }
    })
});

thisManageScheduleButt.addEventListener("click", function () {
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
                var vstrMessageID = document.getElementById('strMessageID').value;
                var thisURL = "/sms/manage/" + vstrGroupID;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrGroupID=' + vstrGroupID + '&vstrMessageID=' + vstrMessageID +
                '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: thisURL,
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#SMSINFDIV').html(html)
                    }
                });
            })
        }
    })
});

thisSendNowButt.addEventListener("click", function () {
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
                var vstrGroupID = document.getElementById('strGroupID').value;
                var vstrMessageID = document.getElementById('strMessageID').value;
                var thisURL = "/sms/manage/" + vstrGroupID;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrGroupID=' + vstrGroupID + '&vstrMessageID=' + vstrMessageID +
                '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: thisURL,
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#SMSINFDIV').html(html)
                    }
                });
            })
        }
    })
});

thisMessageDeliveryReportsButt.addEventListener("click", function () {
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
                var vstrGroupID = document.getElementById('strGroupID').value;
                var vstrMessageID = document.getElementById('strMessageID').value;
                var thisURL = "/sms/manage/" + vstrGroupID;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrGroupID=' + vstrGroupID + '&vstrMessageID=' + vstrMessageID +
                    '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: thisURL,
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#SMSINFDIV').html(html)
                    }
                });
            })
        }
    })
});
