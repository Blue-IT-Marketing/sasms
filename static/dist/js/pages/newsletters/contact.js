
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
var thisBulkUploadContactsButt = document.getElementById("BulkUploadContactsButt");
var thisUploadContactButt = document.getElementById("UploadContactButt");
var thisRemoveButt = document.getElementById("RemoveButt");


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

                var vstrChoice = 3;
                //var vstrContactList = $('strContacts').val().split('\n');
                vstrContactList = document.getElementById('strContacts').value;
                alert(vstrContactList);
                var vstrContactList = vstrContactList.split('\n');
                var vstrThisContactList = "";
                for (thisContact in vstrContactList) {
                    if (isEmpty(vstrThisContactList) === true ) {
                        vstrThisContactList = vstrContactList[thisContact];
                    } else {
                        vstrThisContactList = vstrThisContactList + "|" + vstrContactList[thisContact];
                    }
                }
                var vstrListID = document.getElementById('strListID').value;
                var thisURL = "/admin/newsletters/" + vstrListID;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrContacts=' + vstrThisContactList + '&vstrListID=' + vstrListID + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: thisURL,
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#BulkUploadContactsINFDIV').html(html)
                    }
                })
            })
        }
    })
});


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

                var vstrChoice = 4;
                var vstrNames = document.getElementById('strNames').value;
                var vstrSurname = document.getElementById('strSurname').value;
                var vstrCellNumber = document.getElementById('strCellNumber').value;
                var vstrEmail = document.getElementById('strEmail').value;
                var vstrListID = document.getElementById('strListID').value;
                var thisURL = "/admin/newsletters/" + vstrListID;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrNames=' + vstrNames + '&vstrSurname=' + vstrSurname +
                    '&vstrCellNumber=' + vstrCellNumber + '&vstrListID=' + vstrListID + '&vstrEmail=' + vstrEmail +
                    '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: thisURL,
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

                var vstrChoice = 5;

                var vstrListID = document.getElementById('strListID').value;
                var vstrRemoveEmail = document.getElementById('strRemoveEmail').value;

                var thisURL = "/admin/newsletters/" + vstrListID;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrListID =' + vstrListID + '&vstrRemoveEmail=' + vstrRemoveEmail +
                    '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: thisURL,
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#RemoveContactINFDIV').html(html)
                    }
                })
            })
        }
    })
});

