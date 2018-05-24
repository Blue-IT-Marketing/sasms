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
if (len >= 150) {
  val.value = val.value.substring(0, 150);
} else {
  $('#charNum').html("Character Limit = " + (150 - len));
}
}

var thisUploadAdvertButt = document.getElementById("UploadAdvertButt");
var thisstrAdvert = document.getElementById("strAdvert");
var thisAssignCreditButt = document.getElementById("AssignCreditButt");


thisUploadAdvertButt.addEventListener("click", function () {

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

                var vstrStartDate = document.getElementById('strStartDate').value;
                var vstrStartTime = document.getElementById('strStartTime').value;
                var vstrAdvertID = document.getElementById('strAdvertID').value;
                vstrAdvert = thisstrAdvert.value;

                vstrStartDate = vstrStartDate.trim();
                vstrStartTime = vstrStartTime.trim();

                if (isEmpty(vstrAdvert) || isEmpty(vstrStartDate) || isEmpty(vstrStartTime)) {
                    alert("Please complete all fields to update your advert")

                } else {

                    var thisURL = "/adverts/manage/" + vstrAdvertID;

                    var dataString = '&vstrChoice=' + vstrChoice + '&vstrAdvert=' + vstrAdvert +
                        '&vstrStartDate=' + vstrStartDate + '&vstrStartTime=' + vstrStartTime +
                        '&vstrAdvertID=' + vstrAdvertID + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                    $.ajax({
                        type: "post",
                        url: thisURL,
                        data: dataString,
                        cache: false,
                        success: function (html) {
                            $('#UploadAdvertINFDIV').html(html)
                        }
                    });
                }
            })
        }
    })
});



thisAssignCreditButt.addEventListener("click", function() {

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


                var vstrChoice = 8;
                var vstrAvailableCredit = document.getElementById("strAvailableCredit").value;
                var vstrAdvertID = document.getElementById("strAdvertID").value;
                var vstrCreditToAssign = document.getElementById("strCreditToAssign").value;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrAvailableCredit=' + vstrAvailableCredit + '&vstrAdvertID=' + vstrAdvertID +
                    '&vstrCreditToAssign=' + vstrCreditToAssign + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;

                $.ajax({
                    type: "post",
                    url: "/adverts/manage/" + vstrAdvertID,
                    data: dataString,
                    cache: false,
                    success: function (Response) {
                        $('#UploadAdvertINFDIV').html(Response)

                    }
                })

            })
        }
    })
});



