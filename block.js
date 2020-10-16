FRAME_ID="toChange"
AD_ID="MyAdsId3"

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function get_frame()
{
    frame = document.getElementById(FRAME_ID)
    if (frame != null) { return frame.contentWindow.document }
    throw new Error("No frame window!")
}

async function remove_ad()
{
    while (true)
    {
        frame = get_frame()
        ad = frame.getElementById(AD_ID)
        if (ad != null)
        {
            ad.remove()
            return
        }
        await sleep(100)
    }
}

function change_hook(id)
{
    original(id)
    remove_ad()
}

function main()
{
    if (typeof change === "function")
    {
        original = change
        change = change_hook
    }
    try 
    {
        get_frame()
        remove_ad()
    }
    catch {}
}

main()