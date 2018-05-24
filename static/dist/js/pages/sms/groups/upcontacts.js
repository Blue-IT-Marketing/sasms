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


var thisUploadContactButt = document.getElementById("UploadContactButt");
var thisBulkUploadContactsButt = document.getElementById("BulkUploadContactsButt");
var thisRemoveButt = document.getElementById("RemoveButt");
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

                var vstrChoice = 1;
                var vstrNames = document.getElementById('strNames').value;
                var vstrSurname = document.getElementById('strSurname').value;
                var vstrCellNumber = document.getElementById('strCellNumber').value;
                var vstrGroupID = document.getElementById('strGroupID').value;
                var thisURL = "/sms/groupman/" + vstrGroupID;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrNames=' + vstrNames + '&vstrSurname=' + vstrSurname +
                    '&vstrCellNumber=' + vstrCellNumber + '&vstrGroupID=' + vstrGroupID + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: thisURL,
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

thisBulkUploadContactsButt.addEventListener("click", function () {

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

                var vstrChoice = 9;
                //var vstrContactList = $('strContacts').val().split('\n');
                var vstrContactList = document.getElementById('strContacts').value;
                alert(vstrContactList);
                var vstrContactList = vstrContactList.split('\n');
                var vstrThisContactList = "";
                for (thisContact in vstrContactList) {
                    if (vstrThisContactList == "") {
                        vstrThisContactList = vstrContactList[thisContact];
                    } else {
                        vstrThisContactList = vstrThisContactList + "|" + vstrContactList[thisContact];
                    }
                }
                var vstrGroupID = document.getElementById('strGroupID').value;
                var thisURL = "/sms/groupman/" + vstrGroupID;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrContacts=' + vstrThisContactList + '&vstrGroupID=' + vstrGroupID +
                    '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: thisURL,
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#BulkUploadContactsINFDIV').html(html)
                    }
                });
            })
        }
    })
});


thisRemoveButt.addEventListener("click", function () {


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

                var vstrChoice = 11;
                var vstrGroupID = document.getElementById('strGroupID').value;
                var vstrRemoveCell = document.getElementById('strRemoveCell').value;
                var thisURL = "/sms/groupman/" + vstrGroupID;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrGroupID=' + vstrGroupID + '&vstrRemoveCell=' + vstrRemoveCell +
                 '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: thisURL,
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#RemoveContactINFDIV').html(html)
                    }
                });
            })
        }
    })
});