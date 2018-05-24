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


var strSelectedGroupsList = [];

function GetGroup(clicked_id){
    if (strSelectedGroupsList.indexOf(clicked_id) < 0){
        strSelectedGroupsList.push(clicked_id);
    }else{
            for(var i = strSelectedGroupsList.length - 1; i >= 0; i--) {
                if(strSelectedGroupsList[i] === clicked_id) {
                   strSelectedGroupsList.splice(i, 1);
                }
            }
    }
}

var thisJoinGroupsButt = document.getElementById("JoinGroupsButt");
thisJoinGroupsButt.addEventListener("click", function () {

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
                var vstrMemberID = document.getElementById('strMemberID').value;
                var vstrGroupList = "";
                for (thisGroup in strSelectedGroupsList) {
                    if (vstrGroupList == "") {
                        vstrGroupList = thisGroup;
                    } else {
                        vstrGroupList = vstrGroupList + "," + thisGroup;
                    }
                }
                var thisURL = "/sms/groupman/" + vstrMemberID;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrMemberID=' + vstrMemberID + '&vstrGroupList=' +
                    vstrGroupList + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: thisURL,
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#ProcessMembershipINFDIV').html(html)
                    }
                });
            })
        }
    })
});