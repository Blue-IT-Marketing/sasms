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


var thisUploadPostalAddressButt = document.getElementById("UploadPostalAddressButt");
var thisUploadNotesButt = document.getElementById("UploadNotesButt");

var thisUploadPhysicalAddressButt = document.getElementById("UploadPhysicalAddressButt");
tinymce.init({
  selector: '#strNotes',
  height: 710,
  theme: 'modern',
  plugins: [
    'image media codesample imagetools link',
    'advlist autolink lists link image charmap print preview hr anchor pagebreak',
    'searchreplace wordcount visualblocks visualchars code fullscreen',
    'insertdatetime media nonbreaking save table contextmenu directionality',
    'emoticons template paste textcolor colorpicker textpattern imagetools codesample toc help'
  ],

  toolbar1: 'undo redo | insert | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent',
  toolbar2: 'print preview media | forecolor backcolor emoticons | codesample help | link image media codesample',
  image_advtab: true,
  image_caption: true,
  media_live_embeds: true,
  imagetools_cors_hosts: ['tinymce.com', 'codepen.io'],
  templates: [
    { title: 'Test template 1', content: 'Test 1' },
    { title: 'Test template 2', content: 'Test 2' }
  ],
  content_css: [
    '//fonts.googleapis.com/css?family=Lato:300,300i,400,400i',
    '//www.tinymce.com/css/codepen.min.css'
  ]
 });

thisUploadPostalAddressButt.addEventListener("click", function () {
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
                var vstrBox = document.getElementById('strBox').value;
                var vstrCityTown = document.getElementById('strCityTown').value;
                var vstrProvince = document.getElementById('strProvince').value;
                var vstrCountry = document.getElementById('strCountry').value;
                var vstrPostalCode = document.getElementById('strPostalCode').value;
                var vstrContactID = document.getElementById('strContactID').value;
                var vstrCell = document.getElementById('strCell').value;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrBox=' + vstrBox + '&vstrCityTown=' + vstrCityTown +
                    '&vstrProvince=' + vstrProvince + '&vstrCountry=' + vstrCountry + '&vstrPostalCode=' + vstrPostalCode +
                    '&vstrContactID=' + vstrContactID + '&vstrCell=' + vstrCell + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: "/admin/contacts/" + vstrCell,
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#UploadAddressINFDIV').html(html)
                    }
                });
            })
        }
    })
});

thisUploadNotesButt.addEventListener("click", function () {
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
                var vstrCell = document.getElementById('strCell').value;
                var vstrSubject = document.getElementById('strSubject').value;
                var vstrNotes = tinyMCE.activeEditor.getContent();
                var vstrContactID = document.getElementById('strContactID').value;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrSubject=' + vstrSubject + '&vstrNotes=' + vstrNotes + '&vstrContactID=' + vstrContactID +
                    '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: "/admin/contacts/" + vstrCell,
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#UploadNotesINFDIV').html(html)
                    }
                });

            })

        }
    })
});


thisUploadPhysicalAddressButt.addEventListener("click", function () {

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
                var vstrStandNumber = document.getElementById('strStandNumber').value;
                var vstrStreetName = document.getElementById('strStreetName').value;
                var vstrPhyCityTown = document.getElementById('strPhyCityTown').value;
                var vstrPhyProvince = document.getElementById('strPhyProvince').value;
                var vstrPhyCountry = document.getElementById('strPhyCountry').value;
                var vstrPhyPostalCode = document.getElementById('strPhyPostalCode').value;
                var vstrContactID = document.getElementById('strContactID').value;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrStandNumber=' + vstrStandNumber + '&vstrStreetName=' + vstrStreetName +
                    '&vstrPhyCityTown=' + vstrPhyCityTown + '&vstrPhyProvince=' + vstrPhyProvince + '&vstrPhyCountry=' + vstrPhyCountry +
                    '&vstrPhyPostalCode=' + vstrPhyPostalCode + '&vstrContactID=' + vstrContactID +
                '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: "/admin/contacts/" + vstrContactID,
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#UploadPhysicalAddressINFDIV').html(html)
                    }
                });
            })
        }
    })
});
