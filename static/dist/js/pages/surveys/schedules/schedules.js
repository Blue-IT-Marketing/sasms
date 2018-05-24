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

var thisUploadSchedulesButt  = document.getElementById("UploadSchedulesButt");
thisUploadSchedulesButt.addEventListener("click", function () {
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
                var vstrContactList = document.getElementById('strContactList').value;
                var vstrName = document.getElementById('strName').value;
                var vstrDescription = document.getElementById('strDescription').value;
                var vstrStartDate = document.getElementById('strStartDate').value;
                var vstrStartTime = document.getElementById('strStartTime').value;
                // vstrNotifyOnStart if this variable are on check boxes or select boxes modify accordingly
                var vstrNotifyOnStart = document.getElementById('strNotifyOnStart').value;
                var vstrNotifyOnEnd = document.getElementById('strNotifyOnEnd').value;


                var thisURL = "/surveys/schedules";

                var dataString = '&vstrChoice=' + vstrChoice + '&vstrName=' + vstrName + '&vstrDescription=' + vstrDescription +
                    '&vstrStartDate=' + vstrStartDate + '&vstrStartTime=' + vstrStartTime + '&vstrNotifyOnStart=' + vstrNotifyOnStart +
                    '&vstrNotifyOnEnd=' + vstrNotifyOnEnd + '&vstrSurveyID=' + vstrSurveyID + '&vstrContactList=' + vstrContactList +
                 '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "get",
                    url: thisURL,
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#UploadScheduleINFDIV').html(html)
                    }
                });
            })
        }
    })
});