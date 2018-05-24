function isEmpty(a){
    if (a == null || a ==''){
        return true;
    }else{
        return false;
    }
}
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

var thisUpdateSurveyButt = document.getElementById("UpdateSurveyButt");
var thisAssignCreditButt = document.getElementById("AssignCreditButt");
thisUpdateSurveyButt.addEventListener("click", function () {
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
                var vstrSurveyID = document.getElementById('strSurveyID').value;
                vstrSurveyName = vstrSurveyName.trim();
                vstrDescription = vstrDescription.trim();

                if (isEmpty(vstrSurveyName) || isEmpty(vstrDescription)) {
                    alert("Please complete all required fields to update your survey")
                } else {
                    var thisURL = "/surveys/manage/" + vstrSurveyID;
                    var dataString = '&vstrChoice=' + vstrChoice + '&vstrSurveyName=' + vstrSurveyName + '&vstrDescription=' + vstrDescription +
                        '&vstrSurveyType=' + vstrSurveyType + '&vstrSurveyID=' + vstrSurveyID + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                    $.ajax({
                        type: "post",
                        url: thisURL,
                        data: dataString,
                        cache: false,
                        success: function (html) {
                            $('#UpdateSurveyINFDIV').html(html)
                        }
                    });
                }
            })
        }
    })
});

thisAssignCreditButt.addEventListener("click", function () {
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
                var vstrSurveyID = document.getElementById("strSurveyID").value;
                var vstrCreditToAssign = document.getElementById("strCreditToAssign").value;
                var vstrAvailableCredit = document.getElementById("strAvailableCredit").value;
                var thisURL = "/surveys/manage/" + vstrSurveyID;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrCreditToAssign=' + vstrCreditToAssign + '&vstrSurveyID=' + vstrSurveyID +
                    '&vstrAvailableCredit=' + vstrAvailableCredit + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: thisURL,
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#UpdateSurveyINFDIV').html(html)
                    }
                });
            })
        }
    })
});

