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


var thisMessageButt = document.getElementById("MessageButt");

thisMessageButt.addEventListener("click", function () {

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


                var vstrChoice = 7;
                var vstrSubject = document.getElementById('strSubject').value;
                var vstrMessage = tinyMCE.activeEditor.getContent();
                var vstrCell = document.getElementById('strCell').value;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrSubject=' + vstrSubject + '&vstrMessage=' + vstrMessage + '&vstrCell=' + vstrCell + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: "/admin/contacts/" + vstrCell,
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#MessageINFDIV').html(html)
                    }
                });
            })
        }
    })
});





tinymce.init({
  selector: '#strMessage',
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
