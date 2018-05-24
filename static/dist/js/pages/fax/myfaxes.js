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
var thisSendFaxButt = document.getElementById("SendFaxButt");
thisSendFaxButt.addEventListener("click", function () {
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
                var vstrToFaxNumber = document.getElementById("strToFaxNumber").value;
                var vstrSubject = document.getElementById("strSubject").value;
                var vstrCoverPage = document.getElementById("strCoverPage").value;
                var vstrAttachFaxes = document.getElementById("strAttachFaxes").files[0];

                var boundary = '-------314159265358979323846';
                var delimiter = "\r\n--" + boundary + "\r\n";
                var close_delim = "\r\n--" + boundary + "--";
                var bucket = "sa-sms.appspot.com";
                var filename = "fax--" + vstrAttachFaxes.name;
                var reader = new FileReader();
                reader.readAsBinaryString(vstrAttachFaxes);

                reader.onload = function (e) {
                    var contentType = vstrAttachFaxes.type || 'application/octet-stream';
                    var metadata = {
                        'name': filename,
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
                                $('#SendFaxINFDIV').html("Error Uploading your attached fax")
                            } else {

                                var dataString = '&vstrChoice=' + vstrChoice + '&vstrToFaxNumber=' + vstrToFaxNumber + '&vstrSubject=' + vstrSubject +
                                    '&vstrCoverPage=' + vstrCoverPage + '&vstrFilename=' + filename +
                                    '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                                $.ajax({
                                    type: "post",
                                    url: "/fax",
                                    data: dataString,
                                    cache: false,
                                    success: function (Response) {
                                        $('#SendFaxINFDIV').html(Response)
                                    }
                                });
                            }
                        });
                    }
                    catch (e) {
                        $('#SendFaxINFDIV').html("Error Loading File")
                    }
                };
            })
        }
    })
});

