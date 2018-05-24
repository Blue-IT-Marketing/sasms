try {


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


}catch(err){

}

var thisUpdateGroupDetailButt = document.getElementById("UpdateGroupDetailButt");

thisUpdateGroupDetailButt.addEventListener("click", function () {

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
                var vstrGroupID = document.getElementById('strGroupID').value;
                var vstrGroupName = document.getElementById('strGroupName').value;
                var vstrGroupDescription = document.getElementById('strGroupDescription').value;
                var thisURL = "/sms/groupman/" + vstrGroupID;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrGroupID=' + vstrGroupID + '&vstrGroupName=' + vstrGroupName +
                    '&vstrGroupDescription=' + vstrGroupDescription + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: thisURL,
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#GroupDetailUpdateINFDIV').html(html)
                    }
                });

            })
        }
    })
});