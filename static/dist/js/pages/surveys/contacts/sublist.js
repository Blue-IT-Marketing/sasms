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
var thisUploadContactButt = document.getElementById("UploadContactButt");
var thisBulkUploadContactsButt = document.getElementById("BulkUploadContactsButt");
var thisRemoveButt = document.getElementById("RemoveButt");
thisUploadContactButt("click", function () {

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
                var vstrListID = document.getElementById('strListID').value;
                var thisURL = "/surveys/contacts/" + vstrListID;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrNames=' + vstrNames + '&vstrSurname=' + vstrSurname +
                    '&vstrCellNumber=' + vstrCellNumber + '&vstrListID=' + vstrListID +
                '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
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

                var vstrChoice = 2;
                //var vstrContactList = $('strContacts').val().split('\n');
                var vstrContactList = document.getElementById('strContacts').value;
                console.log(vstrContactList);
                vstrContactList = vstrContactList.split('\n');
                var vstrThisContactList = "";
                for (thisContact in vstrContactList) {
                    if (isEmpty(vstrThisContactList)) {
                        vstrThisContactList = vstrContactList[thisContact];
                    } else {
                        vstrThisContactList = vstrThisContactList + "|" + vstrContactList[thisContact];
                    }
                }
                console.log(vstrThisContactList);
                var vstrListID = document.getElementById('strListID').value;
                var thisURL = "/surveys/contacts/" + vstrListID;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrContacts=' + vstrThisContactList + '&vstrListID=' + vstrListID +
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

                var vstrChoice = 3;
                var vstrRemoveCell = document.getElementById('strRemoveCell').value;
                var vstrListID = document.getElementById('strListID').value;
                var thisURL = "/surveys/contacts/" + vstrListID;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrListID=' + vstrListID + '&vstrRemoveCell=' + vstrRemoveCell;
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