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
var thisUpdateAccountDetailsButt = document.getElementById("UpdateAccountDetailsButt");
var thisAddCreditsButt = document.getElementById("AddCreditsButt");
var thisUploadDepositSlipButt = document.getElementById("UploadDepositSlipButt");
thisUpdateAccountDetailsButt.addEventListener("click", function () {
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
                var vstrCell = document.getElementById('strCell').value;
                var vstrTel = document.getElementById('strTel').value;
                var vstrEmail = document.getElementById('strEmail').value;
                var vstrWebsite = document.getElementById('strWebsite').value;
                vstrNames = vstrNames.trim();
                vstrSurname = vstrSurname.trim();
                vstrCell = vstrCell.trim();
                vstrTel = vstrTel.trim();
                vstrEmail = vstrEmail.trim();
                vstrWebsite = vstrWebsite.trim();

                if (isEmpty(vstrNames) || isEmpty(vstrSurname) || isEmpty(vstrCell) || isEmpty(vstrEmail)) {
                    alert("Please complete all fields to update your account details")
                } else {
                    var dataString = '&vstrChoice=' + vstrChoice + '&vstrNames=' + vstrNames + '&vstrSurname=' + vstrSurname +
                        '&vstrCell=' + vstrCell + '&vstrTel=' + vstrTel + '&vstrEmail=' + vstrEmail + '&vstrWebsite=' + vstrWebsite +
                    '&vstrUserID=' + struid +  '&vstrAccessToken=' + accessToken;
                    $.ajax({
                        type: "post",
                        url: "/surveys",
                        data: dataString,
                        cache: false,
                        success: function (html) {
                            $('#AccountINFDIV').html(html)
                        }
                    });
                }
            })
        }else{
            alert("Please login to create a survey")
        }
    })
});

thisAddCreditsButt.addEventListener("click", function () {
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
                var vstrTotalCredits = document.getElementById("strTotalCredits").value;
                var vstrAddCredits = document.getElementById("strAddCredits").value;
                var vstrPaymentMethod = document.getElementById("strPaymentMethod").value;
                var dataString = "&vstrChoice=" + vstrChoice + '&vstrTotalCredits=' + vstrTotalCredits + '&vstrAddCredits=' + vstrAddCredits +
                    '&vstrPaymentMethod=' + vstrPaymentMethod + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: "/surveys",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#AddCreditsINFDIV').html(html)
                    }
                });
            })
        }
    })
});



thisUploadDepositSlipButt.addEventListener("click", function () {
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

                var boundary = '-------314159265358979323846';
                var delimiter = "\r\n--" + boundary + "\r\n";
                var close_delim = "\r\n--" + boundary + "--";
                var bucket = "sa-sms.appspot.com";
                var fileData = document.getElementById("strDepositSlipFile").files[0];
                var vstrTopUpReference = document.getElementById("strTopUpReference").value;
                var vstrYourReferenceNumber = document.getElementById("strYourReferenceNumber").value;


                if (isEmpty(vstrTopUpReference) === true) {
                    alert("Error Uploading Deposit Slip")
                } else {
                    var reader = new FileReader();
                    reader.readAsBinaryString(fileData);


                    reader.onload = function (e) {

                        // loading image to canvas
                        const image = new Image();
                        image.src = e.target.result;
                        const $preview = document.getElementById('preview');
                        const previewCtx = $preview.getContext('2d');
                        $preview.width = 600;
                        $preview.height = 600;
                        previewCtx.drawImage(image,0,0);

                        var vstrFilename = "survey-deposit-" + vstrTopUpReference +"."+ fileData.name.split('.').pop();
                        var contentType = fileData.type || 'application/octet-stream';
                        var metadata = {
                            'name': vstrFilename,
                            'mimeType': contentType,
                            'x-goog-project-id': '368838242766'
                        };
                        var base64Data = btoa(reader.result);
                        var multipartRequestBody =
                            delimiter +
                            'Content-Type: application/json\r\n\r\n' +
                            JSON.stringify(metadata) +
                            delimiter +
                            'Content-Type: ' + contentType + '\r\n' +
                            'Content-Transfer-Encoding: base64\r\n' +
                            '\r\n' +
                            base64Data +
                            close_delim;

                        var request = gapi.client.request({
                            'path': '/upload/storage/v1/b/' + bucket + '/o',
                            'method': 'POST',
                            'params': {'uploadType': 'multipart'},
                            'headers': {
                                'Content-Type': 'multipart/mixed; boundary="' + boundary + '"'
                            },
                            'body': multipartRequestBody
                        });
                        try {
                            request.execute(function (resp) {
                                if (resp.hasOwnProperty("error")) {
                                    $('#UploadDepositSlipINFDIV').html("Error Loading File")
                                } else {
                                    var vstrChoice = 0;
                                    var dataString = '&vstrChoice=' + vstrChoice + '&vstrTopUpReference=' + vstrTopUpReference + '&vstrYourReferenceNumber=' + vstrYourReferenceNumber +
                                        '&vstrDepositSlipFile=' + vstrFilename + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                                    $.ajax({
                                        type: "post",
                                        url: "/surveys/topup/invoice/" + vstrTopUpReference,
                                        data: dataString,
                                        cache: false,
                                        success: function (Response) {
                                            $('#UploadDepositSlipINFDIV').html(Response)
                                        }
                                    });
                                }
                            });
                        }
                        catch (e) {
                            $('#UploadDepositSlipINFDIV').html("Error Loading File")
                        }

                    };
                }
            })
        }
    })
});
