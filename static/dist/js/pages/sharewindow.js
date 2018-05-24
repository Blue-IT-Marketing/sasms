
function shareThis() {
   navigator.share({
       title: document.title, text: "Hellow world",
       url: window.location.href
   }).then() => {
       console.log("Successfully shared");
    })
}