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


var thisSpendCreditButt = document.getElementById("SpendCreditButt");
var thisCalculateWithdrawAmountButt = document.getElementById("CalculateWithdrawAmountButt");
var thisProcessWithdrawalButt = document.getElementById("ProcessWithdrawalButt");

thisSpendCreditButt.addEventListener("click", function () {
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
                var vstrSpendCredit = document.getElementById('strSpendCredit').value;


                var dataString = '&vstrChoice=' + vstrChoice + '&vstrSpendCredit=' + vstrSpendCredit + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: "/affiliates",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#SpendCreditINFDIV').html(html)
                    }
                });

            })
        }
    })
});


thisCalculateWithdrawAmountButt.addEventListener("click", function () {

    var vstrOfferPrice = document.getElementById('strOfferPrice').value;
    vstrOfferPrice = parseInt(vstrOfferPrice);
    var vstrWithDrawCredit = document.getElementById('strWithDrawCredit').value;
    vstrWithDrawCredit = parseInt(vstrWithDrawCredit);
    var vstrAvailableCredit = document.getElementById('strAvailableCredit').value;
    vstrAvailableCredit = parseInt(vstrAvailableCredit);
    if (vstrWithDrawCredit <= vstrAvailableCredit && vstrWithDrawCredit > 0){
        document.getElementById('strWithdrawalAmount').value = (vstrOfferPrice * vstrWithDrawCredit)/100;
    }else{
        if (vstrWithDrawCredit > vstrAvailableCredit){
            document.getElementById('strWithDrawCredit').value = vstrAvailableCredit;
            document.getElementById('strWithdrawalAmount').value = (vstrOfferPrice * vstrAvailableCredit)/100;
        }else{
            document.getElementById('strWithdrawalAmount').value = 0;
        }

    }
});

thisProcessWithdrawalButt.addEventListener("click", function () {
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


                var vstrChoice = 5;
                var vstrWithdrawalAmount = document.getElementById('strWithdrawalAmount').value;
                var vstrSelectMethod = document.getElementById('strSelectMethod').value;
                var vstrWithDrawCredit = document.getElementById('strWithDrawCredit').value;


                var dataString = '&vstrChoice=' + vstrChoice + '&vstrWithdrawalAmount=' + vstrWithdrawalAmount + '&vstrSelectMethod=' + vstrSelectMethod +
                    '&vstrWithDrawCredit=' + vstrWithDrawCredit + '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: "/affiliates",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#ProcessWithdrawalINFDIV').html(html)
                    }
                });
            })
        }
    })
});


// TODO-Consider obtaining data through an ajax interface back to the app
// TODO-We can obtain live data this way thereby enabling us to display real time credits data for affiliates
var WithDrawalsArray = [165, 159, 180, 181, 156, 155, 140,130,250,100,210,224];
var MonthlyCreditArray = [128, 148, 140, 119, 186, 127, 190,200,210,150,234,120];
var LabelsArray = ["January", "February", "March", "April", "May", "June", "July","August","September","October", "November", "December"];

var data = {
  labels: LabelsArray,
  datasets: [
      {
          label: "Monthly Withdrawals",
          fillColor: "rgba(220,220,220,0.2)",
          strokeColor: "rgba(220,220,220,1)",
          pointColor: "rgba(220,220,220,1)",
          pointStrokeColor: "#fff",
          pointHighlightFill: "#fff",
          pointHighlightStroke: "rgba(220,220,220,1)",
          data:WithDrawalsArray
      },
      {
          label: "Monthly Credit",
          fillColor: "rgba(151,187,205,0.2)",
          strokeColor: "rgba(151,187,205,1)",
          pointColor: "rgba(151,187,205,1)",
          pointStrokeColor: "#fff",
          pointHighlightFill: "#fff",
          pointHighlightStroke: "rgba(151,187,205,1)",
          data:MonthlyCreditArray
      }
  ]
};

var ctx = new Chart(document.getElementById("myChart").getContext("2d")).Line(data);

