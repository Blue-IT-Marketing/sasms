/**
 *
 * Consider using this javascript to include all API needed to fully interface with social media and also
 * TODO - we can make use of java script to intergrate social media login options such as those offered by firebase
 * @type {Element}
 */


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


var thisUpdateFacebookGroupsButt = document.getElementById("UpdateFacebookGroupsButt");
var thisUpdateTwitterSettingsButt = document.getElementById("UpdateTwitterSettingsButt");

thisUpdateFacebookGroupsButt.addEventListener("click", function () {
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
                var vstrFacebook = document.getElementById('strFacebook').value;
                var vstrFacebookCodeSecret = document.getElementById('strFacebookCodeSecret').value;
                var vstrGroupIDs = document.getElementById('strGroupIDs').value;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrFacebook=' + vstrFacebook + '&vstrFacebookCodeSecret=' + vstrFacebookCodeSecret +
                    '&vstrGroupIDs=' + vstrGroupIDs + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: "/affiliates",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#UpdateFacebookGroupINFDIV').html(html)
                    }
                });
            })
        }
    })
});

thisUpdateTwitterSettingsButt.addEventListener("click", function () {
    var vstrChoice = 10;
    var dataString = "";
      $.ajax({
            type: "post",
            url: "/affiliates",
            data: dataString,
            cache: false,
          success: function(html){
            $('#UpdateTwitterSettingsINFDIV').html(html)
          }
      });
});