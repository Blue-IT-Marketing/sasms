  if ('serviceWorker' in navigator) {
    console.log("Will the service worker register?");
    navigator.serviceWorker.register('/service.js',{scope: "/"})
      .then(function(reg){
        console.log("Yes, it did.", reg);
      }).catch(function(err) {
        console.log("No it didn't. This happened: ", err)
      });
  }
