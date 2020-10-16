chrome.runtime.onInstalled.addListener(function(details){
    set_cookie()
});

function set_cookie()
{
    chrome.cookies.set({
        "url" : "https://hindipix.in/",
        "name": "userid",
        "value": "bruh",
        "domain": "hindipix.in",
        "path": "/",
        "secure": true,
        "expirationDate": 1760276035.0,
        "sameSite" : "no_restriction"
    }, function(){})
}

