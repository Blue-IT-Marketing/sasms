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
function countChar(val) {
var len = val.value.length;
if (len >= 60) {
  val.value = val.value.substring(0, 60);
} else {
  $('#charNumQ').html("Character Limit = " + (60 - len));
}
}
function countChar1(val) {
var len = val.value.length;
if (len >= 20) {
  val.value = val.value.substring(0, 20);
} else {
  $('#charNum1').html("Character Limit = " + (20 - len));
}
}
function countChar2(val) {
var len = val.value.length;
if (len >= 20) {
  val.value = val.value.substring(0, 20);
} else {
  $('#charNum2').html("Character Limit = " + (20 - len));
}
}
function countChar3(val) {
    var len = val.value.length;
    if (len >= 20) {
      val.value = val.value.substring(0, 20);
    } else {
      $('#charNum3').html("Character Limit = " + (20 - len));
    }
}
function countChar4(val) {
    var len = val.value.length;
    if (len >= 20) {
      val.value = val.value.substring(0, 20);
    } else {
      $('#charNum4').html("Character Limit = " + (20 - len));
    }
}

var thisUploadQuestionButt = document.getElementById("UploadQuestionButt");
thisUploadQuestionButt.addEventListener("click",function () {
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
                var vstrQuestion = document.getElementById('strQuestion').value;
                var vstrChoiceOne = document.getElementById('strChoiceOne').value;
                var vstrChoiceTwo = document.getElementById('strChoiceTwo').value;
                var vstrChoiceThree = document.getElementById('strChoiceThree').value;
                var vstrChoiceFour = document.getElementById('strChoiceFour').value;
                var vstrSurveyID = document.getElementById('strSurveyID').value;
                var thisURL = "/surveys/manage/" + vstrSurveyID;

                vstrQuestion = vstrQuestion.trim();
                vstrChoiceOne = vstrChoiceOne.trim();
                vstrChoiceTwo = vstrChoiceTwo.trim();
                vstrChoiceThree = vstrChoiceThree.trim();
                vstrChoiceFour = vstrChoiceFour.trim();

                if (isEmpty(vstrQuestion) || isEmpty(vstrChoice) || isEmpty(vstrChoiceTwo)) {
                    alert("At least your Question and two first choices must be filled in for your survey question to be accepted")
                } else {
                    var dataString = '&vstrChoice=' + vstrChoice + '&vstrSurveyID=' + vstrSurveyID + '&vstrQuestion=' + vstrQuestion +
                        '&vstrChoiceOne=' + vstrChoiceOne + '&vstrChoiceTwo=' + vstrChoiceTwo + '&vstrChoiceThree=' + vstrChoiceThree +
                        '&vstrChoiceFour=' + vstrChoiceFour + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                    $.ajax({
                        type: "post",
                        url: thisURL,
                        data: dataString,
                        cache: false,
                        success: function (html) {
                            $('#UploadQuestionINFDIV').html(html)
                        }
                    });
                }
            })
        }
    })
});

