
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
}else {}}
catch (err){}

tinymce.init({
          selector: '#strArticleEditor',
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

var thisSaveArticleButt = document.getElementById("SaveArticleButt");
var thisDeleteArticleButt = document.getElementById("DeleteArticleButt");
var thisPublishArticleButt = document.getElementById("PublishArticleButt");

thisSaveArticleButt.addEventListener("click", function () {
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

                var vstrArticleHeading = document.getElementById('strArticleHeading').value;
                var vstrURL = document.getElementById('strURL').value;
                var vstrArticleEditor = tinymce.get('strArticleEditor').getContent();
                var vstrListID = document.getElementById('strListID').value;
                var vstrArticleID = document.getElementById('strArticleID').value;

                var dataString = '&vstrChoice=' + vstrChoice + '&vstrArticleHeading=' + vstrArticleHeading + '&vstrArticleEditor=' + vstrArticleEditor +
                    '&vstrListID=' + vstrListID + '&vstrArticleID=' + vstrArticleID + '&vstrURL=' + vstrURL +
                    '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: "/newsletters/editor/" + vstrListID,
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#EditINFDIV').html(html)
                    }
                })
            })
        }
    })
});

thisDeleteArticleButt.addEventListener("click", function () {
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
                var vstrArticleID = document.getElementById('strArticleID').value;
                var vstrListID = document.getElementById('strListID').value;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrArticleID=' + vstrArticleID +
                    '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: "/newsletters/editor/" + vstrListID,
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#EditINFDIV').html(html)
                    }
                })
            })
        }
    })
});
thisPublishArticleButt.addEventListener("click", function () {
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

                var vstrArticleHeading = document.getElementById('strArticleHeading').value;
                var vstrURL = document.getElementById('strURL').value;
                var vstrArticleEditor = tinymce.get('strArticleEditor').getContent();
                var vstrListID = document.getElementById('strListID').value;
                var vstrArticleID = document.getElementById('strArticleID').value;

                var dataString = '&vstrChoice=' + vstrChoice + '&vstrArticleHeading=' + vstrArticleHeading + '&vstrArticleEditor=' + vstrArticleEditor +
                    '&vstrListID=' + vstrListID + '&vstrArticleID=' + vstrArticleID + '&vstrURL=' + vstrURL +
                    '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: "/newsletters/editor/" + vstrListID,
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#EditINFDIV').html(html)
                    }
                });
            })
        }
    })
});
