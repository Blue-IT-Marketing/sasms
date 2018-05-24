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


var thisSendMessageButt = document.getElementById("SendMessageButt");
var thisContactFormButt = document.getElementById("ContactFormButt");
var thisSupportTicketsButt = document.getElementById("SupportTicketsButt");
var thisAddressButt = document.getElementById("AddressButt");
//Send Message Handler
thisSendMessageButt.addEventListener("click", function() {
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
                var varstrNames = document.getElementById('strnames').value;
                var varstrCell = document.getElementById('strcell').value;
                var varstrEmail = document.getElementById('stremail').value;
                var varstrsubject = document.getElementById('strsubject').value;
                var varstrmessage = document.getElementById('strmessage').value;

                var dataString = '&vstrChoice=' + vstrChoice + '&vstrNames=' + varstrNames + '&vstrCell=' + varstrCell + '&vstrEmail=' + varstrEmail +
                    '&vstrSubject=' + varstrsubject + '&vstrMessage=' + varstrmessage +
                    '&vstrUserID=' + struid +  '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: "/contact",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#FormResponseDiv').html(html)
                    }
                });
            })
        }else{
                var vstrChoice = 0;
                var varstrNames = document.getElementById('strnames').value;
                var varstrCell = document.getElementById('strcell').value;
                var varstrEmail = document.getElementById('stremail').value;
                var varstrsubject = document.getElementById('strsubject').value;
                var varstrmessage = document.getElementById('strmessage').value;

                var dataString = '&vstrChoice=' + vstrChoice + '&vstrNames=' + varstrNames + '&vstrCell=' + varstrCell + '&vstrEmail=' + varstrEmail +
                    '&vstrSubject=' + varstrsubject + '&vstrMessage=' + varstrmessage ;
                $.ajax({
                    type: "post",
                    url: "/contact",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#FormResponseDiv').html(html)
                    }
                });

        }
    })
});

//Contact Form Handler
thisContactFormButt.addEventListener("click",function () {
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
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: "/contact",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#ContactINFDIV').html(html)
                    }
                });
            })
        }else{
                var vstrChoice = 1;
                var dataString = '&vstrChoice=' + vstrChoice;
                $.ajax({
                    type: "post",
                    url: "/contact",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#ContactINFDIV').html(html)
                    }
                });

        }
    })
});
//Support Ticket Handler
thisSupportTicketsButt.addEventListener("click", function() {
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
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: "/contact",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#ContactINFDIV').html(html)
                    }
                });

            })
        }else{
                var vstrChoice = 2;
                var dataString = '&vstrChoice=' + vstrChoice;
                $.ajax({
                    type: "post",
                    url: "/contact",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#ContactINFDIV').html(html)
                    }
                });
        }
    })
});

thisAddressButt.addEventListener("click", function () {
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
                var dataString = '&vstrChoice=' + vstrChoice  + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: "/contact",
                    data: dataString,
                    cache: false,
                    success: function (Response) {
                        $('#ContactINFDIV').html(Response)
                    }
                })
            })
        }else{
                var vstrChoice = 4;
                var dataString = '&vstrChoice=' + vstrChoice ;
                $.ajax({
                    type: "post",
                    url: "/contact",
                    data: dataString,
                    cache: false,
                    success: function (Response) {
                        $('#ContactINFDIV').html(Response)
                    }
                })

        }
    })
});
