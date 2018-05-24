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

function isEmpty(a){
    if (a == null || a ==''){
        return true;
    }else{
        return false;
    }
}
var thisUploadSurveyButt = document.getElementById("UploadSurveyButt");
thisUploadSurveyButt.addEventListener("click", function () {
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
                var vstrSurveyName = document.getElementById('strSurveyName').value;
                var vstrDescription = document.getElementById('strDescription').value;
                var vstrSurveyType = document.getElementById('strSurveyType').value;
                vstrSurveyName = vstrSurveyName.trim();
                vstrDescription = vstrDescription.trim();

                if (isEmpty(vstrSurveyName) || isEmpty(vstrDescription)) {
                    alert("Complete all required fields to create a survey")
                } else {

                    var dataString = '&vstrChoice=' + vstrChoice + '&vstrSurveyName=' + vstrSurveyName + '&vstrDescription=' + vstrDescription +
                        '&vstrSurveyType=' + vstrSurveyType + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                    $.ajax({
                        type: "post",
                        url: "/surveys",
                        data: dataString,
                        cache: false,
                        success: function (html) {
                            $('#UploadSurveyINFDIV').html(html)
                        }
                    });
                }
            })
        }
    })
});
