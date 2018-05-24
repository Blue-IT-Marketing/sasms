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



var thisUploadContactsButt = document.getElementById("UploadContactsButt");

thisUploadContactsButt.addEventListener("click", function () {
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
                var vstrNames = document.getElementById('strNames').value;
                var vstrSurname = document.getElementById('strSurname').value;
                var vstrCell = document.getElementById('strCell').value;
                var vstrTel = document.getElementById('strTel').value;
                var vstrFax = document.getElementById('strFax').value;
                var vstrEmail = document.getElementById('strEmail').value;
                var vstrWebsite = document.getElementById('strWebsite').value;
                var vstrTitle = document.getElementById('strTitle').value;
                var vstrDateCreated = document.getElementById('strDateCreated').value;

                var dataString = '&vstrChoice=' + vstrChoice + '&vstrNames=' + vstrNames + '&vstrSurname=' + vstrSurname + '&vstrSurname=' + vstrSurname +
                    '&vstrCell=' + vstrCell + '&vstrTel=' + vstrTel + '&vstrFax=' + vstrFax + '&vstrEmail=' + vstrEmail + '&vstrWebsite=' + vstrWebsite +
                    '&vstrDateCreated=' + vstrDateCreated + '&vstrTitle=' + vstrTitle + '&vstrUserID=' + struid + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: "/admin/contacts",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#UploadContactINFDIV').html(html)
                    }
                });

            })
        }
    })
});
