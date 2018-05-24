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


var thisSurveyInfoButt = document.getElementById("SurveyInfoButt");
var thisSurveyQuestionsButt = document.getElementById("SurveyQuestionsButt");
var thisSurveyResponsesButt = document.getElementById("SurveyResponsesButt");
var thisMakePaymentButt = document.getElementById("MakePaymentButt");

thisSurveyInfoButt.addEventListener("click", function () {
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
                var vstrSurveyID = document.getElementById('strSurveyID').value;
                var thisURL = "/surveys/manage/" + vstrSurveyID;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrSurveyID=' + vstrSurveyID + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: thisURL,
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#SurveyINFDIV').html(html)
                    }
                });
            })
        }
    })
});

thisSurveyQuestionsButt.addEventListener("click", function () {
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
                var vstrSurveyID = document.getElementById('strSurveyID').value;
                var thisURL = "/surveys/manage/" + vstrSurveyID;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrSurveyID=' + vstrSurveyID + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: thisURL,
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#SurveyINFDIV').html(html)
                    }
                });
            })
        }
    })
});

thisSurveyResponsesButt.addEventListener("click", function () {
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
                var vstrSurveyID = document.getElementById('strSurveyID').value;
                var thisURL = "/surveys/manage/" + vstrSurveyID;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrSurveyID=' + vstrSurveyID +  '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: thisURL,
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#SurveyINFDIV').html(html)
                    }
                });
            })
        }
    })
});

thisMakePaymentButt.addEventListener("click", function () {
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
                var vstrSurveyID = document.getElementById('strSurveyID').value;
                var vstrOrderID = document.getElementById('strOrderID').value;
                var thisURL = "/surveys/payments/" + vstrOrderID;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrSurveyID=' + vstrSurveyID + '&vstrOrderID=' + vstrOrderID +  '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: thisURL,
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#SurveyINFDIV').html(html)
                    }
                });
            })
        }
    })
});