
var thisUploadNewsLetterButt = document.getElementById("UploadNewsLetterButt");
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
thisUploadNewsLetterButt.addEventListener("click", function () {
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
                var vstrListName = document.getElementById('strListName').value;
                var vstrListDescription = document.getElementById('strListDescription').value;
                var vstrStartSendingDate = document.getElementById('strStartSendingDate').value;
                var vstrStartSendingTime = document.getElementById('strStartSendingTime').value;

                var dataString = '&vstrChoice=' + vstrChoice + '&vstrListName=' + vstrListName + '&vstrListDescription=' + vstrListDescription +
                    '&vstrStartSendingDate=' + vstrStartSendingDate + '&vstrStartSendingTime=' + vstrStartSendingTime +
                '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: "/admin/newsletters",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#UploadNewsLetterINFDIV').html(html)
                    }
                });
            })
        }
    })
});

