var RECENT_DATA = "<span class='zzazza'><h3 id='nas'> <a>Recently Watched:</a></h3><hr> <br></span><center class='centg' id='recents'></center><br><br><br>"
var CONTINUE_DATA = "<span class='zzazza'><h3 id='nas'> <a>Continue Watching:</a></h3><hr> <br></span><center class='centg' id='continue_watch'></center><br><br><br>"

function insert_to_top(data)
{
    var recents  = document.createElement("div")
    var main_area = document.querySelector(".maingg")

    main_area.insertBefore(recents, main_area.firstChild);
    recents.innerHTML = data
}

function remove_figure(figure, button, name)
{   
    chrome.storage.local.remove(name, function(result){})
    button.remove()
    figure.remove()
}

function create_figure(name, img_src, url, element)
{
    var figure = document.createElement("figure")
    figure.className = "imghvr-flip-diag-1 TVVV"

    var img = document.createElement("img")
    img.src = img_src
    figure.appendChild(img)

    var fig_caption = document.createElement("figcaption")
    fig_caption.innerText = name
    figure.appendChild(fig_caption)

    var link = document.createElement("a")
    link.href = url
    figure.appendChild(link)

    element.appendChild(figure)

    var remove = document.createElement("button")
    remove.style.position = "relative"
    remove.style.top = "20px"
    remove.style.right = "90px"
    remove.innerText = "Remove"
    remove.onclick = function(){remove_figure(figure, remove, name)}

    element.appendChild(remove)
}

function add_figure(name, element)
{
    chrome.storage.local.get([name], function(result) 
    {
        var [img, url] = result[name]
        create_figure(name, img, url, element)
    })
}

function insert_figures()
{
    var recents = document.getElementById("recents")
    chrome.storage.local.get(null, function(items) {
        var allKeys = Object.keys(items);
        allKeys.forEach(function(name, index, array)
        {
            if (name === "CONTINUE WATCHING") 
            {
                insert_to_top(CONTINUE_DATA)
                add_figure(name, document.getElementById("continue_watch"))
                return
            }
            add_figure(name, recents)
        })
    });
}

function main()
{
    document.querySelector("#slideshow").remove()
    insert_to_top(RECENT_DATA)
    insert_figures()
}

main()