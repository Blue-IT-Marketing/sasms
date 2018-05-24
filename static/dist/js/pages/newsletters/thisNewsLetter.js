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

var thisLettersButt = document.getElementById("LettersButt");
var thisContactsButt = document.getElementById("ContactsButt");
var thisScheduleButt = document.getElementById("ScheduleButt");

thisLettersButt.addEventListener("click", function () {
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
                var vstrListID = document.getElementById('strListID').value;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrListID=' + vstrListID +
                    '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: "/admin/newsletters/" + vstrListID,
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#thisNewsLetterINFDIV').html(html)
                    }
                });
            })
        }
    })
});

thisContactsButt.addEventListener("click", function () {
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
                var vstrListID = document.getElementById('strListID').value;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrListID=' + vstrListID +
                    '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: "/admin/newsletters/" + vstrListID,
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#thisNewsLetterINFDIV').html(html)
                    }
                })
            })
        }
    })
});


thisScheduleButt.addEventListener("click", function () {
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

                var vstrChoice = 6;
                var vstrListID = document.getElementById('strListID').value;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrListID=' + vstrListID +
                    '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;

                $.ajax({
                    type: "post",
                    url: "/admin/newsletters/" + vstrListID,
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#thisNewsLetterINFDIV').html(html)
                    }
                })
            })
        }
    })
});

