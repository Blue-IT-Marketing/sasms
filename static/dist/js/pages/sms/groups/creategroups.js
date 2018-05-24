
var thisCreateGroupButt = document.getElementById("CreateGroupButt");
thisCreateGroupButt.addEventListener("click", function () {

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
                var vstrGroupName = document.getElementById('strGroupName').value;
                var vstrGroupDescription = document.getElementById('strGroupDescription').value;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrGroupName=' + vstrGroupName +
                    '&vstrGroupDescription=' + vstrGroupDescription + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "get",
                    url: "/admin/sms/groups",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#CreateGroupsINFDIV').html(html)
                    }
                });

            })
        }
    })
});