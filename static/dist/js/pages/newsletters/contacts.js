
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
}catch (err) {
}
function isEmpty(a){
    if (a === null || a ===''){
        return true;
    }else{
        return false;
    }
}
var thisUploadContactButt = document.getElementById("UploadContactButt");

thisUploadContactButt.addEventListener("click", function () {
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
                var vstrListID = document.getElementById('strListID').value;
                var vstrNames = document.getElementById('strNames').value;
                var vstrSurname = document.getElementById('strSurname').value;
                var vstrCell = document.getElementById('strCell').value;
                var vstrEmail = document.getElementById('strEmail').value;

                var dataString = '&vstrChoice=' + vstrChoice + '&vstrListID=' + vstrListID + '&vstrEmail=' + vstrEmail + '&vstrCell=' + vstrCell +
                    '&vstrSurname=' + vstrSurname + '&vstrNames=' + vstrNames + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: "/admin/newsletters/" + vstrListID,
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#UploadContactINFDIV').html(html)
                    }
                })
            })
        }
    })
});

