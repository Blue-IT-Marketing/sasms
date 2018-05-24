


function LoadBlogPost(articleID){
var vstrChoice = 0;
var dataString = '&vstrChoice=' + vstrChoice + '&vstrarticleID=' + articleID;
$.ajax({
    type: "post",
    url: "/blog/" + articleID,
    data: dataString,
    cache: false,
    success: function (Response) {
        $('#BlogINFDIV').html(Response);

        console.log("/blog/"+articleID);
    }
})
}