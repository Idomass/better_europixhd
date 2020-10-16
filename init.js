function add_to_recents()
{
    var img = document.querySelectorAll("[property='og:image']")
    img = img[0].content

    var url = window.location.href

    var leftside = document.querySelector(".leftside")
    var name = leftside.querySelector("span").innerText

    if (name.toLowerCase().includes("season"))
    {
        name = "CONTINUE WATCHING"
    }
    var obj = {};
    obj[name] = [img, url]

    chrome.storage.local.set(obj, 
                             function() {});
}

var s = document.createElement('script');
s.src = chrome.extension.getURL('block.js');
(document.head||document.documentElement).appendChild(s);
s.onload = function() {
    s.parentNode.removeChild(s);
};
add_to_recents()
