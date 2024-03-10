function restrictMobile(){
    if (navigator.userAgent.match(/Android/i) || navigator.userAgent.match(/webOS/i) || navigator.userAgent.match(/iPhone/i) || navigator.userAgent.match(/iPad/i) || navigator.userAgent.match(/iPod/i) || navigator.userAgent.match(/BlackBerry/i) || navigator.userAgent.match(/Windows Phone/i)) {
        // the user is using a mobile device, so redirect to the mobile version of the website
        if(window.alert( "This website is not designed for mobile devices. Please use a desktop browser to access this website.")){
            window.close()
        }
        else{
            restrictMobile();
        }
    }
}
restrictMobile();