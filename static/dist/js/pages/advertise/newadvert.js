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

var thisUploadAdvertButt = document.getElementById("UploadAdvertButt");

function isEmpty(a){
    if (a == null || a ==''){
        return true;
    }else{
        return false;
    }
};
function countChar(val) {
var len = val.value.length;
if (len >= 150) {
  val.value = val.value.substring(0, 150);
} else {
  $('#charNum').html("Character Limit = " + (150 - len));
}
}
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


                var vstrChoice = 3;
                var vstrAdvert = document.getElementById('strAdvert').value;
                var vstrPackage = document.getElementById('strPackage').value;
                var vstrStartDate = document.getElementById('strStartDate').value;
                var vstrStartTime = document.getElementById('strStartTime').value;
                vstrAdvert = vstrAdvert.trim();
                vstrPackage = vstrPackage.trim();
                vstrStartDate = vstrStartDate.trim();
                vstrStartTime = vstrStartTime.trim();

                if (isEmpty(vstrAdvert) || isEmpty(vstrPackage) || isEmpty(vstrStartDate) || isEmpty(vstrStartTime)) {
                    alert("Please complete all the fields in this form to submit an advert");
                } else {

                    var dataString = '&vstrChoice=' + vstrChoice + '&vstrAdvert=' + vstrAdvert + '&vstrPackage=' + vstrPackage +
                        '&vstrStartDate=' + vstrStartDate + '&vstrStartTime=' + vstrStartTime + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                    $.ajax({
                        type: "post",
                        url: "/advertise",
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

